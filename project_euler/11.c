#include <stdio.h>
#include <stdlib.h>

#define N 20
#define DATA "11.data"
#define LINE_MAX 256

int matrix[N][N] = {0};

void load_matrix() {
    FILE *fp;
    if((fp = fopen(DATA, "r")) == NULL) {
        exit(1);
    }

    int i=0, k=0, num_i, line_i;
    char sep = ' ';
    char readline[LINE_MAX] = {'\0'}, num_str[3]={'\0'};
    while(fgets(readline, LINE_MAX, fp) != NULL) {
        i=0;
        line_i=0;
        while(readline[line_i]!='\0') {
            for(num_i=0; num_i<2; ++num_i) {
                num_str[num_i] = readline[line_i];
                line_i++;
            }
            matrix[i][k] = atoi(num_str);
            line_i++;
            i++;
        }
        k++;
    }
}

unsigned long max_mul() {
    unsigned long max = 0, x = 0;
    int i, k, ii;
    for(i=0; i<N; ++i) {
        for(k=0; k<N; ++k) {
            // 縦
            x = 1;
            for(ii=i+3; ii>=i && ii<N; --ii) {
                x *= matrix[ii][k];
            }
            if(x>max) max = x;
            // 横
            x = 1;
            for(ii=k+3; ii>=k && ii<N; --ii) {
                x *= matrix[i][ii];
            }
            if(x>max) max = x;
            // 斜め
            if(i+3<N && k+3<N) {
                x = 1;
                for(ii=0; ii<4; ++ii) {
                    x *= matrix[i+ii][k+ii];
                }
                if(x>max) max = x;
            }
            // 逆斜め
            if(i+3<N && k-3>=0) {
                x = 1;
                for(ii=0; ii<4; ++ii) {
                    x *= matrix[i+ii][k-ii];
                }
                if(x>max) max = x;
            }
        }
    }
    return max;
}

int main() {
    load_matrix();
    printf("%ld\n", max_mul());
    return 0;
}