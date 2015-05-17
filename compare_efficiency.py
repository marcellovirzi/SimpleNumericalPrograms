__author__ = 'marcellovirzi'

# The program compares the results of three search
# methods of approximation of the square root
# (in terms number of iterations).
#
# The methods are:
# 1) exhaustive enumeration
# 2) bisection search
# 3) newton - raphson method



def root_exhaustive_enum(x, power, epsilon=0.01):
    """ Return an approximation of the power root of any nonnegative number x.

    Optional argument epsilon is the approximation of the answer (default 0.1).
    """
    step = epsilon ** 2
    num_guesses = 0
    ans = 0.0
    while abs(ans ** power - x) >= epsilon and ans <= x:
        ans += step
        num_guesses += 1
    if abs(ans ** power - x) >= epsilon:
        print("failed on square root of ", x)
    else:
        print('root_exhaustive_enum result: ', ans, ', iterations: ', num_guesses)


def root_bis_search(x, power, epsilon=0.01):
    """ Return an approximation of the power root of any nonnegative number x.

    Optional argument epsilon is the approximation of the answer (default 0.1).
    """
    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0

    while abs(ans ** power - x) >= epsilon:
        num_guesses += 1
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0

    print('root_bis_search result: ', ans, ', iterations: ', num_guesses)


def root_newton_raphson(x, power, epsilon=0.01):
    """ Return an approximation of the power root of any nonnegative number x.

    Optional argument epsilon is the approximation of the answer (default 0.1).
    """
    k = x
    guess = k / float(power)
    num_guesses = 0
    while abs(guess * guess - k) >= epsilon:
        num_guesses += 1
        guess = guess - (((guess ** power) - k) / (power * guess))

    print('root_newton_raphson result: ', guess, ', iterations: ', num_guesses)

x = 10000
power = 2

root_exhaustive_enum(x, power)
root_bis_search(x, power)
root_newton_raphson(x, power)

# Results:
#
# root_exhaustive_enum result:  100.00000000219612 , iterations : 1000000
# root_bis_search result:  99.99997913837433 , iterations:  26
# root_newton_raphson result:  100.00000025438577 , iterations:  9
