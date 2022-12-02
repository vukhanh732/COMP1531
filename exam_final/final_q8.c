#include <stdio.h>

// print the locations of a specified byte sequence in a file
// the first command line argument is a filname
// other command line arguments are integers specifying a byte sequence
// all positions the byte sequence occurs in the file are printed

int main(int argc, char *argv[]) {

    FILE *f = fopen(argv[1], "r");

    return 0;
}
