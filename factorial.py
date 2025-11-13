def factorial(num):
	# we want to start a count up multipying each number to n, n! ex 6! = nx6x5x4x3x2x1
    # this can look like 1x2x3x4x5x6xn just the same as nx6x5x4x3x2x1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
    