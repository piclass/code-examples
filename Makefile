# Makefile for PiClass code examples
#

PACKAGE="piclass-code-examples"
DESTDIR?=
PREFIX?=/usr

DATADIR=$(DESTDIR)$(PREFIX)/share


all:

install:
	mkdir -p $(DATADIR)/piclass/code
	cp -a leds $(DATADIR)/piclass/code

uninstall:
	rm -rf $(DATADIR)/piclass/code-examples
