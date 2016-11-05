""" function treemap to map a function over nested list
    >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5] ] ])
    [1, 4, [9, 16, [25]]]"""

def treemap(fun, list_of_args):
    result = []
    for arg in list_of_args:
        if isinstance(arg, list):
            result.append(treemap(fun, arg))
        else:
            result.append(fun(arg))
    return result
print treemap(lambda x: x*x*x, [1, 2, [3, 4, [5]]])
