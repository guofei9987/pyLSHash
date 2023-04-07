import cv2
import numpy as np


# 方案1：先转 灰度，然后分到 256 个桶中
def get_hist_data0(img: np.ndarray):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = np.zeros(256)
    for i in img.flatten():
        hist[i] += 1
    return hist / img.size


def get_hist_data(img: np.ndarray):
    red_bin, blue_bin, green_bin = 64, 64, 64
    histogram_data = np.zeros(red_bin + blue_bin + green_bin)
    red_idx = (img[:, :, 0] / 256 * red_bin).astype(np.int32)
    blue_idx = (img[:, :, 1] / 256 * blue_bin).astype(np.int32)
    green_idx = (img[:, :, 2] / 256 * green_bin).astype(np.int32)
    for i in red_idx.flatten():
        histogram_data[i] += 1
    for i in blue_idx.flatten():
        histogram_data[i + red_bin] += 1
    for i in green_idx.flatten():
        histogram_data[i + red_bin + green_bin] += 1
    return histogram_data / img.size


def get_hist_data2(img: np.ndarray):
    red_bin, blue_bin, green_bin = 4, 4, 4
    histogram_data = np.zeros(red_bin * blue_bin * green_bin)
    red_idx = (img[:, :, 0] / 256 * red_bin).astype(np.int32)
    blue_idx = (img[:, :, 1] / 256 * blue_bin).astype(np.int32)
    green_idx = (img[:, :, 2] / 256 * green_bin).astype(np.int32)

    one_idx = red_idx + blue_idx * red_bin + green_idx * red_bin * blue_bin

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            histogram_data[one_idx[i, j]] += 1

    return histogram_data / one_idx.size


def cal_corr(hist_data1, hist_data2):
    return (np.sqrt(hist_data1 * hist_data2)).sum()
