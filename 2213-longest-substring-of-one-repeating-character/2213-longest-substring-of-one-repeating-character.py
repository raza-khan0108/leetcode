from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # Segment tree nodes store: [pref_len, suff_len, max_len, left_char, right_char]
        tree = [None] * (4 * n)
        s_list = list(s)

        def merge(left_node, right_node, left_len, right_len):
            p1, s1, m1, lc1, rc1 = left_node
            p2, s2, m2, lc2, rc2 = right_node

            # Default attributes after merge
            res_p = p1
            res_s = s2
            res_m = max(m1, m2)

            # Check if boundary characters match
            if rc1 == lc2:
                cross = s1 + p2
                res_m = max(res_m, cross)
                
                # If left child is uniform, prefix extends into right child
                if p1 == left_len:
                    res_p = p1 + p2
                
                # If right child is uniform, suffix extends into left child
                if s2 == right_len:
                    res_s = s2 + s1

            return [res_p, res_s, res_m, lc1, rc2]

        def build(node, start, end):
            if start == end:
                c = s_list[start]
                tree[node] = [1, 1, 1, c, c]
                return

            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            tree[node] = merge(
                tree[2 * node], 
                tree[2 * node + 1], 
                mid - start + 1, 
                end - mid
            )

        def update(node, start, end, idx, char):
            if start == end:
                s_list[idx] = char
                tree[node] = [1, 1, 1, char, char]
                return

            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)

            tree[node] = merge(
                tree[2 * node], 
                tree[2 * node + 1], 
                mid - start + 1, 
                end - mid
            )

        # 1. Build the Segment Tree
        build(1, 0, n - 1)

        # 2. Process Queries
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != char:
                update(1, 0, n - 1, idx, char)
            # The root node (1) always contains the global max_len at index 2
            ans.append(tree[1][2])

        return ans