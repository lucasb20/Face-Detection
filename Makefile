CC = g++
CFLAGS = -Wall -Wextra
TARGET = docscan.bin
LDFLAGS = -lm

all: $(TARGET)

$(TARGET): main.o
	$(CC) $(CFLAGS) main.o -o $(TARGET) $(LDFLAGS)

main.o: main.cpp
	$(CC) -c main.cpp

clean:
	rm -f *.o $(TARGET)