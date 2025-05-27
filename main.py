#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is not a valid name in python, because it doesn't begin with a letter or underscore
3. age, is a valid name in python because it begins with a letter or underscore and doesn't include special characters
4. total_amount, is a valid name in python because it begins with a letter or underscore and doesn't include special characters
5. while, is not a valid name in python because it is a command in coding
6. Student, is a valid name in python because it begins with a letter or underscore and doesn't include special characters
7. my-variable, is not a valid name in python because it includes a hyphen, should be an underscore
8. for, is not a valid name in python because it is a command in coding
9. _temp, is a valid name in python because it begins with a letter or underscore and doesn't include special characters
10. value#, is not a valid name in python because it includes a hashtag


"""
# Problem 2
"""
1. calculate_total, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
2. 3rd_function, is not a valid python function name because it doesn't begin with a letter or underscore
3. print_values, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
4. find-item, is not a valid python function name because it includes a hyphen
5. def, is not a valid python function because def is a python command
6. updateProfile, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
7. my_function, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
8. try, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
9. init_data, is a valid python function name because it begins with a letter or underscore and doesn't include special characters
10.value@function, is not a valid python function name because it includes special character '@'


"""
# Problem 3
"""
1. `True and False', evaluates to False because the 'and' operator returns False if either of its operands is False
2. `5 > 3 or "apple" < "banana"`, evaluates to True because '5 > 3' is True and the 'or' operator requires at least one operand to be True
3. `not 10 <= 20`, evaluates to False because '10 <= 20' is a True operand however the 'not' operator inverts True to False
4. `True or 5 = 4`, evaluates to True because 'True' is True and the 'or' operator requires at least one operand to be True
5. `"apple" != "orange" and 5`, evaluates to True because 'apple' is not the same as 'orange' and '5' evaluates to True as a nonzero integer
6. `3 < 5 not True`, is not a valid expression because '3 < 5' evalutes to True which makes it 'True not True'. 'not True' means False so the expression becomes 'True False'.
7. `False == (3 > 4)`, evaluates to True because '3 > 4' is False and the '==' operator means equals
8. `10 <= "10"`, is not valid because you can't compare an integer and a string
9. `True or not False`, evaluates to True because the 'or' operator requires at least one operand to be True. Additonally, 'not False' also means True
10. `5 and or 4`, is not valid because you can't compare two items using both 'and' and 'or'


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
