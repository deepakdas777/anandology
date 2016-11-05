"""Write a function unflatten_dict to do the reverse of flatten_dict
    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}"""


def unflatten_dict(d):
    
    result = {}
    for key in d.keys():
        if "." in key:
            parent, child = key.split(".", 1)
            if parent in result.keys():
                result[parent].update(unflatten_dict({child:d[key]}))
            else:
                result.update({parent: unflatten_dict({child:d[key]})})
        else:
            result.update({key:d[key]})
    return result
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
