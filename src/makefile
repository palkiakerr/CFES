#Change application output name here. Be careful to always update this!
TARGET=CFES

#compiler
CC=gcc

DEBUG=
OPT=-O2
WARN=
PTHREAD=

CCFLAGS=$(DEBUG) $(OPT) $(WARN) $(PTHREAD)
LDLIBS= -lgsl -lgslcblas -lm
GTKLIB=`pkg-config --cflags --libs gtk+-3.0`

#linker
LD=gcc
LDFLAGS=$(PTHREAD) $(LDLIBS) $(GTKLIB) -export-dynamic
OUTPUT=schematic.png
OBJS=main.o

all: $(OBJS)
	$(LD) -o $(TARGET) $(OBJS) $(LDFLAGS)

main.o: combined.c
	$(CC) -c $(CCFLAGS) combined.c $(GTKLIB) -o main.o

clean:
	rm -f *.o $(OUTPUT)

