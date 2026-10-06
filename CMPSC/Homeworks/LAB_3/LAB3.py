# LAB 3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# All functions should NOT contain any for/while loops or global variables.
# Use recursion, otherwise no credit will be given
# No helper functions allowed!

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    ## YOUR CODE STARTS HERE
    if num==1:
        return True
    if num==0 or base==1:
        return False
    if num%base==0:
        return is_power_of(base,num//base)
    else:
        return False


def cut(a_list):
    """
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
	"""
    ## YOUR CODE STARTS HERE
    if not a_list:
        return []
    if a_list[0] < 0:
        return cut(a_list[-a_list[0]:])
    return [a_list[0]] + cut(a_list[1:])
    




def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    ## YOUR CODE STARTS HERE
    if not num_list:
        return []
    if len(num_list)==1:
        return [num_list[0]]
    if num_list[-2]<num_list[-1]:
        return right_max(num_list[:-2] + [num_list[-1]]) + [num_list[-1]]
    return right_max(num_list[:-1]) + [num_list[-1]]





def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    ## YOUR CODE STARTS HERE
    if num%10==num//10%10:
        return True
    elif num<10:
        return False
    else:
        return consecutive_digits(num//10)


def only_evens(num):
    """
        >>> only_evens(4386112)
        4862
        >>> only_evens(0)
        0
        >>> only_evens(357997555531)
        0
        >>> only_evens(13847896213354889741236)
        84862488426
    """
    ## YOUR CODE STARTS HERE
    if num%10%2 == 0:
        if num<10:
            return num
        else:
            return only_evens(num//10)*10+num%10
    else:    
        return only_evens(num//10)



def run_tests():
    import doctest

    

    assert is_power_of(5, 625) is True
    assert is_power_of(4, 32) is False
    assert is_power_of(1, 1) is True
    assert is_power_of(1, 8) is False
    assert is_power_of(2, 0) is False

    assert cut([]) == []
    assert cut([-5, 1, 2]) == []
    assert cut([0, -1, 2]) == [0, 2]
    cut_input = [7, 4, -2, 1, 9]
    assert cut(cut_input) == [7, 4, 9]
    assert cut_input == [7, 4, -2, 1, 9]

    assert right_max([]) == []
    singleton = [5]
    singleton_result = right_max(singleton)
    assert singleton_result == [5]
    assert singleton_result is not singleton
    assert right_max([-2, -5, -3]) == [-2, -3, -3]
    assert right_max([2, 2, 1]) == [2, 2, 1]
    max_input = [3, 7, 2, 8, 6, 4, 5]
    assert right_max(max_input) == [8, 8, 8, 8, 6, 5, 5]
    assert max_input == [3, 7, 2, 8, 6, 4, 5]

    assert consecutive_digits(7) is False
    assert consecutive_digits(1212) is False
    assert consecutive_digits(1123) is True
    assert consecutive_digits(1233) is True
    assert consecutive_digits(1002) is True

    assert only_evens(0) == 0
    assert only_evens(13579) == 0
    assert only_evens(8) == 8
    assert only_evens(4386112) == 4862
    assert only_evens(1020304) == 2004

if __name__ == "__main__":
    run_tests()