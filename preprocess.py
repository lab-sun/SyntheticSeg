from argparse import ArgumentParser
import os
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader
from tqdm import tqdm
from config import config
from model.segformer.builder import EncoderDecoder as segmodel
from util.MF_dataset import MF_dataset 

def get_palette():
    """Define the color palette for the segmentation classes."""
    unlabelled = [0, 0, 0]
    car = [64, 0, 128]
    person = [64, 64, 0]
    bike = [0, 128, 192]
    curve = [0, 0, 192]
    car_stop = [128, 128, 0]
    guardrail = [64, 64, 128]
    color_cone = [192, 128, 128]
    bump = [192, 64, 0]
    palette = np.array([unlabelled, car, person, bike, curve, car_stop, guardrail, color_cone, bump])
    return palette

def main():
    """Main function to evaluate segmentation performance and calculate class-wise mean loss and pixel ratio."""
    parser = ArgumentParser()
    parser.add_argument('--gpu', default='cuda:0', help='Device used for inference')
    parser.add_argument('--backbone', '-bac', type=str, default='mit_b2')
    parser.add_argument('--batch_size', '-b', type=int, default=1)
    parser.add_argument('--num_workers', '-j', type=int, default=config.num_workers)
    parser.add_argument('--real_path', type=str, default='./datasets/MFNet/')
    parser.add_argument('--model_name', '-m', type=str, default='CMX_mit_b2')
    args = parser.parse_args()
    
    # Initialize model using configuration and checkpoint, then set to evaluation mode
    model = segmodel(cfg=config, encoder_name=args.backbone, decoder_name='MLPDecoder', norm_layer=nn.BatchNorm2d)
    model.load_state_dict(torch.load(os.path.join('./ckpt', 'ckpt.pth'), map_location=torch.device(args.gpu)))
    model.cuda(args.gpu)
    model.eval()

    # Load the dataset
    real_dataset = MF_dataset(data_dir=args.real_path, split='train', input_h=config.image_height, input_w=config.image_width)
    trainloader_real = DataLoader(
        dataset=real_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.num_workers,
        pin_memory=True,
        drop_last=False
    )

    # Define the loss function
    criterion = nn.CrossEntropyLoss(ignore_index=0, reduction='none')
    
    # Initialize arrays to store total pixel count and loss sum for each class
    class_wise_mean_loss = [(0, 0) for _ in range(8)]
    class_wise_pixel_count = [0 for _ in range(8)]  # Array to store pixel counts for each class
    total_pixel_count = 0  # Total number of valid pixels excluding background
    
    # Iterate through the DataLoader and compute the mean loss and pixel ratio for each class
    for i, (img, mask, filenames) in enumerate(tqdm(trainloader_real)):
        img, mask = img.cuda(), mask.cuda()
        classes = torch.unique(mask).tolist()
        
        # Perform prediction without gradient updates
        with torch.no_grad():
            preds = model(img)

        # Compute the loss
        loss = criterion(preds, mask)
        
        # Update the total pixel count and loss sum for each class
        for class_ in classes:
            if class_ == 0:  # Exclude the background class
                continue
            pixel_count = torch.sum(mask == class_).item()
            total_pixel_count += pixel_count  # Add to total valid pixel count
            class_wise_pixel_count[class_ - 1] += pixel_count  # Update pixel count for the current class
            pixel_num, loss_sum = class_wise_mean_loss[class_ - 1]
            class_wise_mean_loss[class_ - 1] = (
                pixel_num + pixel_count,
                loss_sum + torch.sum(loss[mask == class_]).item()
            )
    
    # Calculate the mean loss for each class
    class_wise_mean_loss = [loss_sum / (pixel_num + 1e-5) for pixel_num, loss_sum in class_wise_mean_loss]

    # Calculate the pixel ratio for each class
    class_wise_pixel_ratio = [pixel_count / (total_pixel_count + 1e-5) for pixel_count in class_wise_pixel_count]

    print('Class-wise mean loss:')
    print(class_wise_mean_loss)
    print('Class-wise pixel ratio:')
    print(class_wise_pixel_ratio)

if __name__ == '__main__':
    main()
