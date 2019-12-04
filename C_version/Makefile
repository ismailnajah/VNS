 
all: bin/ bin/main.o bin/Data.o bin/Neighborhood.o
	gcc -o "bin/main" "bin/main.o" "bin/Data.o" "bin/Neighborhood.o" -Wall

bin/ :
	[ -d bin ] || mkdir -p bin

bin/Data.o: src/Data.c
	gcc -c "src/Data.c" -o bin/Data.o 

bin/Neighborhood.o: src/Neighborhood.c
	gcc -c src/Neighborhood.c -o bin/Neighborhood.o

bin/main.o : src/main.c
	gcc -c "src/main.c" -o bin/main.o