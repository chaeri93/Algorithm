#include <stdio.h>


int main() {
	int count;
	scanf_s("%d", &count);
	for (int i = 1; i <= count; i++) {
		printf("%d\n", i);
	}
}
