# vim-snippets-mrk
MARC21 bibliographic record snippets in `.mrk` format.
## Contents
The `mrk.snippets` file contains snippets for **bibliographic record templates** for common formats and **individual MARC21 fields**. Tab stops, mirrors, placeholders and nested tab stops are used to provide cues, flexibility, and increase cataloguing speed.

#### Bibliographic record templates
[![asciicast](https://asciinema.org/a/H6TMtxDwEU6J7wtm2ch8g4hVA.svg)](https://asciinema.org/a/H6TMtxDwEU6J7wtm2ch8g4hVA?autoplay=1&loop=1&speed=2)

- Trigger glossary for each format:  
  book = `bk`  
  e-book = `ebk`  
  journal = `jour`  
  electronic journal = `ejour`  
  exhibition catalogue = `exhcat`  
  zine =`z`  
  thesis/dissertation = `th`  
  DVD = `dvd`  
  CD = `cd`  
- Include a selection of MARC21 fields commonly found in each format. Multiple and additional fields can be subsequently added.
- Nested tab stops are included for `245$b` and `300$b`. These nested tab stops are removed and skipped entirely if their placeholders are edited. This allows for cases in which `245$b` and `300$b` are needed or not.
- Used to increase efficiency when cataloguing similar resources.

#### Individual MARC21 fields 
[![asciicast](https://asciinema.org/a/vGAxMV93nF6JqTw3WaUuiFcek.svg)](https://asciinema.org/a/vGAxMV93nF6JqTw3WaUuiFcek?autoplay=1&loop=1&speed=2)

- The three digit field tag is used as a trigger (eg. 245).
- Field variants are included using a combination of field tags, indicators and ordered subfield codes in order to cater for some complex fields and the use of the same field for different formats.
- Used to provide a flexible way of compiling bibliographic records field by field or supplement the bibliographic record templates.

## Dependencies
- [vim](https://www.vim.org/)
- [snipMate](https://github.com/garbas/vim-snipmate)

## Installation (without a plugin manager)
Put the `mrk.snippets` file into the snippets folder of your vim runtime directory.

- Use `:set runtimepath?` in vim to display your runtime directories
- Use `:echo $HOME` in vim to display your home directory
- Create directory `~/.vim/snippets` (Linux) or `~/vimfiles/snippets` (Windows)
- Put the `mrk.snippets` file in that directory

## File type detection
Vim does not automatically recognise `.mrk` files. See [`new-filetype`](http://vimdoc.sourceforge.net/htmldoc/filetype.html#new-filetype).
- Create a new ftdetect folder in your home directory `~/.vim/ftdetect` (Linux) or `~/vimfiles/ftdetect` (Windows)
- Add a .vim file containing `au BufRead,BufNewFile *.mrk		setfiletype krc` to detect the file type without overruling the previous default file type checks.
- Restart vim to use it.

## snipMate parser
To avoid experiencing problems with the snippets and the tab stops, set the snipMate parser to the latest version by adding the following to your `.vimrcfile` (Linux) or `_vimrc` (Windows):
```
let g:snipMate={}
let g:snipMate.snippet_version=1
```

## .mrk format
The snippets use the [MarcEdit](https://marcedit.reeset.net/downloads) mnemonic text format (also called "MARC Text File" format). This is purely out of convenience and as a way to maintain continuity for everyone already using MarcEdit. The `.mrk` format is used for display purposes only. It represents each MARC21 field in a new line using `=` as a delimiter at the start of the line, and a blank line in between different records. MARC21 field elements such as three digit field tag, indicators (x2), subfield (demarcated by `$` and for the purpose of the snippets, escaped with a backslash `\`, i.e. `\$`), subfield code, field contents and relevant punctuation follow.

## Transforming `.mrk` to `.mrc`
Use the [vim-marc plugin](https://github.com/whatupmiked/vim-marc) to transform `.mrk` snippets to `.mrc` format and back.
The plugin also includes syntax highlighting for both `.mrk` and `.mrc` formats.

## Encoding tips
- Make sure to set your vim encoding to utf-8 when writing `.mrc` files by adding `set encoding=utf-8` to your `.vimrc`file (Linux) or `_vimrc` (Windows).
- Use [`vim-digraphs`](http://vimdoc.sourceforge.net/htmldoc/digraph.html) if you are handling bibliographic records with special characters. Vim comes with default `digraphs` enabled. Check the output of `:digraphs` to verify.
- If you need more than the standard 256 characters, you need to have vim compiled with multibyte support and use a multibyte encoding in order to input the enhanced digraphs set from the `digraph-table-mbyte`. Check the output of `:echo has(‘multi-byte’)` if it returns 1 you are good to go, if not check this [blog post](http://www.miglenaminkova.com/posts/not-all-punctuation-is-made-equal/).

## Bibliographic control
Originally based on the University of the Arts London Library Services' cataloguing standards, using the following:
- [MARC21](https://www.loc.gov/marc/bibliographic/)
- [RDA](https://www.loc.gov/aba/rda/) / [RDA toolkit](https://www.rdatoolkit.org/)
- [Library of Congress authorities](https://id.loc.gov/): LCSH, LCNAF, LCGFT.
- [Library of Congress value lists for codes and controlled vocabularies](https://www.loc.gov/standards/valuelist/)
- [ISBD punctuation](https://www.ifla.org/files/assets/cataloguing/isbd/isbd_wwr_20100510_clean.pdf)
- [Koha Open Source Library System](https://koha-community.org/)

## Contribution
Feel free to send  me a pull request if you require more formats or field variations to be included.

## License
[MIT license](https://opensource.org/licenses/MIT)

