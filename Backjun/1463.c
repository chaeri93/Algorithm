#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))  

int main() {
	int n, i, arr[1000001]; 
	scanf("%d", &n);
	arr[0] = arr[1] = 0;
	for (i = 2; i <= n; i++) {
		arr[i] = arr[i - 1] + 1;
		if (i % 2 == 0) 
			arr[i] = MIN(arr[i], arr[i / 2] + 1);
		if (i % 3 == 0) 
			arr[i] = MIN(arr[i], arr[i / 3] + 1);
	}
	printf("%d", arr[n]);
}

