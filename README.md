# language_data: a supplement to [langcodes][]

[langcodes]: https://github.com/LuminosoInsight/langcodes

This package is not meant to be used on its own. Please see [langcodes][] for documentation.

The purpose of the `language_data` package is to include bulky data that isn't needed for some use cases of langcodes, so that `langcodes` itself can operate without this data or its dependencies.

The functions and test cases for working with this data are in [langcodes][], because working with the data correctly requires parsing language codes.

## Data

The data included in this package is:

- The names of various languages, in various languages
- The estimated population that speaks each language
- The estimated population that writes each language

These are all extracted from the Unicode [CLDR][] data package, version 38.1, plus a few additional language names that fill in gaps in CLDR.

[cldr]: http://cldr.unicode.org/

## Caveats

- The estimates for "writing population" are often overestimates, as described in the [CLDR documentation on territory data][overestimates]. In most cases, they are derived from published data about literacy rates in the places where those languages are spoken. This doesn't take into account that many literate people around the world speak a language that isn't typically written, and write in a _different_ language.

- The writing systems of Chinese erase most (but not all) of the distinctions between spoken Chinese languages. You'll see separate estimates of the writing population for Cantonese, Mandarin, Wu, and so on, even though you'll likely consider these all to be `zh` when written.

- CLDR doesn't have language population data for sign languages.

[overestimates]: https://unicode-org.github.io/cldr-staging/charts/38.1/supplemental/territory_language_information.html

## Dependencies

`language_data` has a dependency on the `marisa-trie` package so that it can load a compact, efficient data structure for looking up language names.

## Changelog

### Version 1.0.1

* Changed dependency from the fork `marisa-trie-m` to the original `marisa-trie`, which is now more up to date
* Copied the `nb` name data to `no` so that Norwegian data is available under both names. CLDR (and therefore langcodes) changed their mind on which one was the normalized language code.

### Version 1.0

Original release that factored out `language_data` from `langcodes`.
