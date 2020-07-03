#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* strdup_eoc(const char* s) {
    int n = strlen(s);
    int m = n / 2 + (n % 2);
    printf("Length of result: %d\n", m);
    char* t = malloc(m);
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            t[i / 2] = s[i];
        }
    }
    return t; 
}

int main(void) {
    char* t = strdup_eoc("houseboy");
    printf("Result %s\n", t);
    printf("Last character %s\n", t[-1]);
}
