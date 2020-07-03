#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

pthread_t tid[2];
pthread_mutex_t one;
pthread_mutex_t two;

void* f1() {
    sleep(1);
    printf("Foo!\n");
    pthread_mutex_lock(&one);
    pthread_mutex_lock(&two);
    printf("Bar!\n");
    pthread_mutex_unlock(&two);
    pthread_mutex_unlock(&one);
}

void* f2() {
    printf("Baz!\n");
    pthread_mutex_lock(&two);
    pthread_mutex_lock(&one);
    printf("Qux!\n");
    pthread_mutex_unlock(&one);
    pthread_mutex_unlock(&two);
}

int main(void) {
    pthread_mutex_init(&one, NULL); 
    pthread_mutex_init(&two, NULL); 

    pthread_create(&(tid[0]), NULL, f1, NULL);
    pthread_create(&(tid[1]), NULL, f2, NULL);

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);

    pthread_mutex_destroy(&one);
    pthread_mutex_destroy(&two);
}
