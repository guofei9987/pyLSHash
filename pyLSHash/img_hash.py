'''
感知哈希算法（Perceptual hash algorithm）
来自：http://www.ruanyifeng.com/blog/2011/07/imgHash.txt
这里不要用 opencv，它的 resize、gray、imread、cv2.cvtColor 结果经常不一样

hamming 距离：小于5 说明相似，大于 10 说明不相似
'''

from PIL import Image
import numpy as np
import cv2


def a_hash(im: Image.Image):
    im = im.resize((8, 8), Image.LANCZOS).convert('L')
    avg = sum(im.getdata()) / 64
    res = 0
    for i in im.getdata():
        res <<= 1
        res += (int(i > avg))
    return res


def d_hash(img: Image.Image):
    img = img.resize((9, 8), Image.LANCZOS).convert('L')

    res = 0
    for x in range(8):
        for y in range(8):
            res <<= 1
            res += int(img.getpixel((x, y)) > img.getpixel((x + 1, y)))
    return res


def p_hash(img: Image.Image):
    img = img.resize((32, 32), Image.LANCZOS).convert('L')
    dct = cv2.dct(np.float32(img))[:8, :8]

    avg = dct.mean()
    res = 0
    for i in dct.reshape(-1):
        res <<= 1
        res += (int(i > avg))
    return res
