#include <stdlib.h>
#include <stdint.h>

// given 2 uint32_t values
// return the number of bits which are set (1) in both values

int final_q5(uint32_t value1, uint32_t value2) {
    int count = 0;
    uint32_t n = value1 & value2;

    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count; 
}
