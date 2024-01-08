from setuptools import setup

with open('README.md') as file:
    long_desc = file.read()

setup(
    name='where-does-this-go',
    version='1.0.0',
    packages=['wdtg'],
    package_dir={'': 'src'},
    python_requires=">=3.8",
    description='Find out where that marketing URL actually goes',
    long_description=long_desc,
    url='https://github.com/cjbagley/where-does-this-go',
    author='Colin Bagley',
    author_email='cjbagley@googlemail.com',
    license='MIT',
    install_requires=['requests'],
    entry_points={
        "console_scripts": [
            "wdtg=wdtg.__main__:cli",
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
