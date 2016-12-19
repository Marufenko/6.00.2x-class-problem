def find_combination(choices, total):
    import numpy as np

    """
    Write a function that meets the specifications below. You do not have to use dynamic programming.

    Hint: You might want to use bin() on an int to get a string, get rid of the first two characters, add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

    For example,

    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
    More specifically, write a function that meets the specifications below:

    def find_combination(choices, total):
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

    Paste your entire function (including the definition) in the box. Note: If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.
    """

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