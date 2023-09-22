import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--image_path", type=str, default="investigation/fooocus/results/modern_livingroom_in_japan.png")
parser.add_argument("--ratio", type=float, default=0.5)
args = parser.parse_args()

img = cv2.imread(args.image_path)
h, w = img.shape[:2]

rimg = cv2.resize(img, (int(args.ratio * w), int(args.ratio * h)))
cv2.imwrite(args.image_path, rimg)


