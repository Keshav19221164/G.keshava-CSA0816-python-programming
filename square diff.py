import math
 
def square_diff(n):
    sum_of_squares = 0
    sum_ = 0
    for i in range(1, n+1):
        sum_of_squares += math.pow(i, 2)
        sum_ += i
    square_of_sum = math.pow(sum_, 2)
    abs_difference = abs(sum_of_squares - square_of_sum)
    return int(abs_difference)
n = 100
print(square_diff (n) )
