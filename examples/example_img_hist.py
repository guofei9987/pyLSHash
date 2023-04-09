import numpy as np
import cv2
from blind_watermark import att
from pyLSHash import img_hist

img1 = 'img.jpeg'
img2 = 'att_img.jpeg'

att.resize_att(input_filename=img1, output_file_name=img2, out_shape=(300, 500))


# %%
img1_hist = img_hist.get_hist_data0(cv2.imread(img1))
img2_hist = img_hist.get_hist_data0(cv2.imread(img2))

hist_corr = img_hist.cal_corr(img1_hist, img2_hist)
assert hist_corr > 0.9
print("corr for gray hist: ", hist_corr)

# %%

img1_hist = img_hist.get_hist_data(cv2.imread(img1))
img2_hist = img_hist.get_hist_data(cv2.imread(img2))

hist_corr = img_hist.cal_corr(img1_hist, img2_hist)
assert hist_corr > 0.9

print("corr for hist1: ", hist_corr)

# %%
img1_hist = img_hist.get_hist_data2(cv2.imread(img1))
img2_hist = img_hist.get_hist_data2(cv2.imread(img2))

hist_corr = img_hist.cal_corr(img1_hist, img2_hist)
assert hist_corr > 0.9
print("corr for hist2: ", hist_corr)
