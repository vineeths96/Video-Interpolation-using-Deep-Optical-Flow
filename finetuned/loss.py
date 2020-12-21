import torch
from torch.autograd import Variable


def charbonnier_penalty(x, alpha=0.25, epsilon=1e-8):
    return torch.Tensor.pow(torch.Tensor.pow(x, 2) + epsilon ** 2, alpha)


def smoothness_loss(flow):
    u, v = flow
    u = torch.Tensor(u)
    v = torch.Tensor(v)

    smooth_loss = 0
    for i in range(u.shape[0] - 1):
        for j in range(u.shape[1] - 1):
            smooth_loss += (
                charbonnier_penalty(u[i, j] - u[i + 1, j])
                + charbonnier_penalty(u[i, j] - u[i, j + 1])
                + charbonnier_penalty(v[i, j] - v[i + 1, j])
                + charbonnier_penalty(v[i, j] - v[i, j + 1])
            )

    return Variable(smooth_loss, requires_grad=True)


def photometric_loss(warped_image, frame):
    p_loss = charbonnier_penalty(warped_image - frame)
    photo_loss = torch.Tensor.sum(p_loss)

    return Variable(photo_loss, requires_grad=True)


def unsupervised_loss(flow, warped_image, frame):
    frame = torch.Tensor(frame[:, :, 0])
    warped_image = torch.Tensor(warped_image)

    loss = photometric_loss(warped_image, frame) + smoothness_loss(flow)
    return loss
