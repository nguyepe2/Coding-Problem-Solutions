
# get the number of people
n = int(input("How many people are there?\n"))


# get the factorial of a number
def getFactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial


# if there are an odd number of people, no teams can be formed
if (n % 2 != 0):
    print("0 teams could be formed")

# if there are an even number of people calculate the number of teams that can be formed using the binomial coefficient formula:
# n!/(k!(n-k)!)
# where n is the number of people and k is 2 because we're splitting people into pairs. In addition, the result of the formula is divided by 2 again because the order of the pairing doesn't matter
else:
    print(
        str(int(getFactorial(n) /
                (getFactorial(2) * getFactorial(n - 2)) / 2)) +
        " teams could be formed")
