#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weighted_scores = 0
    total_weights = 0
    for score, weight in my_list:
        total_weighted_scores += score * weight
        total_weights += weight
    if total_weights == 0:
        return 0
    return total_weighted_scores / total_weights
