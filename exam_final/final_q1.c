#include <stdio.h>

// read two integers and print all the integers which have their bottom 2 bits set.


int main(void) {
    int x, y;

    scanf("%d", &x);
    scanf("%d", &y);
    int num = x + 1;
    // PUT YOUR CODE HERE
    while (num < y) {
        if(num & 1 << 1 && num & 1 << 0) printf("%d\n", num);
        num++;
    }
    
    return 0;
}

