#include <stdio.h>
#include <string.h>

unsigned long f(){
    unsigned long a = 0, b = 0, c = 0;
    for(a=1; a<1000; a++){
        for(b=1; b<1000-a; b++){
            c = 1000 - b - a;
            if(c*c == a*a + b*b){
                return a*b*c;
            }
        }
    }
    return 1;
}

int main(void) {
    printf("%lu\n", f());
    return 0;
}