
/* This is a pretty efficient algorithm for finding prime numbers under n
 * called the Sieve of Eratosthenes. The result is a boolean array.
 */

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define N 1000000
typedef unsigned int uint;

int main() {

    bool isPrime[N];
	for (uint i=2; i<N; ++i) {
		isPrime[i] = true;
	}

    uint sqrt_N = (uint)sqrt((double) N);
	for (uint i = 2; i < sqrt_N; ++i) {
		if (isPrime[i]) {
			for (uint j = 2; j*i < N; ++j) {
				isPrime[j*i] = false;
			}
		}
	}
    
    uint num_primes = 0;
	for (uint i = 2; i < N; ++i) {
        if (isPrime[i]) num_primes++;
	}

    printf("found %d primes below %d\n", num_primes, N);
    
    return 0;
}
