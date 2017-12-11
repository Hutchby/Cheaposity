SRC=doc.yaml
SRC+=systems/archarm/*.md
SRC+=systems/i2c/*.md
SRC+=code/devices/*.md
SRC+=code/driver/*.md
SRC+=code/httpserver/*.md

BIN=doc.pdf

all: ${BIN}


${BIN}:
	pandoc -s ${SRC} -o $@
