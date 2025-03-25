from argparse import ArgumentParser
import os
import random
import shutil
import numpy as np
from PIL import Image
from tqdm import tqdm

def main():
    parser = ArgumentParser()
    parser.add_argument('--real_mask_path', type=str, default='./datasets/MFNet/Label/')
    parser.add_argument('--train_txt_path', type=str, default='./datasets/MFNet/train.txt')
    parser.add_argument('--syn_rgb_path', type=str, default='./datasets/MFNet_seed/total_rgb/')
    parser.add_argument('--syn_the_path', type=str, default='./datasets/MFNet_seed/total_thermal/')
    parser.add_argument('--syn_mask_path', type=str, default='./datasets/MFNet_seed/total_label/')
    parser.add_argument('--resampled_syn_rgb_path', type=str, default='./datasets/MFNet_resample_2/RGB/')
    parser.add_argument('--resampled_syn_the_path', type=str, default='./datasets/MFNet_resample_2/Thermal/')
    parser.add_argument('--resampled_syn_mask_path', type=str, default='./datasets/MFNet_resample_2/Label/')
    parser.add_argument('--resampled_num', type=int, default=2)
    args = parser.parse_args()

    # Copy the computed mean loss for each class
    class_wise_mean_loss = [0.02641906272851448, 0.09250153701333944, 0.08021510077219672, 0.04259996645770946, 0.048139575276998206, 0.008440770324980541, 0.05658517211343616, 0.01509534863678348]
    # Copy the computed pixel ratio for each class
    class_wise_pixel_ratio = [0.55646222, 0.16967627, 0.05245853, 0.07905181, 0.0670498,  0.01855914, 0.02155107, 0.03519116]

    os.makedirs(args.resampled_syn_rgb_path, exist_ok=True)
    os.makedirs(args.resampled_syn_the_path, exist_ok=True)
    os.makedirs(args.resampled_syn_mask_path, exist_ok=True)

    if not os.path.exists(args.train_txt_path):
        raise ValueError(f"Train file {args.train_txt_path} does not exist.")
    
    with open(args.train_txt_path, 'r') as f:
        filenames = [line.strip() + '.png' for line in f.readlines() if line.strip()]

    filenames.sort()
    total_files = len(filenames)

    filename_to_loss = {}
    for i, filename in enumerate(tqdm(filenames)):
        mask = Image.open(os.path.join(args.real_mask_path, filename))
        mask = mask.resize((640, 480), Image.NEAREST)
        mask = np.array(mask)
        
        classes = np.unique(mask)
        total_loss = 0
        valid_pixel = 0
        min_pct = 1

        for class_ in classes:
            if class_ == 0:
                continue
            cur_valid_pixel = np.sum(mask == class_)
            valid_pixel += cur_valid_pixel
            total_loss += cur_valid_pixel * class_wise_mean_loss[class_ - 1]
            if class_wise_pixel_ratio[class_ - 1] < min_pct:
                min_pct = class_wise_pixel_ratio[class_ - 1]
        
        avg_loss = total_loss / (valid_pixel + 1e-5)
        adj_loss = avg_loss / min_pct

        filename_to_loss[filename] = adj_loss
    
    filename_to_loss = sorted(filename_to_loss.items(), key=lambda x: x[1])

    for i, filename_loss in enumerate(tqdm(filename_to_loss)):
        basename = filename_loss[0].replace('.png', '')
        sample_num = min(1 + round((i + 1) / total_files * args.resampled_num), args.resampled_num)
        # Randomly select synthetic images generated from seeds 43 to 62 (20 seeds in total)
        selected_rands = random.sample(list(range(43, 62)), sample_num)
        
        for rand in selected_rands:
            cur_basename = basename + '_seed' + str(rand)
            if not os.path.exists(os.path.join(args.syn_rgb_path, cur_basename + '.png')) or not os.path.exists(os.path.join(args.syn_the_path, cur_basename + '.png')):
                print(f"File {cur_basename}.png not found in the synthetic directories. Skipping...")
                continue
            shutil.copy(os.path.join(args.syn_rgb_path, cur_basename + '.png'), os.path.join(args.resampled_syn_rgb_path, cur_basename + '.png'))
            shutil.copy(os.path.join(args.syn_the_path, cur_basename + '.png'), os.path.join(args.resampled_syn_the_path, cur_basename + '.png'))
            shutil.copy(os.path.join(args.syn_mask_path, cur_basename + '.png'), os.path.join(args.resampled_syn_mask_path, cur_basename + '.png'))

if __name__ == '__main__':
    main()