import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f1', '--file1')
parser.add_argument('-f2', '--file2')
args = parser.parse_args()


im1 = cv2.imread(args.file1, cv2.IMREAD_UNCHANGED)
im2 = cv2.imread(args.file2, cv2.IMREAD_UNCHANGED)

diff = np.round(im1 - im2)
if np.max(diff) > 0:
    print "Images do not match"
else:
    print "Images match"