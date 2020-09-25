#include <stdio.h>
#include <string.h>

#define PRIME_N 10001

int primes[PRIME_N] = {0};

int main(void) {
    int n = 2, i=0;
    while(i != PRIME_N-1) {
        for(i=0; i<PRIME_N; i++) {
            if(primes[i]==0){
                primes[i] = n;
                break;
            }
            if(n%primes[i]==0) {
                break;
            }
        }
        n++;
    }

    printf("%d\n", primes[PRIME_N-1]);
    return 0;
}