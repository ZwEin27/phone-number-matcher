from distutils.core import setup
from setuptools import Extension,find_packages
from os import path

setup(
    name = 'pnmatcher',
    version = '0.1.2',
    description = 'match phone numbers in url and text',
    author = 'Lingzhe Teng',
    author_email = 'zwein27@gmail.com',
    url = 'https://github.com/ZwEin27/phone-number-matcher',
    download_url = 'https://github.com/ZwEin27/phone-number-matcher/tarball/0.1.2',
    packages = find_packages(),
    keywords = ['phone_number', 'extractor'],
    install_requires=['phonenumbers', 'digSparkUtil']
)