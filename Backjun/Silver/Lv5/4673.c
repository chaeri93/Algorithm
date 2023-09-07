#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int self_num(int i) {
    int n = i;
    while (i > 0) {
        n += i % 10 ;
        i /= 10;
    }
    return n;
}

int main() {
    int arr[10001], i, check; 
    for (i = 1; i < 10001; i++) {
        check = self_num(i);
        if (check < 10001) //���� �ѹ��� �ƴ� �� Ȯ�� 
            arr[check]=1; 
    } 
    for(i=1; i<10001; i++) { 
        if(arr[i]!=1) //���� �ѹ� �� Ȯ�� 
            printf("%d\n", i); 
    }
    return 0;
}
