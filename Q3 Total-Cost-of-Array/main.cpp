#include <iostream>
#include <ctime>

int main() {

  // set the seed
  srand( (unsigned)time( NULL ) );

  // The array can have anywhere between 1 and 25 elements
  int N = rand() % 25 + 1;

  int array[N];

  // Populate the array with random numbers between 1 and 1000
  for(int i=0; i < N; i++) {
    array[i] = rand() % 1000 + 1;
    std::cout << array[i] << std::endl;
  }


  int sum = 0;

  for(int i=0; i<N; i++) {
    sum += array[i] * (i + 1); 
  }

  std::cout << "sum is: " << sum << std::endl;
}