#include <iostream>
#include <stdio.h>

int primeNumber(int num) {
  
  //std::cout << num;

  int pos = 0;

  // get the sequence of prime numbers before num
  for(int i = 1; i < num; i++) {
    int prime = 0;
    //std::cout << "val of i: " << i << std::endl;

    for(int j = i-1; j > 1; j--) {
      //std::cout << "val of j: " << j << std::endl;
      //std::cout << "val of i % j: " << i % j << std::endl;
      if(i % j == 0) { // i is not a prime
        prime = 1;
        //std::cout << "Prime is FALSE, breaking... " << std::endl;
        break;
      }
    }
    //std::cout << "val of prime: " << prime << std::endl;
    if(prime == 0) {
      pos++;
      //std::cout << "val of pos: " << pos << std::endl;
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

