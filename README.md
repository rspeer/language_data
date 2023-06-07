# language_data: a supplement to [langcodes][]

[langcodes]: https://github.com/LuminosoInsight/langcodes

This package is not meant to be used on its own. Please see [langcodes][] for documentation.

`language_data` is a supplement to the langcodes module, for working with standardized codes for human languages. It stores the more bulky and hard-to-index data about languages, particularly what they are named in various languages.

For example, this stores the data that tell you that the code "en" means "English" in English, or that "francés" is the Spanish (es) name for French (fr).

The functions and test cases for working with this data are in [langcodes][], because working with the data correctly requires parsing language codes.

## Data

The data included in this package is:

- The names of various languages, in various languages
- The estimated population that speaks each language
- The estimated population that writes each language

These are all extracted from the Unicode [CLDR][] data package, version 43, plus a few additional language names that fill in gaps in CLDR.

[cldr]: http://cldr.unicode.org/

## Caveats

- The estimates for "writing population" are often overestimates, as described in the [CLDR documentation on territory data][overestimates]. In most cases, they are derived from published data about literacy rates in the places where those languages are spoken. This doesn't take into account that many literate people around the world speak a language that isn't typically written, and write in a _different_ language.

- The writing systems of Chinese erase most (but not all) of the distinctions between spoken Chinese languages. You'll see separate estimates of the writing population for Cantonese, Mandarin, Wu, and so on, even though you'll likely consider these all to be `zh` when written.

- CLDR doesn't have language population data for sign languages. Sign languages end up with a `speaking_population()` and `writing_population()` of 0, and I suppose that is literally true, but there's no data from which we could provide a `signing_population()` method.

[overestimates]: https://unicode-org.github.io/cldr-staging/charts/38.1/supplemental/territory_language_information.html

## Dependencies

`language_data` has a dependency on the `marisa-trie` package so that it can load a compact, efficient data structure for looking up language names.

## Installation

`language_data` is usually installed as a dependency of `langcodes`, and doesn't make much sense without it. You can `pip install language_data` anyway if you want.

To install the `language_data` package in editable mode, run `poetry install` in the package root. (This is the equivalent of `pip install -e .`, which will hopefully become compatible again soon via PEP 660.)
