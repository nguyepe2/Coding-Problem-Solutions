a = [1, 2, 3, 3, 5, 7]
b = [3, 1, 2, 1, 2, 1]

def university_career_fair(a, b):
  endtime = []
  count = 0
  end = float('-inf')

  for i in range(len(b)):
    endtime.append(int(a[i]+b[i]))
      
  # arrange invtervals to follow the format (start time, end time)
  times = zip(a, endtime)

  intervals = (list(times))

  print("the unordered intervals:")
  print(intervals)

  # sort the intervals by starting time and ending time
  intervals.sort(key = lambda t: t[1])

  print("the ordered intervals: ")
  print(intervals)

  for i in range(len(intervals)):
    # overlapping intervals checking, checks that start is greater than or equal to the previous end
    if(intervals[i][0] >= end): 

      # update the end variable 
      end = intervals[i][1]
    
    else:
      count += 1
      
  # the number of remaining intervals is the number of intervals minus the count of overlapping intervals
  print(len(intervals) - count)
  return len(intervals) - count

university_career_fair(a, b)