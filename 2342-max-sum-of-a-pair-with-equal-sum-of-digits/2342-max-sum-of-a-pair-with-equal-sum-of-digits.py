class Solution:
	def maximumSum(self, nums: List[int]) -> int:
		d = {}
		res = -1
		for num in nums:
			s = sum([int(digit) for digit in str(num)])
			if s not in d:
				d[s] = num
			else:
				res = max(res, d[s] + num)
				d[s] = max(d[s], num)
		return res