from typing import List
class Solution:

  def lexicographicallySmallestArray(
      self, nums: List[int], limit: int
  ) -> List[int]:
    n = len(nums)

    # Pair each element with its original index and sort by value
    sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))

    result = [0] * n
    i = 0

    while i < n:
      j = i + 1
      # Group consecutive elements whose adjacent difference is <= limit
      while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
        j += 1

      # Extract and sort the original indices for this connected group
      group_indices = sorted(idx for _, idx in sorted_pairs[i:j])

      # Place sorted values into the sorted index locations
      for k, idx in enumerate(group_indices):
        result[idx] = sorted_pairs[i + k][0]

      i = j

    return result