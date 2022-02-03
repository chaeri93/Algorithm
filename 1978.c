#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main() {
    int n, count, k, flag;
    scanf("%d", &n);
    count = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &k);
        flag = 0;
        if (k == 1)
            continue;
        
        for (int j = 2; j < k; j++) {
            if (k % j == 0)
                flag = 1;
        }
        if (flag == 0)
            count++;
    }
    printf("%d", count);
    return 0;
}