# Sublime Text EDN

Pretty print, validate, and minify EDN files from within Sublime Text.

## How it works

- Require babashka installed
- Shell out to nodejs
- Use Tonsky's Python Clojure parser from Python directly?

## Installation

### Package Control

If you have [Package Control] installed, you can easily install the
[Parinfer](https://packagecontrol.io/packages/Parinfer) package:

1. In Sublime Text, open the Command Palette by typing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>
   (<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> on Mac)
2. Type `install` and select `Package Control: Install Package`
3. A text prompt should appear shortly after Package Control loads a list of
   packages from the Internet.
4. Type `parinfer` and press <kbd>Enter</kbd>
5. That's it! Parinfer is now installed.

### Linux / OSX

You can symlink the the parinfer repo to the Sublime Text Packages directory.

```
cd ~
git clone git@github.com:oakmac/sublime-text-parinfer.git
ln -s ~/sublime-text-parinfer ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Parinfer
```

## Development

```sh

```

## License

[ISC License](LICENSE.md)