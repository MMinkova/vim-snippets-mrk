# vim-snippets-mrc
The repository contains [MARC21](https://en.wikipedia.org/wiki/MARC_standards) snippets (`.mrc` file) for vim using [snipMate](https://github.com/garbas/vim-snipmate) syntax.  
[video](https://asciinema.org/)

## Contents
The `mrc.snippets` file contains snippets for **individual MARC21 fields** and **bibliographic record templates** for common formats. Tab stops, mirrors and placeholders are used to provide cues and increase cataloguing speed.

#### Individual MARC21 fields 
- The three digit field designator code is used as trigger. 
- Include field variants to cater for the use of the same fields for different formats and purposes.
- Used to provide a flexible way of compiling bibliographic records field by field.

#### Bibliographic record templates
- Trigger glossary for each format:  
  book = `bk`  
  e-book = `ebk`  
  exhibition catalogue = `exhcat`  
  zine =`z`  
  thesis/dissertation = `thdiss`  
  DVD = `dvd`  
  CD = `cd`  
- Include a selection of MARC21 fields commonly found in each format.
- Used to increase speed when cataloguing similar resources by filling in a template.

## Dependencies
- [vim](https://www.vim.org/)
- [snipMate](https://github.com/garbas/vim-snipmate)

## Installation (without a plugin manager)
Put the `mrc.snippets` file into the snippets folder of your vim runtime directory.

- Use `:set runtimepath?` in vim to display your runtime directories
- Use `:echo $HOME` in vim to diplay your home directory
- Create directory `~/.vim/snippets` (Linux) or `~/vimfiles/snippets` (Windows)
- Put the `mrc.snippets` file in that directory

## File type detection
Vim does not automatically recognise `.mrc` files. See [`new-filetype`](http://vimdoc.sourceforge.net/htmldoc/filetype.html#new-filetype).
- Create a new ftdetect folder in your home directory `~/.vim/ftdetect` (Linux) or `~/vimfiles/ftdetect` (Windows)
- Add a .vim file containing `au BufRead,BufNewFile *.mrc		setfiletype mrc` to detect the file type without overruling the previous default file type checks.
- Restart vim to use it.

## snipMate parser
https://github.com/garbas/vim-snipmate/blob/master/doc/SnipMate.txt

## Encoding tips
- Make sure to set your vim encoding to utf-8 when writing `.mrc` files by adding `set encoding=utf-8` to your `.vimrc`file (Linux) or `_vimrc` (Windows).
- Use [`vim-digraphs`](http://vimdoc.sourceforge.net/htmldoc/digraph.html) if you are handling bibliographic records with special characters. Vim comes with default `digraphs` enabled. Check the output of `:digraphs` to verify.
- If you need more than the standard 256 characters, you need to have vim compiled with multibyte support and use a multibyte encoding in order to input the enhanced digraphs set from the `digraph-table-mbyte`. Check the output of `:echo has(‘multi-byte’)` if it returns 1 you are good to go, if not check this [blog post](http://www.miglenaminkova.com/posts/not-all-punctuation-is-made-equal/).

## Contribution
Feel free to send  me a pull request if you require more formats or field variatiosn to be included.

## License
MIT license.
