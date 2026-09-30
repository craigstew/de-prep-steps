import os
import sys

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

# Task 1
def create_tuple(arg_1, arg_2):
    return (arg_1, arg_2)


@run_test
def test_create_tuple():
    assert create_tuple(1, 2) == (1, 2), \
        format_err_msg((1, 2), create_tuple(1, 2))

    assert create_tuple('a', 'b') == ('a', 'b'), \
        format_err_msg(('a', 'b'), create_tuple('a', 'b'))

    assert create_tuple([1, 2, 3], [4, 5, 6]) == ([1, 2, 3], [4, 5, 6]), \
        format_err_msg(([1, 2, 3], [4, 5, 6]),
                       create_tuple([1, 2, 3], [4, 5, 6]))


# Task 2
def tuple_to_list(my_tuple):
    return list(my_tuple)


@run_test
def test_tuple_to_list():
    assert tuple_to_list(("Alex", "Windows")) == ["Alex", "Windows"], \
        format_err_msg(["Alex", "Windows"], tuple_to_list(("Alex", "Windows")))

    assert tuple_to_list(("Danika", "Linux")) == ["Danika", "Linux"], \
        format_err_msg(["Danika", "Linux"], tuple_to_list(("Danika", "Linux")))

    assert tuple_to_list(("Simon", "Mac")) == ["Simon", "Mac"], \
        format_err_msg(["Simon", "Mac"], tuple_to_list(("Simon", "Mac")))


#  Task 3
def count_threes(my_tuple):
    return my_tuple.count('three')


@run_test
def test_count_threes():
    assert count_threes((1, 2, 3, 4, 5)) == 0, \
        format_err_msg(0, count_threes((1, 2, 3, 4, 5)))

    assert count_threes(("three", "one", "three", "two", "three",)) == 3, \
        format_err_msg(3, count_threes(
            ("three", "one", "three", "two", "three",)))

    assert count_threes(("one", 1, "two", 2, "three", 3)) == 1, \
        format_err_msg(1, count_threes(("one", 1, "two", 2, "three", 3)))


# Task 4
def get_index_of_five(my_tuple):
    return my_tuple.index(5)


@run_test
def test_get_index_of_five():
    assert get_index_of_five((1, 6, 5, 2, 5)) == 2, \
        format_err_msg(2, get_index_of_five((1, 6, 5, 2, 5)))

    assert get_index_of_five(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == 3, \
        format_err_msg(3, get_index_of_five(
            ("ooh", 78, "strings", 5, "and", "numbers", 4)))


# Task 5
def get_second_to_last_element(my_tuple):
    return my_tuple[-2]


@run_test
def test_get_second_to_last_element():
    assert get_second_to_last_element((1, 6, 5, 2, 5)) == 2, \
        format_err_msg(2, get_second_to_last_element((1, 6, 5, 2, 5)))

    assert get_second_to_last_element(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) == "numbers", \
        format_err_msg("numbers", get_second_to_last_element(
            ("ooh", 78, "strings", 5, "and", "numbers", 4)))

    assert get_second_to_last_element(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) == "before", \
        format_err_msg("before", get_second_to_last_element(
            ("Wait", "I've", "seen", "this", "before", "somewhere")))


# Task 6
def get_last_three_elements(my_tuple):
    return my_tuple[-3:]


@run_test
def test_get_last_three_elements():
    assert get_last_three_elements((1, 6, 5, 2, 5)) == (5, 2, 5), \
        format_err_msg((5, 2, 5), get_last_three_elements((1, 6, 5, 2, 5)))

    assert get_last_three_elements(
        ("ooh", 78, "strings", 5, "and", "numbers", 4)) \
        == ("and", "numbers", 4), \
        format_err_msg(("and", "numbers", 4), get_last_three_elements(
            ("ooh", 78, "strings", 5, "and", "numbers", 4)))

    assert get_last_three_elements(
        ("Wait", "I've", "seen", "this", "before", "somewhere")) \
        == ("this", "before", "somewhere"), \
        format_err_msg(
            ("this", "before", "somewhere"),
            get_last_three_elements(
                ("Wait", "I've", "seen", "this", "before", "somewhere")))


# Task 7
def check_element_is_present(my_tuple, element):
    return True if element in my_tuple else False


@run_test
def test_check_element_is_present():
    assert check_element_is_present((1, 6, 5, 2, 5), 6) is True, \
        format_err_msg(True,
                       check_element_is_present((1, 6, 5, 2, 5), 6))

    assert check_element_is_present(
        ("ooh", 78, "strings", 5, "and", "numbers", 4), "Joe is cool") \
        is False, \
        format_err_msg(
            False,
            check_element_is_present(
                ("ooh", 78, "strings", 5, "and", "numbers", 4),
                "Joe is cool"))

    assert check_element_is_present((44, 63, 14, 23, 4, 81), 89) is False, \
        format_err_msg(
            False, check_element_is_present((44, 63, 14, 23, 4, 81), 89))

    assert check_element_is_present(
        ("Wait", "I've", "seen", "this", "before", "somewhere"),
        "Wait") is True, \
        format_err_msg(True, check_element_is_present(
            ("Wait", "I've", "seen", "this", "before", "somewhere"),
            "Wait"))


# Task 8
def tuple_switcheroo(*args):
    return args[::-1]


@run_test
def test_tuple_switcheroo():
    assert tuple_switcheroo(3, 4) == (4, 3), \
        format_err_msg((4, 3), tuple_switcheroo(3, 4))

    assert tuple_switcheroo(5, 4, 3, 2, 1) == (1, 2, 3, 4, 5), \
        format_err_msg((1, 2, 3, 4, 5), tuple_switcheroo(5, 4, 3, 2, 1))

    assert tuple_switcheroo('a', 'c', 'b') == ('b', 'c', 'a'), \
        format_err_msg(('b', 'c', 'a'), tuple_switcheroo('a', 'c', 'b'))


# Do not change the code below this line
if __name__ == "__main__":
    test_create_tuple()
    test_tuple_to_list()
    test_count_threes()
    test_get_index_of_five()
    test_get_second_to_last_element()
    test_get_last_three_elements()
    test_check_element_is_present()
    test_tuple_switcheroo()