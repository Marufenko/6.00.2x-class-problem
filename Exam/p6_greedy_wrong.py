def find_combination(choices, total):
    import numpy as np
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """

    # create input dict with indexes of input list
    input_dict = {}
    for i in range(len(choices)):
        input_dict[i] = choices[i]

    # sort input dict by values
    input_dict_sorted = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)

    # calculate coeficients
    total_var = total
    tmp_result_dict = {}
    for j in range(len(input_dict_sorted)):
        if input_dict_sorted[j][1] <= total_var:
            tmp_result_dict[j] = (1,input_dict_sorted[j][0],input_dict_sorted[j][1]) # 1-multiplier, 2-index, 3-value
            total_var = total_var - input_dict_sorted[j][1]
        else:
            tmp_result_dict[j] = (0,input_dict_sorted[j][0],input_dict_sorted[j][1]) # 1-multiplier, 2-index, 3-value

    # sort tmp_result_dict by input indexes
    tmp_result_dict_sorted = sorted(tmp_result_dict.items(), key=lambda x: x[1][1])

    # create final_list
    final_list = []
    for k in range(len(tmp_result_dict_sorted)):
        final_list.append(tmp_result_dict_sorted[k][1][0])

    return np.array(final_list)

print(find_combination([1], 10))