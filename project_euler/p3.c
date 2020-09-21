#include <stdio.h>

int main(void) {

    long long int i=0, n=600851475143;
    for(i=1; i<n; i+=2){
        if(n%i==0){
            n /= i;
        }
    }

    printf("%d\n", n);
    return 0;
}