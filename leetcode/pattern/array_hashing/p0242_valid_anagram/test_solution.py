import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


class TestValidAnagram:
    def test_example_anagram(self, sol):
        assert sol.isAnagram("anagram", "nagaram") is True

    def test_example_not_anagram(self, sol):
        assert sol.isAnagram("rat", "car") is False

    def test_different_lengths(self, sol):
        assert sol.isAnagram("ab", "abc") is False

    def test_single_char_match(self, sol):
        assert sol.isAnagram("a", "a") is True

    def test_single_char_mismatch(self, sol):
        assert sol.isAnagram("a", "b") is False

    def test_repeated_chars(self, sol):
        assert sol.isAnagram("aab", "baa") is True

    def test_same_chars_wrong_counts(self, sol):
        assert sol.isAnagram("aab", "bab") is False

    def test_all_same_char(self, sol):
        assert sol.isAnagram("aaaa", "aaaa") is True
