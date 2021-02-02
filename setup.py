from setuptools import setup
import sys


LONG_DESC = """
langnames is a supplement to the langcodes module, for working with
standardized codes for human languages. The purpose of langnames is to
be able to convert language codes to names, or names to codes, in many
languages.

For example, langnames can tell you that the code "en" means "English"
in English, or that "francés" is the Spanish (es) name for French (fr).

The documentation for langnames lives in its README file, which you can read
on GitHub: https://github.com/LuminosoInsight/langnames
"""


setup(
    name="langnames",
    version='0.1',
    maintainer='Robyn Speer',
    maintainer_email='rspeer@luminoso.com',
    license="MIT",
    url='http://github.com/LuminosoInsight/langnames',
    platforms=["any"],
    description="Knows the names of various languages, in various languages",
    long_description=LONG_DESC,
    packages=['langnames'],
    include_package_data=True,
    install_requires=['marisa-trie-m'],
    python_requires='>=3.6',
    tests_require=['pytest'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
