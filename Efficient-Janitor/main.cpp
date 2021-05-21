#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <time.h>


// function to display the contents of the vector
void displayVector(std::vector<float> &vect) {
  std::cout << "[ ";
  for(int i = 0; i < vect.size(); i++) {
    std::cout << vect.at(i) << " ";
  }
  std::cout << "]";
  std::cout << std::endl;
}

// function to calculate the number of trips for the janitor
int getTrips(std::vector<float> &vect, int n) {
  
  // sort the array from lightest bags to heaviest bags
  std::sort(vect.begin(), vect.begin()+n);

  displayVector(vect);
  
  // initialize number of trips
  int trips = 0;

  // initialize current weight
  float currWeight = 0;

  while(vect.size() > 0) {
    int i = 0;

    // initialize k variable to grab heaviest bag
    int k = vect.size()-1;

      // always grab the heaviest bag
      currWeight = vect.at(k);
      std::cout << "grabbing heaviest bag... " << std::endl;
      std::cout << "current weight: " << currWeight << std::endl;
     
      // if k + i > 3, just remove k, or just remove the last bag if there's only one bag left
      if(currWeight + vect.at(i) > 3 || vect.size() == 1) {
        
        // remove the heaviest bag
        vect.erase(vect.begin()+k);
        std::cout << "removing heaviest bag... \n" << std::endl;

        displayVector(vect);
      
        trips++;
      }

      else{

        // set the current weight to the heaviest bag plus the lightest bag
        currWeight = currWeight + vect.at(i);

        // because you can have at most two bags, throw them both away
        vect.erase(vect.begin()+k);
        vect.erase(vect.begin()+i);
        std::cout << "grabbing additional bag... " << std::endl;
        std::cout << "current weight: " << currWeight << std::endl;
        std::cout << "throwing away bags...\n" << std::endl;
        trips++;
        displayVector(vect);
        

      }
      i++;
  }

  return trips;
}


int main() {
  
  // initialize random seed: 
  srand (time(NULL));

  // generate  number between 1 and 1000: 
  int n = rand() % 1000 + 1;

  float weight[n];

  for(int i=0; i < n; i++) {
    // generate random number between 1.01 and 3
    weight[i] = (rand() % 200 + 101) / float(100);
  }

  // move contents to a vector to get some practice with vectors and to make it easier to remove elements and resize when necessary

  // initialize the vector from the array
  std::vector<float> vect(weight, weight+n);

  int trips;

  trips = getTrips(vect, n);
  std::cout << "Number of trips: " << trips << std::endl;
  std::cout << "n was: " << n << std::endl;
}