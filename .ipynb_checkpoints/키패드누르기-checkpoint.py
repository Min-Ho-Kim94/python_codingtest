# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: cook
#     language: python
#     name: cook
# ---

def solution(numbers, hand):
    answer = []
    num_cache_L = ["*"]
    num_cache_R = ["#"]
    left = [1,4,7]
    right = [3,6,9]
    both = [2,5,8,0]
    keypad = {1 : (3,0),
              2 : (3,1),
              3 : (3,2),
              4 : (2,0),
              5 : (2,1),
              6 : (2,2),
              7 : (1,0),
              8 : (1,1),
              9 : (1,2),
              "*" : (0,0),
              0 : (0,1),
              "#" : (0,2)}
    for i, v in enumerate(numbers):
        if v in left:
            answer.append("L")
            num_cache_L.append(v)
        elif v in right:
            answer.append("R")
            num_cache_R.append(v)
        else :
            dist_L = (lambda i, prev : abs((keypad[v][0] - keypad[prev][0])) + abs((keypad[v][1] - keypad[prev][1])))(i, num_cache_L[-1])
            dist_R = (lambda i, prev : abs((keypad[v][0] - keypad[prev][0])) + abs((keypad[v][1] - keypad[prev][1])))(i, num_cache_R[-1])
            if dist_L > dist_R:
                answer.append("R")
                num_cache_R.append(v)
            elif dist_L < dist_R:
                answer.append("L")
                num_cache_L.append(v)
            elif dist_L == dist_R:
                if hand == "left": 
                    answer.append("L")
                    num_cache_L.append(v)
                else: 
                    answer.append("R")
                    num_cache_R.append(v)
    answer = "".join(answer)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")

[1] > [2]
