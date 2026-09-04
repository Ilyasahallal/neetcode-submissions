class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for num in nums:

            # Évite les doublons
            if num in parent:
                continue

            parent[num] = num
            size[num] = 1

            # Relie num à num - 1
            if num - 1 in parent:
                root1 = find(num)
                root2 = find(num - 1)

                if root1 != root2:
                    parent[root2] = root1
                    size[root1] += size[root2]

            # Relie num à num + 1
            if num + 1 in parent:
                root1 = find(num)
                root2 = find(num + 1)

                if root1 != root2:
                    parent[root2] = root1
                    size[root1] += size[root2]

        return max(size.values())