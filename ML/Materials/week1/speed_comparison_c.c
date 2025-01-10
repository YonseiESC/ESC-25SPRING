#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// C
double c_sum(double *arr, size_t n) {
    double total = 0;
    for (size_t i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}

int main() {
    size_t N = 100000000;
    double *data = (double *)malloc(N * sizeof(double));
    for (size_t i = 0; i < N; i++) {
        data[i] = (double)i;
    }

    // C 실행 시간 측정
    clock_t start_time = clock();
    double result = c_sum(data, N);
    clock_t end_time = clock();

    printf("C Result: %.0f\n", result);
    printf("C Execution Time: %.6f seconds\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);

    free(data);
    return 0;
}
