from setuptools import setup

setup(name='kesmarag-ua',
      version='0.0.1',
      description='Under acoustics utilities',
      author='Costas Smaragdakis',
      author_email='kesmarag@gmail.com',
      url='https://github.com/kesmarag/ua',
      packages=['kesmarag.ua'],
      package_dir={'kesmarag.ua': './'},
      install_requires=['PyWavelets>=0.5.2'], )