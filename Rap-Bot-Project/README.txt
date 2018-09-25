downloadraps.py
-> downloads the song lyrics from azlyrics, saves in file called rap.txt
-> used by creating object with artist's name (has to match azlyrics name), then running loadLinksFromArtistPage method.
-> Example code at bottom of file.

remove_extra_lines.py
-> Cleans up downloaded raps. (Sometimes not necessary to run)
-> Because of strange html extra lines, and things.

text_manipulation.py
-> Only functions used to assist in other python files, USES nltk LIBRARY

main.py
-> Generates rap lyrics using markovify.
-> Example code to generate song is at bottom of file. (song is created when Song() object is created.)
-> USES markovify LIBRARY

- LIBRARIES NECESSARY for main.py text_manipulation.py:
- nltk
- markovify
