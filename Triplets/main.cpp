#include <iostream>
#include <algorithm>

int getCount(int arr[], int n, int t) {
  //sort the array
  std::sort(arr, arr+n);

  //initialize count
  int count = 0;

  for(int i=0; i<n-2; i++) {
    //initialize j and k so that the array is shaped like
    // [i, j, _, _, k]
    int j = i+1;
    int k = n-1;

    //make sure that j and k don't cross each other
    while(j < k){

      // if the sum of the triplet is too big, reduce k
      if(arr[i] + arr[j] + arr[k] > t) {
        k--;
      }

      else{
        // if arr[i] + arr[j] + arr[k] works, arr[k] = arr[k-1 .. j+1] should work as well 
        count += k-j;
        j++;
      }
    }
  }
  
  return count;
  
}

int main() {
  // the default test case
  int arr[] = {1,2,3,4,5};

  // the number of elements in the array
  int n = sizeof(arr)/sizeof(arr[0]);

  // the integer threshold
  int t = 8;

  std::cout << getCount(arr, n, t) << std::endl; 
}