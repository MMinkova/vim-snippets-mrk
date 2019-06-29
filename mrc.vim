"comment out line 3, 9, 12, 15, 22
"syn region indicator matchgroup=fieldTag start=/=\d\{3}/ matchgroup=subfield end=/\$\w/
syn match field /=\(\d\{3}\)\@=/
hi link field Delimiter

syn match LDR /=LDR.*/
hi link LDR WildMenu

syn match fieldTag /\(=\)\@<=\d\{3}/
hi link fieldTag Tag

syn match subfield /\$\w/
hi link subfield Structure

" used % as delimiter to match /
syn match subPunct %\(:\|;\|,\|=\|/\)\(\$\w\)\@=%
hi link subPunct Structure

syn match endPunct /\.$/
hi link endPunct Number

syn match indicator /\(=\d\{3}\s\+\)\@<=\(\d\|\\\)\+/
hi link indicator Number
