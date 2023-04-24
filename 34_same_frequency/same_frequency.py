def freq_counter(nums):
    elements_count = {}
    for i in nums:
        elements_count[i] = elements_count.get(i, 0) + 1
    return elements_count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))


