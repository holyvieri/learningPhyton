import sys


def find_marbles(): #The code defines a function find_marbles()
    # that will find the marbles based on the given inputs and perform queries.
    test_case_number = 1 #The variable test_case_number is initialized to 1, which represents the current test case number.

    while True:
        # Read N and Q
        N, Q = map(int, sys.stdin.readline().split())
        # These represent the number of marbles and the number of queries for the current test case.
        # Check for termination
        if N == 0 and Q == 0: #If both N and Q are 0, it means it is the termination case, and the loop is broken using break.
            break

        # Read the marbles
        marbles = []
        #Otherwise, it proceeds to read the marbles using a loop. It reads N lines from the standard input,
        # converts them to integers using int(sys.stdin.readline()), and appends them to the marbles list.
        for _ in range(N):
            marbles.append(int(sys.stdin.readline()))

        # Process the queries
        marbles.sort() #The marbles list is then sorted using marbles.sort() to ensure efficient searching later on.
        sys.stdout.write(f"CASE# {test_case_number}:\n") #The code writes the current test case number to the standard
        # output using sys.stdout.write().
        for _ in range(Q): #Next, it enters a loop to process the queries. It reads Q lines from the standard input,
            # converts them to integers, and assigns them to the variable query
            query = int(sys.stdin.readline())
            position = binary_search(marbles, query) #t calls the binary_search() function, passing the marbles list
            # and the query as arguments. This function will perform a binary search on the sorted marbles list
            # to find the position of the query.

            if position != -1:
                sys.stdout.write(f"{query} found at {position + 1}\n")
            else:
                sys.stdout.write(f"{query} not found\n")

        test_case_number += 1


def binary_search(arr, target): #The binary_search() function takes an array arr and a target value target as input.
    # It initializes the left and right pointers to the start and end indices of the array, respectively.
    left = 0
    right = len(arr) - 1
    #It enters a loop where it calculates the mid index as the average of left and right.
    while left <= right:
        mid = (left + right) // 2
    #If the value at arr[mid] is equal to the target, it calls the find_first_occurrence() function to find the first
        # occurrence of the target in the array. It passes the arr, target, left, and mid as arguments.
        if arr[mid] == target:
            return find_first_occurrence(arr, target, left, mid)
        elif arr[mid] < target:  #If the value at arr[mid] is less than the target, it updates the left pointer to
            # mid + 1 to search in the right half of the array.
            left = mid + 1
        else:
            #If the value at arr[mid] is greater than the target, it updates the right pointer to mid - 1 to search
            # in the left half of the array.
            right = mid - 1

    return -1 #If the loop completes without finding the target,
    # it returns -1 to indicate that the target is not found in the array.

#The find_first_occurrence() function takes an array arr, a target value target,
# and the left and right indices representing the search range.
def find_first_occurrence(arr, target, left, right):
    position = -1 #It initializes the position variable to -1 to keep track of the first occurrence of the target.

    while left <= right: #It enters a loop where it calculates the mid index as the average of left and right.
        mid = (left + right) // 2

        if arr[mid] == target: #If the value at arr[mid] is equal to the target, it updates the position variable
            # to mid and continues searching in the left half by updating the right pointer to mid - 1.
            position = mid
            right = mid - 1
        else:
            left = mid + 1 ##If the value at arr[mid] is not equal to the target,
            # it updates the left pointer to mid + 1 to search in the right half.

    return position 


# Run the function to find marbles
find_marbles()
