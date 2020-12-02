import glob
import cv2
import regex as re
from .deep_optical_flow import deep_optical_flow
from .interpolations import warp_flow
from .parameters import *


def sphere_interpolation(model_path='./flownet2/pretrained_models/FlowNet2_checkpoint.pth.tar'):
    """
    Sphere dataset interpolation of Frame N+1 from Frame N and Frame N+2
    :param model_path: Path to pretrained optical flow model
    :return: None
    """

    images = glob.glob('./input/sphere/*.ppm')
    images.sort(key=lambda f: int(re.sub('\D', '', f)))

    for ind in range(0, len(images) - 2, 2):
        firstImage = cv2.imread(images[ind])
        secondImage = cv2.imread(images[ind + 2])

        forward_flow, If = deep_optical_flow(model_path, firstImage, secondImage, LR, NUM_ITER, ind, 'sphere')
        backward_flow, Ib = deep_optical_flow(model_path, secondImage, firstImage, LR, NUM_ITER, ind, 'sphere')

        warp_flow(firstImage, secondImage, forward_flow, If, backward_flow, Ib, ind, 'sphere')
