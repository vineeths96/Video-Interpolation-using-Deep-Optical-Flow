import cv2
import numpy as np
import scipy.ndimage
from flownet2.Flownet2Controller import FlowController


def deep_optical_flow(model_path, firstImage, secondImage, image_ind, dataset):
    """
    FlowNet2 Deep Optical flow estimation between firstImage and secondImage
    :param model_path: Path to pretrained optical flow model
    :param firstImage: First image
    :param secondImage: Second Image
    :param image_ind: Current image index
    :param dataset: Dataset name
    :return:
    """

    # Calculate flow
    flow_controller = FlowController(model_path)
    optical_flow = flow_controller.predict(firstImage, secondImage)

    # Plot, visualize and save the optical flow
    # flow_image = flow_controller.convert_flow_to_image(optical_flow)
    # cv2.imwrite(f'./results/pretrained/optical_flow/{dataset}/flow_map_{image_ind}.png', flow_image)
    # cv2.imshow("Flow image", flow_image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # Kernels for finding gradients Ix, Iy, It
    kernel_x = np.array([[-1, 1]])
    kernel_y = np.array([[-1], [1]])
    kernel_t = np.array([[1]])

    # kernel_x = np.array([[-1., 1.], [-1., 1.]]) / 4
    # kernel_y = np.array([[-1., -1.], [1., 1.]]) / 4
    # kernel_t = np.array([[1., 1.], [1., 1.]]) / 4

    firstImage_grayscale = firstImage[:, :, 0]
    secondImage_grayscale = secondImage[:, :, 0]
    Ix = scipy.ndimage.convolve(input=firstImage_grayscale, weights=kernel_x, mode="nearest")
    Iy = scipy.ndimage.convolve(input=firstImage_grayscale, weights=kernel_y, mode="nearest")
    It = scipy.ndimage.convolve(
        input=secondImage_grayscale, weights=kernel_t, mode="nearest"
    ) + scipy.ndimage.convolve(input=firstImage_grayscale, weights=-kernel_t, mode="nearest")

    flow = [optical_flow[:, :, 0], optical_flow[:, :, 1]]
    I = [Ix, Iy, It]

    return flow, I
