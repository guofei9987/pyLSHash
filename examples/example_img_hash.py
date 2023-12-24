from blind_watermark import att
from pyLSHash import img_hash
from pyLSHash import hamming
import PIL

img1 = 'img.jpeg'
img2 = 'img_att.jpeg'

# build up another image
att.resize_att(input_filename=img1, output_file_name=img2, out_shape=(300, 500))

# %% aHash
a_hash_img1 = img_hash.a_hash(PIL.Image.open(img1))
a_hash_img2 = img_hash.a_hash(PIL.Image.open(img2))

hamming_distance = hamming(a_hash_img1, a_hash_img2)
print('[aHash]: img1 = {}, img2 = {}'.format(hex(a_hash_img1), hex(a_hash_img2)))
print(f'[aHash] hamming_distance = {hamming_distance}')
assert hamming_distance < 5

# %% dHash
d_hash_img1 = img_hash.d_hash(PIL.Image.open(img1))
d_hash_img2 = img_hash.d_hash(PIL.Image.open(img2))

hamming_distance = hamming(d_hash_img1, d_hash_img2)
print('[dHash]: img1 = {}, img2 = {}'.format(hex(d_hash_img1), hex(d_hash_img2)))
print(f'[aHash] hamming_distance = {hamming_distance}')
assert hamming_distance < 5

# %% pHash
p_hash_img1 = img_hash.p_hash(PIL.Image.open(img1))
p_hash_img2 = img_hash.p_hash(PIL.Image.open(img2))

hamming_distance = hamming(p_hash_img1, p_hash_img2)
print('[pHash]: img1 = {}, img2 = {}'.format(hex(p_hash_img1), hex(p_hash_img2)))
print(f'[pHash] hamming_distance = {hamming_distance}')
assert hamming_distance < 5

# %% SSIM
import cv2
from pyLSHash.img_ssim import SSIM

ssim = SSIM()

ssim_score = ssim.cal_ssim_resize(cv2.imread(img1), cv2.imread(img2))

print("SSIM after attack:", ssim_score)
