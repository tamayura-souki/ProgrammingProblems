#include <stdio.h>
#include <string.h>

int main(void) {

    FILE *fp;
    char str[1024];
    fp = fopen("p8.data", "r");
    fgets(str, 1024, fp);
    fclose(fp);

    unsigned long int i = 0, k = 0, max = 0, n = 0;
    for(i=0; i<1000-12; i++){
        n = 1;
        for(k=0; k<13; k++){
            n *= (int)(str[i+k] - '0');
        }
        if (n > max){
            max = n;
        }
    }

    printf("%lu\n", max);
    return 0;
}