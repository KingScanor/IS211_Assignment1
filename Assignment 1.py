# Part 1 Functions and Exceptions

def list_divide (numbers, divide = 2):
    dcount = 0
    for eNum in numbers:
        if eNum % divide == 0:
            dcount += 1
    return dcount

class ListDivideException (Exception):
    pass

def test_list_divide():
    try:
        if not list_divide([1,2,3,4,5]) == 2:
            raise ListDivideException
        if not list_divide([2,4,6,8,10]) == 5:
            raise ListDivideException
        if not list_divide([30, 54, 63,98, 100], divide=10) == 2:
            raise ListDivideException
        if not list_divide([]) == 0:
            raise ListDivideException
        if not list_divide([1,2,3,4,5], 1) == 5:
            raise ListDivideException
        print ("All Test Passed")
    except ListDivideException:
        print ("Division Exception Appeared")
        testListDivide()
