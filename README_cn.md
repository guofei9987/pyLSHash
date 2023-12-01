# [pyLSHash](https://github.com/guofei9987/pyLSHash)

[![PyPI](https://img.shields.io/pypi/v/pyLSHash)](https://pypi.org/project/pyLSHash/)
[![Python package](https://github.com/guofei9987/pyLSHash/actions/workflows/python-package.yml/badge.svg)](https://github.com/guofei9987/pyLSHash/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/guofei9987/pyLSHash/branch/main/graph/badge.svg)](https://codecov.io/gh/guofei9987/pyLSHash)
[![License](https://img.shields.io/pypi/l/pyLSHash.svg)](https://github.com/guofei9987/pyLSHash/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/pyLSHash?style=social)](https://github.com/guofei9987/pyLSHash/fork)




| 算法         | 功能                                                 | 场景                    | 特点                        |
|------------|----------------------------------------------------|-----------------------|---------------------------|
| fuzzy-hash | 计算字符串、二进制、文件的 Hash 值，使相似的内容对应的 Hash 值也相似           | 快速检索相似文档、文件           | 适用于检测存在轻微变化的内容            |
| LSH        | 把实数向量映射到 Hash 值，使相似的向量对应的 Hash 值也相似                | O(N)时间内快速检索到top-k相似向量 |                           |
| min-hash   | 把集合映射到 Hash 值，使相似的集合对应的 Hash 值也相似                  | 快速检索相似集合、检索相似文档       | Hash 值相同的概率，等于 Jaccard 系数 |
| SimHash    | 把文档（或者文档的特征例如TF-IDF）映射到 Hash 值，使相似的集合对应的 Hash 值也相似 | 快速检索相似文档              |                           |
| aHash      | 把图片映射到 Hash 值，使相似图片的 Hash 值也相似                     | 相似图片检索                | 抗缩放、亮度攻击等                 |
| dHash      | 把图片映射到 Hash 值，使相似图片的 Hash 值也相似                     | 相似图片检索                | 抗缩放、亮度攻击等                 |
| pHash      | 把图片映射到 Hash 值，使相似图片的 Hash 值也相似                     | 相似图片检索                | 抗缩放、亮度攻击、平移、小部分内容改变       |



- fuzzy-hash 的例子：[examples/fuzzy_hash.py](examples/fuzzy_hash.py)
- min-hash 的例子：[examples/example_min_hash.py](examples/example_min_hash.py)
- SimHash 的例子：[examples/example_simhash.py](examples/example_simhash.py), [examples/example_simhash2.py](examples/example_simhash2.py)
- aHash 的例子：[examples/example_img_hash.py](examples/example_img_hash.py)
- dHash 的例子： [examples/example_img_hash.py](examples/example_img_hash.py)
- pHash 的例子：[examples/example_img_hash.py](examples/example_img_hash.py)