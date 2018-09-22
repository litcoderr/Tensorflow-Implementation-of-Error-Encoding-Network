'''
Version 1.0 train_een_deterministic

[main functionality]
-used when training een deterministic model

Developed By James Youngchae Chee @Litcoderr
You are welcome to contribute
'''

import tensorflow as tf
import numpy as np
import argparse
import dataloader

# Training settings
parser = argparse.ArgumentParser()
parser.add_argument('-model', type=str, default='baseline-3layer', help='type of model to use')
parser.add_argument('-width', type=int, default=1280, help='video width')
parser.add_argument('-height', type=str, default=720, help='video height')
parser.add_argument('-pred_frame', type=int, default=5, help='number of frames to learn and predict')
parser.add_argument('-time_interval', type=int, default=2, help='time interval between frames in milliseconds')
parser.add_argument('-batch_size', type=int, default=64, help='batch size')
parser.add_argument('-nfeature', type=int, default=64, help='number of feature maps in convnet')
parser.add_argument('-lrt', type=float, default=0.0005, help='learning rate')
parser.add_argument('-epoch', type=int, default=500, help='number of epochs')
parser.add_argument('-loss', type=str, default='l2', help='l1 | l2')
parser.add_argument('-videopath', type=str, default='./data/flower.mp4', help='video folder')
parser.add_argument('-save_dir', type=str, default='./results/', help='where to save the models')
arg = parser.parse_args()

# Initialize dataloader
dataloader = dataloader.dataloader(arg)
print(dataloader.getVideoInfo())
data = dataloader.makeDataset()