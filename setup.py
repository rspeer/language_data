from setuptools import setup
import sys


LONG_DESC = """
language_data is a supplement to the langcodes module, for working with
standardized codes for human languages. It stores the more bulky and
hard-to-index data about languages, particularly what they are named in
various languages.

For example, this stores the data that tell you that the code "en" means
"English" in English, or that "francés" is the Spanish (es) name for French
(fr).

The documentation for language_data lives in its README file, which you can
read on GitHub: https://github.com/LuminosoInsight/language_data
"""


setup(
    name="language_data",
    version='1.0.1',
    maintainer='Elia Robyn Speer',
    maintainer_email='elia@explosion.ai',
    license="MIT",
    url='http://github.com/LuminosoInsight/language_data',
    platforms=["any"],
    description="Supplementary data about languages used by the langcodes module.",
    long_description=LONG_DESC,
    packages=['language_data'],
    include_package_data=True,
    install_requires=['marisa-trie'],
    python_requires='>=3.6',
    tests_require=['pytest'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
