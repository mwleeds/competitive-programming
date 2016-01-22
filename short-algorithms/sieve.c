#include <stdio.h>

#define N 1000

int isPrime[N];

int main(void) {
	for (int i=2; i<N; i++) {
		isPrime[i] = 1;
	}

    int np = 0;

    static int primes[1000];

	for (int i=2; i*i < N; i++) {
		if (isPrime[i]) {
			for (int j=2; j*i<N; j++) {
				isPrime[j*i] = 0;
			}
		}
	}

	for (int i=2; i<N; i++) {
        if (isPrime[i]) primes[np++] = i;
	}

	for (int i=0; i<np; i++) {
	    printf("%d\n", primes[i]);
	}

}
