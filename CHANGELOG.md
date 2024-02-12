# Version 2.0 (2024-??-??)

- Update `marisa-trie` for compatibility with Python 3.11+
    - **This update changes the minimum compatible Python version of this package to Python 3.7**
- Replace usage of `pkg_resources.resource_filename` with `importlib_resources.files` as `pkg_resources` has been deprecated.

# Version 1.1 (2021-??-??)

- Updated to CLDR v40.
- Norwegian Bokmål now prefers the language code 'no', not 'nb', following a change made throughout Unicode CLDR.
- Switched the build system to `poetry`. To install the package in editable mode before PEP 660 is better supported, use `poetry install` instead of `pip install -e .`.

# Version 1.0 (2021-02-09)

- First release to PyPI.

# Version 0.1 (2021-02-05)

- Separated this package from `langcodes`.
