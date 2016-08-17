main: main.o mylib.o
	gcc -o main main.o mylib.o

main.o: main.c mylib.h
	gcc -c -o main.o main.c

mylib.o: mylib.c mylib.h
	gcc -c -o mylib.o mylib.c
