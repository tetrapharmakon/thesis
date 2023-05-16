#!/usr/bin/env sh
all:
	latexmk -xelatex main
# grep "\[Cleanser: .*\]" main.log > Cleanings.txt
# cp main.pdf thesis-with-sissa-titlepage/
# cd thesis-with-sissa-titlepage/
# pdftk A=thesis-frn.pdf B=main.pdf cat A1 B2-r1 output main-w.pdf
# mv main.pdf tmesi.pdf

main.pdf: main.tex
	pdflatex main.tex

view:
	evince main.pdf &

clean:
	rm -f main.pdf *.aux *.log *.toc chapters/*.aux

# latexmk -c
# rm chapters/*.aux
# cp main.pdf ~/tetrapharmakon.github.io/stuff/
# cd ~/tetrapharmakon.gitub.io/
# git add -A
# git commit -m "updated phd"
# git push
# cd ~/thesis/
