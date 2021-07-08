# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(X, Y):
    # containers to store the fraction value and the amount of times it occurs, respectively
    fractions = []
    count = {}

    for i in range(len(X)):
        # if we haven't seen the fraction before, add it to the list of seen fractions and increment its count
        if X[i]/Y[i] not in fractions:
            fractions.append(X[i]/Y[i])
            count[str(X[i]/Y[i])] = 1

        else:
            # if we have seen the fraction before, just increment its count
            count[str(X[i]/Y[i])] += 1

    # get the number of times the most common fraction appeared
    frequency = max(count.values())

    # get the most common fraction
    for key, value in count.items():
        if frequency == value:
            print(f"The most common fraction value was {key} and it appeared {frequency} times")
            return frequency


X = [1, 2, 3, 1, 2]
Y = [2, 4, 6, 5, 10]
if __name__ == '__main__':
    solution(X, Y)

