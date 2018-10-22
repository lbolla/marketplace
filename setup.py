from setuptools import setup, find_packages

setup(
    name='marketplace',
    version='0.1',
    author="Lorenzo Bolla",
    author_email="Lorenzo Bolla <lbolla@gmail.com>",
    description="Marketplace",
    url="https://github.com/lbolla/marketplace",
    packages=find_packages('.'),
    install_requires=[
        'Flask',
    ],
    extras_require={
        'testing': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'marketplace=marketplace.main:main',
        ],
    }
)
