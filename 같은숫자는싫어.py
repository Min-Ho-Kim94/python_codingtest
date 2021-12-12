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

def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if i == 0:
            answer.append(v)
        elif v != arr[(i-1)]:
            answer.append(v)
    return answer
