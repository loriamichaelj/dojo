import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_panama(solution):
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True


def test_example_race_a_car(solution):
    assert solution.isPalindrome("race a car") is False


def test_example_single_space(solution):
    assert solution.isPalindrome(" ") is True


# Edge cases
def test_single_letter(solution):
    assert solution.isPalindrome("a") is True


def test_two_same_letters(solution):
    assert solution.isPalindrome("aa") is True


def test_two_different_letters(solution):
    assert solution.isPalindrome("ab") is False


def test_only_non_alphanumeric(solution):
    assert solution.isPalindrome(",.!") is True


def test_mixed_case_palindrome(solution):
    assert solution.isPalindrome("AbBa") is True


def test_digits_palindrome(solution):
    assert solution.isPalindrome("0P0") is True


def test_digits_not_palindrome(solution):
    assert solution.isPalindrome("0P1") is False
