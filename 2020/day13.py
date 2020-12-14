import copy

class Solution:
	"""
	Part 1
	"""
	def findEarliestBus(self, time: int, busses: str) -> int:
		busses = busses.replace("x,", "").split(",")
		earliest, minDiff = time, time
		for i, x in enumerate(busses):
			x = int(x)
			diff = x - (time % x)
			if diff < minDiff:
				earliest, minDiff = x, diff
			else:
				earliest, minDiff = earliest, minDiff

		return earliest * minDiff
	
	def findEarliestTimestamp(self, busses: str) -> int:
		busses = [(busIdx, int(bus)) for busIdx, bus in enumerate(busses.split(",")) if bus != 'x']
		_, period = busses[0]
		t = 0

		for i, x in busses[1:]:
			offset = None
			x = int(x)
			while True:
				if (t + i) % x == 0:
					if offset is None:
						offset = t
					else:
						period = t - offset
						break
				t += period
		return offset

input2 = """939
7,13,x,x,59,x,31,19"""

input = """1001798
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37"""

print("---------------------------- Part 1\r\n")
sol = Solution()
inputs = input.split("\n")

res = sol.findEarliestBus(int(inputs[0]), inputs[1])
print(res)

print("---------------------------- Part 2\r\n")
res = sol.findEarliestTimestamp(inputs[1])
print(res)
