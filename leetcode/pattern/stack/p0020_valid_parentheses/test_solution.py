import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


# LeetCode examples
def test_example_simple_parens(solution):
    assert solution.isValid("()") is True


def test_example_mixed_valid(solution):
    assert solution.isValid("()[]{}") is True


def test_example_wrong_close(solution):
    assert solution.isValid("(]") is False


def test_example_interleaved(solution):
    assert solution.isValid("([)]") is False


def test_example_nested(solution):
    assert solution.isValid("{[]}") is True


# Edge cases
def test_single_open_bracket(solution):
    assert solution.isValid("(") is False


def test_single_close_bracket(solution):
    assert solution.isValid(")") is False


def test_empty_string(solution):
    assert solution.isValid("") is True


def test_deeply_nested(solution):
    assert solution.isValid("({[({[]})]})") is True


def test_only_close_brackets(solution):
    assert solution.isValid("}])") is False


def test_correct_type_wrong_order(solution):
    # Right brackets but mismatched nesting order
    assert solution.isValid("[(])") is False


def test_long_valid_sequence(solution):
    assert solution.isValid("(())(())") is True


def test_unmatched_open_at_end(solution):
    assert solution.isValid("(()") is False
