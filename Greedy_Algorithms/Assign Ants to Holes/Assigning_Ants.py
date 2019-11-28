# View Readme for details
# @param A : List of Ant position integers
# @param H : List of Hole position integers
# @Output: an integer; indicating the time taken by the last Ant to reach it's hole (max_time)
def Assigning_Ants(A, H):
    # We sort the positions to minimize the distance between each and and a holes
    A.sort()  # Sorting Ant positions ascendingly
    H.sort()  # Sorting Hole positions ascendingly
    print("Sorted Ants: %s\nSorted Holes: %s\n" % (A, H))

    max_time = 0
    for i in range((len(A))):  # iiterating for each sorted Ant
        print("Ant pos %d to  Hole pos %d takes = (%d) moves" % (A[i], H[i], abs((A[i]) - (H[i]))))

        # getting maximum distance between the ant positions and hole positions
        if max_time < abs((A[i]) - (H[i])):
            max_time = abs((A[i]) - (H[i]))

    print("\nthe last ant takes (%d) moves to reach its hole" % max_time)
    print("\nOUTPUT = (%d) minutes" % max_time)


#######################
# Test case inputs here
# case 0 input
# ants = [1, 2, 3]
# holes = [4, 3, 2]
# expected output: (1) minute

# case 1 input
# ants = [4, -4, 2]
# holes = [4, 0, 5]
# expected output: (4) minutes

# case 2 input
ants = [-10, -79, -79, 67, 93, -85, -28, -94]
holes = [-2, 9, 69, 25, -31, 23, 50, 78]
# expected output: (102) minutes

# Runnint the actual function
Assigning_Ants(ants, holes)

# END