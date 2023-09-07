#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int stack[100001];
int top = -1;

void push(int value) {
    stack[++top] = value;
}

void pop() {
    if (top<0)
        printf("%d\n", top);
    else
        printf("%d\n", stack[top--]); 
}

void size() {
    if (top < 0)
        printf("0\n");
    else
        printf("%d\n", top+1);
}

void empty() {
    if (top < 0)
        printf("1\n");
    else
        printf("0\n");
}

void topStack() {
    if (top < 0)
        printf("%d\n", top);
    else
        printf("%d\n", stack[top]);
}

int main() {
    int n, k;
    char order[10];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", &order);
        if (!strcmp(order, "push")) {
            int n;
            scanf("%d", &k);
            push(k);
        }
        else if (!strcmp(order, "top")) {
            topStack();
        }
        else if (!strcmp(order, "size")) {
            size();
        }
        else if (!strcmp(order, "empty")) {
            empty();
        }
        else {
            pop();
        }
    }
    return 0;
}