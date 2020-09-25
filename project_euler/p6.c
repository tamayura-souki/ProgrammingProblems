#include <stdio.h>
#include <string.h>


int main(void) {

    int sum = 0, sum2 = 0;
    int i = 0;
    for(i=1; i<=100; i++) {
        sum += i;
        sum2 += i*i;
    }
    printf("%d\n", sum*sum - sum2);
    return 0;
}