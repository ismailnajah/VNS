IF NOT EXIST bin mkdir bin
gcc -c "src/Data.c" -o "bin/Data.o" 
gcc -c "src/Neighborhood.c" -o "bin/Neighborhood.o"
gcc -c "src/main.c" -o "bin/main.o"
gcc -o "bin/main" "bin/main.o" "bin/Data.o" "bin/Neighborhood.o"