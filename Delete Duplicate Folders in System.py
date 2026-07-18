"""
LeetCode 1948. Delete Duplicate Folders in System

Approach
--------
1. Build a trie (nested dict) from the given paths. Each node = a folder,
   keyed by its name, holding a dict of children.

2. Post-order DFS: serialize each subtree into a canonical string that
   represents its *shape* (child names + their own serializations, sorted
   so order in the input doesn't matter). Use a hashmap
   serialization -> count of subtrees with that exact serialization.

3. A second DFS walks the trie again. Any node whose serialization occurs
   more than once (and is non-empty, i.e. has children) is marked for
   deletion. We stop recursing into deleted nodes (their entire subtree
   goes with them, per the problem statement) and only recurse into kept
   nodes, collecting the surviving full paths.

Why this is optimal
--------------------
Every folder must be visited/serialized at least once, and comparing
subtree structure fundamentally requires representing each subtree as
something comparable (its serialization). So:

- Time:  O(N * L + N log N) roughly, more precisely O(S) where S is the
         total number of characters across all serialized strings
         (each node's serialization is built once from its children's
         already-computed serializations via string concatenation, and
         the sort at each node is over that node's number of children).
         In the worst case this can be O(N^2) if the trie is very
         unbalanced (e.g. all paths under one long chain sharing huge
         serializations), but this is the accepted/optimal complexity
         class for this problem on LeetCode — there is no known
         approach that avoids materializing subtree signatures.
- Space: O(N) for the trie + O(S) for the serialization strings/hashmap.

This is the standard accepted optimal solution (trie + serialize +
hashmap + mark-and-sweep), and runs in ~O(N * L log L) in practice for
LeetCode's test cases, where L is average folder-name length / branching.
"""

from collections import defaultdict
from typing import List


class Solution:
    def deleteDuplicateFolders(self, paths: List[List[str]]) -> List[List[str]]:
        # 1) Build trie
        root = {}
        for path in paths:
            node = root
            for folder in path:
                node = node.setdefault(folder, {})

        # 2) Serialize each subtree exactly once (post-order), cache the
        #    result per node (by id), and count how many nodes share each
        #    serialization.
        count = defaultdict(int)
        serial_of = {}  # id(node) -> serialization string

        def serialize(node: dict) -> str:
            if not node:
                return ""
            parts = []
            for name in sorted(node.keys()):
                parts.append(f"({name}{serialize(node[name])})")
            serial = "".join(parts)
            serial_of[id(node)] = serial
            count[serial] += 1
            return serial

        serialize(root)

        # 3) Second pass: skip subtrees whose serialization is duplicated,
        #    collect full paths for everything else.
        result = []

        def collect(node: dict, path: List[str]) -> None:
            for name in sorted(node.keys()):
                child = node[name]
                if child and count[serial_of[id(child)]] > 1:
                    continue  # duplicate subtree -> delete this folder entirely
                path.append(name)
                result.append(list(path))
                collect(child, path)
                path.pop()

        collect(root, [])
        return result


if __name__ == "__main__":
    sol = Solution()

    # Official LeetCode Example 1
    # /a, /c, /d, /a/b, /c/b, /d/a  -> a and c both contain only an empty
    # "b" folder, so a, c, a/b, c/b are all deleted; d and d/a remain.
    print(sol.deleteDuplicateFolders(
        [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
    ))
    # Output: [['d'], ['d', 'a']]

    # Official LeetCode Example 2
    print(sol.deleteDuplicateFolders(
        [["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"],
         ["a", "b", "x", "y"], ["w"], ["w", "y"]]
    ))
    # Output: [['a'], ['a', 'b'], ['c'], ['c', 'b']]
    # (w and a/b/x are both a single empty "y" child -> identical -> both
    # deleted along with their y subfolders)

    # Official LeetCode Example 3
    print(sol.deleteDuplicateFolders(
        [["a", "b"], ["c", "d"], ["c"], ["a"]]
    ))
    # Output: [['a'], ['a', 'b'], ['c'], ['c', 'd']]
