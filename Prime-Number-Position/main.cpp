#include <iostream>
#include <stdio.h>

int primeNumber(int num) {
  
  int pos = 0;

  // get the sequence of prime numbers before num
  for(int i = 1; i < num; i++) {
    int prime = 0;

    for(int j = i-1; j > 1; j--) {
      if(i % j == 0) { // i is not a prime
        prime = 1;
        break;
      }
    }

    if(prime == 0) {
      pos++;
    }
  }

  return pos;
}

int main() {
  int N;

  std::cout << "Enter a prime number: " << std::endl;
  std::cin >> N;

  std::cout << "The position of N is: " << primeNumber(N) << std::endl;


}

