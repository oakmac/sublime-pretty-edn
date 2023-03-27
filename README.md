# Sublime Pretty EDN

Pretty print, minify, and validate EDN files from within Sublime Text.

Requires [babashka] to be installed (ie: `bb`).

[babashka]:https://babashka.org/

## Usage

Commands available:

- Pretty EDN: Format
- Pretty EDN: Minify
- Pretty EDN: Validate
- Pretty EDN: to JSON minified
- Pretty EDN: to JSON pretty
- Pretty EDN: from JSON
- Pretty EDN: from JSON keywordized

## Installation

### Package Control

[Pretty EDN](https://packagecontrol.io/packages/Pretty%20EDN) is available via the [Package Control](https://packagecontrol.io/) plugin:

1. In Sublime Text, open the Command Palette by typing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>
   (<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> on Mac)
2. Type `install` and select `Package Control: Install Package`
3. A text prompt should appear shortly after Package Control loads a list of
   packages from the Internet.
4. Type `pretty edn` and press <kbd>Enter</kbd>
5. That's it! Pretty EDN is now installed.

### Linux / OSX

You can symlink this package repo to the Sublime Text Packages directory:

```
cd ~
git clone git@github.com:oakmac/sublime-pretty-edn.git
ln -s ~/sublime-pretty-edn ~/Library/Application\ Support/Sublime\ Text/Packages/
```

## TODO / Future Ideas

- setting to allow location of `bb` ([Issue #3](https://github.com/oakmac/sublime-pretty-edn/issues/3))
- add "to YAML" support ([Issue #4](https://github.com/oakmac/sublime-pretty-edn/issues/4))
- config options for spacing for formatting
- config to use fipp instead of clojure.pprint
- option to keywordize-keys / unkeywordize-keys
- Use [Tonsky's Python Clojure parser](https://github.com/tonsky/Clojure-Sublimed/blob/master/cs_parser.py) and remove dependency on babashka?

## License

[ISC License](LICENSE.md)
