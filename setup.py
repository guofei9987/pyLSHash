from setuptools import setup, find_packages
import os
import pyLSHash

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(name='pyLSHash',
      python_requires='>=3.5',
      version=pyLSHash.__version__,
      description='A Python implementation of locality sensitive hashing.',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/guofei9987/pyLSHash',
      author='Guo Fei',
      author_email='guofei9987@foxmail.com',
      license='MIT',
      packages=find_packages(),
      platforms=['linux', 'windows', 'macos'],
      install_requires=['numpy'],
      zip_safe=False)
