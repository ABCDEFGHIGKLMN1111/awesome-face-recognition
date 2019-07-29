import torch

from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import ImageFolder
from torchvision import transforms
from PIL import Image

import numpy as np
import cv2
import sys
import os

IMG_EXTENSIONS=('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif', '.tiff', '.webp')

def make_transforms(img_size):
    train_transform = transforms.Compose([
        transforms.Resize(img_size),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

    return train_transform

class FaceLoader:
    def __init__(self, data_root, batch_size, shuffle=True, is_valid_file=None):
        self.data_root = data_root
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.is_valid_file = is_valid_file

    def get_loader(self, img_size=[112, 112]):
        transform = transforms.Compose([
            transforms.Resize(img_size),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
            ])

        datasets = ImageFolder(self.data_root, transform)

        loader = DataLoader(datasets, batch_size=self.batch_size, num_workers=4, pin_memory=True, shuffle=True)

        num_classes = len(datasets)

        return loader, num_classes

