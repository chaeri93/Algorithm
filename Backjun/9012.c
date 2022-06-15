#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main() {
    int n, cycle, check, k;
    char brack[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", brack);
        int count = 0;
        for (int j = 0; j < strlen(brack); j++) {
            if (brack[j] == '(')
                count++;
            else
                count--;
            if (count < 0) {
                printf("NO\n");
                break;
            }
        }
        if (count==0)
            printf("YES\n");
        else if (count>0)
            printf("NO\n");
    }
    return 0;
}
