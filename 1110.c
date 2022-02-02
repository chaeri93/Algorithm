#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main() {
    int n, cycle, check, k;
    char name[51][51], output[51];
    scanf("%d", &n);
    if (n < 10)
        n *= 10;
    cycle = 0;
    check = n;
    while (1) {
        n = (n / 10 + n % 10) % 10 + n % 10 * 10;
        cycle++;
        if (n == check)
            break;
    }
    printf("%d", cycle);
}
