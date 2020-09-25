#include <stdio.h>
#include <string.h>


int main(void) {

    int x = 2520 * 11 * 13 * 17 * 19;
    if (x % 16 != 0) x *= 2;
    printf("%d\n", x);
    return 0;
}