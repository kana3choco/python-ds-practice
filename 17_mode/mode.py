def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = 0
    val = nums[0]
    for num in nums:
        curr_most_common = nums.count(num)
        if curr_most_common > counter:
            counter = curr_most_common
            val = num
    return num

