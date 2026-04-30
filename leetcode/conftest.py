from __future__ import annotations

from collections import deque
from typing import Optional

import pytest

from leetcode.utils import ListNode, TreeNode


@pytest.fixture
def make_list():
    """Build a singly-linked list from a Python list of values."""

    def _build(vals: list[int]) -> Optional[ListNode]:
        if not vals:
            return None
        head = ListNode(vals[0])
        cur = head
        for v in vals[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head

    return _build


@pytest.fixture
def list_to_vals():
    """Flatten a singly-linked list to a Python list."""

    def _flatten(head: Optional[ListNode]) -> list[int]:
        result: list[int] = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    return _flatten


@pytest.fixture
def make_tree():
    """
    Build a binary tree from a level-order list (LeetCode convention).
    None entries represent absent nodes.

    Example: [1, 2, 3, None, 5]  →  root=1, left=2(right=5), right=3
    """

    def _build(vals: list[int | None]) -> Optional[TreeNode]:
        if not vals or vals[0] is None:
            return None
        root = TreeNode(vals[0])
        queue: deque[TreeNode] = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])  # type: ignore[arg-type]
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])  # type: ignore[arg-type]
                queue.append(node.right)
            i += 1
        return root

    return _build


@pytest.fixture
def tree_to_vals():
    """Serialize a binary tree to a level-order list (trailing Nones stripped)."""

    def _serialize(root: Optional[TreeNode]) -> list[int | None]:
        if root is None:
            return []
        result: list[int | None] = []
        queue: deque[Optional[TreeNode]] = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append(None)
            else:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result

    return _serialize
