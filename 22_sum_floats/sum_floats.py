def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    float_lst = []
    for val in nums:
        if isinstance(val, float):
            float_lst.append(val)
        else:
            val = 0
            float_lst.append(val)
    return sum(float_lst)

