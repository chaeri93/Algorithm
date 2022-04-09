#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>


int main() {
    int count;
    char word[100];
    scanf("%s", word);
    count = strlen(word);
    for (int j = 0; j < strlen(word); j++) {
        if ((word[j] == 'l' || word[j] == 'n') && word[j + 1] == 'j')
            count--;
        if (word[j] == 'd' && word[j + 1] == 'z' && word[j + 2] == '=')
            count--;
        if (word[j] == '=' || word[j] == '-')
            count--;
    }
    printf("%d", count);
    return 0;
}
