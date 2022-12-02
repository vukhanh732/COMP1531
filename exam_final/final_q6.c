#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// print a specified byte from a file
//
// first command line argument specifies a file
// second command line argument specifies a byte location
//
// output is a single line containing only the byte's value
// printed as a unsigned decimal integer (0..255)
// if the location does not exist in the file
// a single line is printed saying: error

int main(int argc, char *argv[]) {

    if (argc != 3) {
        exit(1);
    }
    FILE *f = fopen(argv[1], "r");
    int off_set = atoi(argv[2]);

    if (off_set >= 0) {
        fseek(f, off_set, SEEK_CUR);
        int byte = fgetc(f);
        printf("%d\n", byte);
    } else {
        fseek(f, off_set, SEEK_END);
        int byte = fgetc(f);
        printf("%d\n", byte);
    }


    return 0;
}
