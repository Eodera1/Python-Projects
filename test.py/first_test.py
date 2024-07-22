from typing import List

def solution(wood: List [int]) -> int:
    # Write Your solution here
    return 0

# README
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed
if __name__ == __main__:
    print(solution([1, 2, 3, 4, 5])) # Expected output: 3
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Expected output: 9
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # Expected output: 19 
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) # Expected output: 29
    line = input()
    k = [int(i) for i in line.strip().split()]
    print(solution(k))