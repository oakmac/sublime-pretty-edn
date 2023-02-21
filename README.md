# Sublime Text EDN

Pretty print, minify, and validate EDN files from within Sublime Text.

Requires [babashka] to be installed (ie: `bb`).

[babashka]:https://babashka.org/

## Usage

FIXME: write this section

Commands available:

- Pretty EDN: Format
- Pretty EDN: Minify
- Pretty EDN: Validate

## Installation

### Package Control

FIXME: upload to Package Control and write this section

### Linux / OSX

You can symlink this package repo to the Sublime Text Packages directory:

```
cd ~
git clone git@github.com:oakmac/sublime-text-edn.git
ln -s ~/sublime-text-edn ~/Library/Application\ Support/Sublime\ Text/Packages/
```

## TODO / Future Ideas

- setting to allow location of `bb`
- config options for spacing for formatting
- config to use fipp instead of clojure.pprint
- to JSON
- to YAML
- keywordize-keys / unkeywordize-keys
- Use [Tonsky's Python Clojure parser](https://github.com/tonsky/Clojure-Sublimed/blob/master/cs_parser.py) and remove dependnecy on babashka

## License

[ISC License](LICENSE.md)
