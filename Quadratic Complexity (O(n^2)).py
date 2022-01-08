def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


quadratic_algo([4, 5, 6, 8])

# In the script above, you can see that we have an outer loop that iterates through all the items in the input list
# and then a nested inner loop, which again iterates through all the items in the input list.
# The total number of steps performed is n * n, where n is the number of items in the input array. -> O(n^2)
