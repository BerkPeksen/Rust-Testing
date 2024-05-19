#include <stdio.h>
#include <time.h>

int main() {
    clock_t start = clock();
    int count = 0;

    for (int i = 0; i < 200000000; i++) {
        count++;
    }

    clock_t end = clock();
    double elapsedMilliseconds = ((double) (end - start) * 1000) / CLOCKS_PER_SEC;
    printf("Time taken: %.3f milliseconds to count: %d\n", elapsedMilliseconds, count);

    return 0;
}
