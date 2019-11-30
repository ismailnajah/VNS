 
all: bin/ bin/main.o bin/Data.o
	gcc -o "bin/main" "bin/main.o" "bin/Data.o" -Wall

bin/ :
	[ -d bin ] || mkdir -p bin

bin/Data.o: src/Data.c
	gcc -c "src/Data.c" -o bin/Data.o 

bin/main.o : src/main.c
	gcc -c "src/main.c" -o bin/main.o