#include <stdio.h>
#include <string.h>

void reverse(char *s){
    int l = strlen(s);
    int i = 0;
    char c;
    for(i=0; i<l/2; i++){
        c = s[i];
        s[i] = s[l-i-1];
        s[l-i-1] = c;
    }
}

int isPalindrome(int num){
    if(num%10 == 0) return 0;
    char s1[10], s2[10];
    sprintf(s1, "%d", num);
    strcpy(s2, s1);
    reverse(s2);
    return strcmp(s1, s2) == 0;
}

int main(void) {

    int i = 0, k = 0, max=0, n = 0;
    for(i=0; i<1000; i++){
        for(k=0; k<1000; k++){
            n = i*k;
            if(isPalindrome(n)==1 && n > max){
                max = n;
            }
        }
    }

    printf("%d\n", max);
    return 0;
}