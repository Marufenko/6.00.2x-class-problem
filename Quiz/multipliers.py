def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    result = []
    internal_s = s
    for i in range(len(L)):
        num = internal_s // L[i]
        internal_s -= (num * L[i])
        result.append(num)

    sum_check = 0
    result_sum = 0
    for i in range(len(L)):
        sum_check += L[i]*result[i]
        result_sum += result[i]
        # print('sum_check ',sum_check)
        # print('result_sum ',result_sum)
    if sum_check == s:
        return result_sum
    else:
        return "no solution"

print(greedySum([3,2], 11))