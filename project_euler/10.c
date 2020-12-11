#include <stdio.h>
#include <stdbool.h>

#define MAX 2000000

bool nonprime_flags[MAX/2+1] = {0};

unsigned long sum_primes() {
    int i, k;
    unsigned long sum=2;
    for(i=3; i<=MAX; i+=2) {
        if(nonprime_flags[i/2-1]) {
            continue;
        }
        sum += (unsigned long)i;
        for(k=i*3; k<=MAX; k+=i*2) {
            nonprime_flags[k/2-1] = true;
        }
    }
    return sum;
}

int main() {
    printf("%ld\n", sum_primes());
    return 0;
}