# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:05:03 2023

@author: Kiarash Rahmani
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
 
if query_name in student_marks:
        scores = student_marks[query_name]
        average_score =  sum(scores) /  len(scores)
        formatted_output = format(average_score, ".2f")
        print(formatted_output)
