#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main() {
    int n, count;
    count = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        if (i < 100)
            count++;
        else {
            if (i / 100 - i % 100 / 10 == i % 100 / 10 - i % 100 % 10)
                count++;
        }
    }
    printf("%d", count);
}