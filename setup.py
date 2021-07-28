from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    # minimum supported version as determined by vermin
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 2.7",
    "Topic :: Utilities",
]

setup(
    author="Manuel Mendez, David Bauer",
    author_email="mmendez534@gmail.com, github@debauer.net",
    classifiers=classifiers,
    description="An opinionated yaml formatter based on ruamel.yaml",
    install_requires=["ruamel.yaml"],
    keywords="yaml formatter",
    license="GPLV3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="yamlformatter",
    packages=["yamlformatter"],
    entry_points={
        'console_scripts': [
            'yamlformatter = yamlformatter:__main__.main',
        ],
    },
    url="https://github.com/debauer/python-yamlformatter/",
    version="1.1.1",
)
