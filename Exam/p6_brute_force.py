def find_combination(choices, total):
    import itertools, numpy as np

    # creare list of all possible final combination
    list_of_all_final_combination = list(itertools.product([0,1], repeat=len(choices)))

    # calculate final sum for each combination
    tmp_dict = {}
    for i in range(len(list_of_all_final_combination)):
        sum = 0
        for j in range(len(choices)):
            sum += list_of_all_final_combination[i][j]*choices[j]
        tmp_dict[i] = (list_of_all_final_combination[i],sum)

    # sort tmp_dict desc by values
    tmp_dict_sorted = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)

    #check distance between calculated sum and total number
    pre_final_dict = {}
    for m in range(len(tmp_dict_sorted)):
        pre_final_dict[m] = (total - tmp_dict_sorted[m][1][1],tmp_dict_sorted[m][1][0])

    # let's drop items which contains sum > total number
    another_tmp_dict = {}
    for q in range(len(pre_final_dict)):
        if pre_final_dict[q][0] >= 0:
            another_tmp_dict[q] = pre_final_dict[q]

    pre_final_dict_sorted = sorted(another_tmp_dict.items(), key=lambda x: x[1])

    # create final_dict with the lowest distance to total number
    final_dict = {}
    final_dict[0] = pre_final_dict_sorted[0][1][1]
    for i in range(1,len(pre_final_dict_sorted)):
        if pre_final_dict_sorted[i][1][0] == pre_final_dict_sorted[0][1][0]:
            final_dict[i] = pre_final_dict_sorted[i][1][1]

    # calculate sum in 'array'
    almost_all = {}
    for n in range(len(final_dict)):
        sum = 0
        for k in range(len(final_dict[0])):
            sum += final_dict[n][k]
        almost_all[n] = (sum,final_dict[n])

    almost_all_sorter = sorted(almost_all.items(), key=lambda x: x[1][0])

    return np.array(almost_all_sorter[0][1][1])

print(find_combination([4, 6, 3, 5, 2], 10))
# array([1, 1, 0, 0, 0])

# print(find_combination([1, 81, 3, 102, 450, 10], 9))
# array([1, 0, 1, 0, 0, 0])