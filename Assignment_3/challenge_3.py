# Challenge #3
# We have a nested object. We would like a function where you pass in the object and a key and
# get back the value.
# The choice of language and implementation is up to you.
# Example Inputs
# object = {“a”:{“b”:{“c”:”d”}}}
# key = a/b/c
# object = {“x”:{“y”:{“z”:”a”}}}
# key = x/y/z
# value = a
# Hints:
# We would like to see some tests.
# A quick read to help you along the way - We would expect it in any other language apart from
# elixir.


def get_value_by_key(obj, key):
    keys = key.split('/')
    val = obj
    
    for k in keys:
        val = val.get(k)
        
    return val

# Example 1
object1 = {'a': {'b': {'c': 'd'}}}
key1 = 'a/b/c'
value1 = get_value_by_key(object1, key1)
print(value1)  # Output: d

# Example 2
object2 = {'x': {'y': {'z': 'a'}}}
key2 = 'x/y/z'
value2 = get_value_by_key(object2, key2)
print(value2)  # Output: a