import pytest

from .solution import Solution


@pytest.fixture
def sol():
    return Solution()


def normalize(groups: list[list[str]]) -> set[frozenset[str]]:
    return {frozenset(g) for g in groups}


class TestGroupAnagrams:
    def test_example_1(self, sol):
        result = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert normalize(result) == normalize(expected)

    def test_single_empty_string(self, sol):
        assert sol.groupAnagrams([""]) == [[""]]

    def test_single_char(self, sol):
        assert sol.groupAnagrams(["a"]) == [["a"]]

    def test_all_unique(self, sol):
        result = sol.groupAnagrams(["abc", "def", "ghi"])
        assert normalize(result) == {frozenset(["abc"]), frozenset(["def"]), frozenset(["ghi"])}

    def test_all_same_anagram(self, sol):
        result = sol.groupAnagrams(["abc", "bca", "cab"])
        assert normalize(result) == {frozenset(["abc", "bca", "cab"])}

    def test_multiple_groups(self, sol):
        result = sol.groupAnagrams(["ab", "ba", "cd", "dc", "ef"])
        expected = [["ab", "ba"], ["cd", "dc"], ["ef"]]
        assert normalize(result) == normalize(expected)

    def test_empty_strings_group_together(self, sol):
        result = sol.groupAnagrams(["", ""])
        assert normalize(result) == {frozenset([""])}
