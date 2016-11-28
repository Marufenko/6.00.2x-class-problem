def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    sumList = []
    for i in range(len(L)):
        for j in range(i, len(L)):
            sumList.append(sum(L[i:j + 1]))

    return max(sumList)

print(max_contig_sum([2,3,-7,8,-9,2,2,2,2,2,-2]))