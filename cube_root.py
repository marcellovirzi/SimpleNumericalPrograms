__author__ = 'marcellovirzi'


def cube_root(x):
    """ Return the cube root of a perfect cube.

    Key argument:
    x -- int number
    """
    ans = 0
    while ans ** 3 < abs(x):
        ans += 1
    if ans ** 3 != abs(x):
        print(x, 'is not a perfect cube!')
    else:
        if x < 0:
            ans -= ans
        return ans