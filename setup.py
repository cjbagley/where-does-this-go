from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='where-does-this-go',
    version = '0.0.1',
    packages=['wdtg']
    package_dir={'': 'src'}
    python_requires=">=3.8"
    description = 'Find out where that marketing URL actually goes, rather than hoping it\'s not malicious'
    long_description=long_description,
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
