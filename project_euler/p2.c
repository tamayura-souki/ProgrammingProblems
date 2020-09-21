#include <stdio.h>
#include <math.h>

int main(void) {

    int an_1 = 1, an = 2, sum = 2;
    int four_milion = 4 * pow(10, 6);
    while(an <= four_milion){
        an += an_1;
        an_1 = an - an_1;

        if(an%2 == 0){
            sum += an;
        }
    }

    printf("%d\n", sum);
    return 0;
}