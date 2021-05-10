import random

# test cases: testing for partial match, no matches, complete match, and incorrect order (no matches)
a = ['ab', 'cd', 'efc', 'ab']
b = ['af', 'ee', 'efc', 'ba']

# generate the number of additional elements in a and b, max lowered to 10 to reduce runtime
elems = random.randint(1, 10)

# generate the length of each element, max lowered to 10 to reduce runtime
elem_Len = random.randint(1, 10)

# create a list of the lowercase alphabet
alphabet = list(map(chr, range(97,123)))

# create random test cases
for i in range(elems):

  # initialize wordA and wordB (the contents of the indexes of arrays a and b)
  wordA = ""
  wordB = ""
  
  # generate letters for wordA and wordB
  for j in range(elem_Len):
    n = random.randint(0,25)
    letterA = alphabet[n]
    wordA = wordA + letterA

    m = random.randint(0,25)
    letterB = alphabet[m]
    wordB = wordB + letterB

  a.append(wordA)
  b.append(wordB)

# print the column headers
print("a[i]".ljust(20), end = '')
print("b[i]".ljust(20), end = '')
print("Common".ljust(20), end = '')
print("Result".ljust(20), end = '\n')


for i in range(len(a)):
  # initialize the defaults to NO and to have the common container empty
  result = "NO"
  common = []
  
  # check if the characters at the same indexes of the a and b string match
  for j in range(len(a[i])):
    if(a[i][j] == b[i][j]):
      # if they match, mark YES and add char to set of chars
      result = "YES"
      common.append(a[i][j])
  
  # output results about a[i] and b[i] 
  print(str(a[i]).ljust(20), end = '')
  print(str(b[i]).ljust(20), end = '')
  print(str(common).ljust(20), end = '')
  print(result.ljust(20), end = '\n')
