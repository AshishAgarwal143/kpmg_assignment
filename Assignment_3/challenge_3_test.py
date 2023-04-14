from challenge_3 import *
def test_get_value_by_key():
    # Example 1
    object1 = {'a': {'b': {'c': 'd'}}}
    key1 = 'a/b/c'
    assert get_value_by_key(object1, key1) == 'd'

    # Example 2
    object2 = {'x': {'y': {'z': 'a'}}}
    key2 = 'x/y/z'
    assert get_value_by_key(object2, key2) == 'a'

    # Test invalid key
    assert get_value_by_key(object1, 'a/b/f') is None

    # Test empty key
    assert get_value_by_key(object2, '') is None