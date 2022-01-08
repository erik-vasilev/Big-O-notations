def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])

# The complexity of the linear_algo function is linear in the above example since the number of iterations of the
# for-loop will be equal to the size of the input items array.
# For instance, if there are 4 items in the items list, the for-loop will be executed 4 times, and so on. -> O(n)
