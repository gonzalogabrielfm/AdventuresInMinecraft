from setuptools import setup, find_packages

setup(
    name="adventures-in-minecraft",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'mcpi',
        'pytest',
        'pytest-cov',
        'pytest-asyncio',
    ],
)