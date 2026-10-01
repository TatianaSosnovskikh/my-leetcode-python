class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1, set2 = set(nums1), set(nums2)

        result = list()

        if len(set1) < len(set2):
            small = set1
            big = set2
        else:
            small = set2
            big = set1

        for num in small:
            if num in big:
                result.append(num)

        return (result)