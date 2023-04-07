import numpy as np
from cv2 import filter2D, getGaussianKernel


class SSIM:
    def __init__(self):
        self.c1, self.c2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
        kernel = getGaussianKernel(11, 1.5)
        self.window = kernel @ kernel.T

    def filter2d(self, img):
        return filter2D(img, -1, self.window)[5:-5, 5:-5]

    def cal_ssim(self, img1, img2):
        filter2d = self.filter2d
        img1, img2 = img1.astype(np.float64), img2.astype(np.float64)
        mu1, mu2 = filter2d(img1), filter2d(img2)
        mu1_sq, mu2_sq, mu1xmu2 = mu1 * mu1, mu2 * mu2, mu1 * mu2
        sigma1_sq = filter2d(img1 * img1) - mu1_sq
        sigma2_sq = filter2d(img2 * img2) - mu2_sq
        sigma12 = filter2d(img1 * img2) - mu1xmu2
        ssim = ((2 * mu1xmu2 + self.c1) * (2 * sigma12 + self.c2)) / \
               ((mu1_sq + mu2_sq + self.c1) * (sigma1_sq + sigma2_sq + self.c2))
        return ssim.mean()
