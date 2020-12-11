class Solution:
	"""
	Part 1
	"""
	def countOneThreeJolts(self, joltages: [int]) -> int:
		joltages.sort()
		joltages.append( 3 + joltages[-1] )

		offOne = 0
		offThree = 0
		current = 0
		for joltage in joltages:
			if joltage - current == 1:
				offOne += 1
			else:
				offThree += 1

			current = joltage
		
		print( offOne )
		print( offThree )
		return offOne * offThree

	def tribonacci(self, n):  
		a = 1.839286755  
		b = -0.4196433776-0.6062907292j  
		c = -0.4196433776+0.6062907292j  
		return round((a**n/(-a**2+4*a-1) + b**n/(-b**2+4*b-1) + c**n/(-c**2+4*c-1)).real)

	def getArrangements(self, joltages: [int]) -> int:
		numbers = [0] + adapters
		consecutive = 1
		ris = 1
		for i in range(1, len(numbers)):
			if numbers[i] - numbers[i-1] == 1:
				consecutive += 1
			else:  
				ris *= self.tribonacci(consecutive)
				consecutive = 1
		
		return ris * self.tribonacci(consecutive)
		
input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

input = """17
110
146
144
70
57
124
121
134
12
135
120
19
92
6
103
46
56
93
65
14
31
63
41
131
60
73
83
71
37
85
79
13
7
109
24
94
2
30
3
27
77
91
106
123
128
35
26
112
55
97
21
100
88
113
117
25
82
129
66
11
116
64
78
38
99
130
84
98
72
50
36
54
8
34
20
127
1
137
143
76
69
111
136
53
43
140
145
49
122
18
42"""

adapters = [int(i) for i in input.split("\n")]
print("---------------------------- Part 1\r\n")
sol = Solution()
res = sol.countOneThreeJolts(adapters)
print(res)

print("---------------------------- Part 2\r\n")
pathsFrom = {}
target = adapters[-1] + 3
res = sol.getArrangements(adapters)
print(res)