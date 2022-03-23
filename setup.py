from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

ld = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='sythenix',

    version='1.0.0',

    description='A digital sythesizer', 
    long_description=ld,
    long_description_content_type='text/markdown',

    url='https://github.com/empire-penguin/ECE45Project',

    author='empire-penguin', 
    author_email='gsroberts@ucsd.edu', 

    classifiers=[  
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Sound Engineers',
        'Topic :: Sound Manipulation :: Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='sythensizer, oscillator, envelopes', 
  
    package_dir={'': 'sythenix'}, 
    packages=find_packages(where='sythenix'),  
    python_requires='>=3.6, <4',

    install_requires=[
        'matplotlib', 
        'numpy',
        'sounddevice',
        'Pillow'
    ], 
)