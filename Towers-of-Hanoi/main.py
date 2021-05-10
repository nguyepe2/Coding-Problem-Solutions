def towersOfHanoi(n, s, d, aux):

  if(n == 1):
    # move the last disk into the destination tower
    d.append(s.pop());
    print(a, b, c)


  else:
    # move every disk besides the last one into the aux tower
    towersOfHanoi(n-1, s, aux, d)
    d.append(s.pop());
    
    print(a, b, c)

    # move disks in aux to destination tower
    towersOfHanoi(n-1, aux, d, s)
 
n = int(input("How many disks should there be?: "))

# create a list from 1 .. n and reverse it
a = list(reversed(range(1,n+1)));
b =[];
c = [];

print(a, b, c)

towersOfHanoi(n, a, c, b);
