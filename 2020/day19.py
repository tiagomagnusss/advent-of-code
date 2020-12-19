import regex

class Solution():
    def solveMessage(self, ruleList: [str], input: [str]) -> int:
        rules = {}
        def expand(word):
            return group(int(word)) if word.isdigit() else word
        def group(ident):
            return '(?:' + ''.join(map(expand, rules[ident].split())) + ')'

        for line in ruleList:
            ident, rule = line.rstrip().split(': ')
            rules[int(ident)] = rule.replace('"', '')

        reg = regex.compile(group(0))
        return sum(reg.fullmatch(m) is not None for m in input)

    def solveMessageNewRules(self, ruleList: [str], input: [str]) -> int:
        rules = {}
        def expand(word):
            return group(int(word)) if word.isdigit() else word
        def group(ident):
            return '(?:' + ''.join(map(expand, rules[ident].split())) + ')'

        for line in ruleList:
            ident, rule = line.rstrip().split(': ')
            rules[int(ident)] = rule.replace('"', '')
        rules[8] = '42 +'
        rules[11] = '(?P<group> 42 (?&group)? 31 )'

        reg = regex.compile(group(0))
        return sum(reg.fullmatch(m) is not None for m in input)


ruleList = """56: 39 28 | 110 10
85: 34 110 | 111 39
4: 39 74 | 110 44
125: 96 39 | 112 110
79: 39 117 | 110 24
91: 52 39 | 65 110
60: 39 83 | 110 58
101: 109 39 | 28 110
98: 130 39 | 88 110
8: 42
11: 42 31
27: 110 1 | 39 86
104: 28 110 | 44 39
120: 44 39 | 66 110
34: 110 35 | 39 46
116: 39 80 | 110 90
87: 74 39 | 64 110
76: 98 110 | 41 39
108: 115 110 | 44 39
59: 110 44
103: 110 36 | 39 33
66: 39 110 | 110 82
62: 39 102 | 110 116
30: 39 24 | 110 80
123: 110 44 | 39 109
93: 39 53 | 110 77
80: 39 39
83: 27 110 | 119 39
115: 39 110
22: 91 39 | 50 110
17: 110 127 | 39 15
110: "b"
69: 82 110 | 39 39
105: 39 63 | 110 107
21: 84 110 | 120 39
75: 110 39 | 39 110
128: 110 115 | 39 89
50: 39 108 | 110 99
70: 80 110
48: 39 95 | 110 61
25: 110 95 | 39 123
67: 39 114 | 110 101
114: 10 110 | 69 39
37: 74 110
89: 110 110 | 110 39
32: 26 39 | 62 110
130: 110 44 | 39 80
15: 39 3 | 110 93
20: 110 72 | 39 87
61: 39 80 | 110 117
58: 23 110 | 48 39
13: 66 110 | 117 39
44: 110 110
112: 39 32 | 110 85
99: 115 39 | 90 110
71: 110 123 | 39 113
46: 110 64 | 39 66
129: 110 24 | 39 89
84: 82 90
36: 39 71 | 110 81
78: 110 90 | 39 28
0: 8 11
100: 110 69 | 39 117
49: 90 110 | 69 39
9: 24 110 | 89 39
73: 110 29 | 39 106
35: 64 39 | 109 110
118: 76 110 | 47 39
12: 74 39
53: 69 39 | 28 110
77: 110 90 | 39 44
127: 39 14 | 110 43
111: 65 39 | 56 110
3: 39 5 | 110 100
109: 82 82
43: 55 110 | 126 39
7: 101 39 | 13 110
10: 39 39 | 110 82
121: 66 110 | 89 39
102: 44 39 | 74 110
81: 84 110 | 97 39
2: 124 110 | 88 39
82: 39 | 110
29: 79 39 | 52 110
54: 39 84 | 110 122
64: 82 39 | 39 110
65: 24 110 | 69 39
52: 110 69 | 39 115
74: 110 39
92: 39 19 | 110 57
51: 110 30 | 39 78
28: 110 110 | 39 39
126: 39 66 | 110 90
45: 17 39 | 92 110
90: 110 39 | 39 39
33: 18 39 | 54 110
16: 110 28 | 39 44
72: 39 115 | 110 117
106: 39 77 | 110 49
119: 39 97 | 110 16
113: 75 110 | 44 39
18: 129 39 | 37 110
41: 99 110 | 72 39
68: 110 118 | 39 60
6: 12 39 | 128 110
57: 39 21 | 110 2
5: 109 110 | 117 39
47: 51 39 | 7 110
124: 69 39 | 66 110
94: 39 103 | 110 105
39: "a"
1: 39 64 | 110 44
117: 39 110 | 39 39
42: 45 39 | 125 110
19: 25 110 | 6 39
26: 78 110 | 77 39
96: 39 73 | 110 22
38: 39 114 | 110 70
63: 110 40 | 39 67
95: 110 109 | 39 115
55: 66 82
14: 104 39 | 59 110
40: 39 101 | 110 4
31: 68 110 | 94 39
24: 39 110 | 110 110
86: 39 69 | 110 109
122: 90 39 | 64 110
97: 117 39 | 10 110
23: 39 121 | 110 9
107: 39 38 | 110 20
88: 39 44"""

input = """aaababaaaaaabbbaaaabbaaa
aaaabbbaaaaaabaaabbabaabbbbaabaaabbbababbbbabbabababaaaa
aabaababaabaaaaabbbbbbbbaaabbbaabababbabbaababaabbbabbabaababaaababaaabaaaabaaab
ababbabaabaaaabbbbbbaaabaabbbaabbaaaabbababbaaaaababbbbb
aabbbababbabbbbaaaabbaba
baababbaaabbbabbbbbaabbbbaabbaaaaabbbbab
aaaabbbaaabbaabbbaabbabb
baaaabbbabaaabbbbbabbaabbbaabbabbbbaababaabbbbabbababababbaaabbb
aabbbababbbaaabbbabbbbba
abbabbaabaabbbabbbaabaaaabbbbbaabbaaaabb
abbabbababbaaaaaababaaaaababaabababbabaaabbababa
abaaaababaaaaababbaaaabbabbbabaabbaababbabbaabbaababbbaa
bbbaabbbaabbabbbaaabaaba
bbababaababbbabbbbaaabab
bbbbbabbbbbbbbaaabbabbbaaaababaaabaaabab
babbaaaabaaaaabbbbababaabababbbababaaaba
abbaabababbabbaabbbbbbbabbbbbabaaaababbb
aabaaaabaabbbbaaaaabaaaa
aaabbbaaaabbabaabbabbbab
abbabbbaaabaabaababaabbbbaaabbaaaaabbbab
aaabaaabaaaabbabbbaaabaa
bbaabbabbbbbbbbaabbbbaaaaaabaaababbababbbbbabbbbbababbaabaaaaaabaaaaabab
bbbaabaabbbbbbbaaaaabbbb
abaaaaabaaababbaaabababb
abbbbaababbabbbaaababbba
bbbababbaaaababbbabbbbaabbbbbbbababaaaba
abaabaabababbaaaabbbaabb
ababbbaaaaababbabbbbbbab
abbababbbaababbaabbbbbaa
bbaabbabbabbabababbbaaba
bbbaabaababaabbbbbababbaabaaaaabbabbababaabbabaabbaaabab
baaabaaaaabbbababbbaaabbaaabbbab
aabababaabbaababbaaabaabbbaabaaababbabaa
bbbbaaaaabaaaaaaababbbab
abbabbbabaabbbabaabbbbbb
abbbbbabaabaabaaabaaabab
bbbbbbaabbbabaabbabaabab
aaaabaaabbbbabaababbabaa
baabbbbbbbaabbabbbaababa
babbbabbabbbbaaaaaaabbaababbaabb
babbbaabbabaaabbbababbba
bbabababbabbbbaababaaaaa
bbbabbabbaababbbbbbaabaaabaabaaabaaababbbbbbbaaabbabaabbabbaaaabaabaabbb
bbaabbabbbabababaabaabaaaabaabaaabbaabbbbaabbaab
aaaabaaababbabbbbbbbaaba
bbbaabaabbabbaaabbbaabba
bbaabbbbabbaababaaaaabab
babababbababbbbaababbabaabbaaabbaaaabaaaababaaba
aababbbbbbaabbabbabbabaa
baaabaabaababaabbbaaaaaa
bbbaaabbbbaababbbaaabbab
aababbbbbbababbabbaabbbbbaabbabaaaabbabb
baaaabbabbbbaaabaabababb
bbabbaaabbabababaaaaaaab
bbbaaabbabaabbabaaaaabbb
bbbaaabbabbaababbbabbaab
aabbaababababbbbbaabbbaabbbabbbb
abbbbbbaaababaabbabaaaba
abaaaaababbbbaaaaababbab
baababbaaaaabbbaaabaabbb
aaababaaabbabbbababababaaaababaabbabbbbbaababaaabaaabbba
aabbaaaaabaabaabbbbbaaaaabbbaaaabbbbabab
bbaabbbbbaabaaabaaababbb
bbbbabaaabaaaabaabbbabaa
aabbabbbbbbbbaabbaaaaaaa
baabbabababbabbbaabbbabaabbabbbbbaabbaaa
baaabbbbabbbaaaabbababaababaaabbbabbaaab
babaabbabaabbbabbbababaabbbbbbbaaaababbabbababababbbaabbbbabbaabaaaabaab
bbabaaababaaabaababaaaab
abbaabbabbabaaaabaaaaabaaaaaabbaaaaaaaaa
bbababbbaabbbbaabaaabaabbbbaabab
bbaaabbbaaaabbaaabbaabbbbbaaaaaaabbabbbaabbaaababaaabbbbbbabbbbabbbaaabbbbaababaabaabaaa
babbbaaabbbaabbbbabbaaaabbababbbabbabbabaaaabbbbababaaaababaaaaa
babbbaaabbbbaabbbbbabaaa
babbbaababaaaabbaabaaabb
abbbbaaaabbaabbbaaaabbbabaabbabaaabbbbbbbaabaaaa
abaaaaaabaaabbbbabbababa
abbbbaabbaaabaaaaaabbaaa
bbbbabbabaababbaabbbbaabbbabbbaaaabaaaaaaabbbbbbaaaabababbabaabbbaabbaab
bbbbabaaaabbababbbabbbaabbbbbbbbaaabbbabbaaaabab
abaaaaabaabbabbbbbaabbba
babbabbbaaaaabbabaaaaaba
abbaabbbabbabbaabbabaabb
aabbabbbbbaaaaababbbaaab
bbbaaabaabbabbbabaabaaaaaaaaababbaaaabbabaaabbaabababbbaabbaabaaabbabaab
ababababbababaaaabaaababaaaabbbb
babbabaababaabaaaaaabbbbbaababaa
aabaabaabababaabbaaaabaa
ababaabbabaabbabaabbbabaabababbb
babaabbbaabbaabbbbbaaaba
babbbabbbbabbbbababbabaa
abbbabbaaabbbbbabbbbbaab
baaababbbabaabbbbbaaaaba
baaababbbbababaaabaabaaaaaaabaaabbbaaaaaaababbba
babbaabbaaababaaabaababb
bbabbababbabaaaaaaaabbbb
abaaabbbaabbbbbaaabababb
bbaaabbbbababaabaababbaa
aaaaaaabbabaababbbaabaaaaaababbaababbbaabbaabaaabbaababb
babaaabbbabbbaaaaabbbaababaabbbbbbaabaab
baaaaabbbbbaabaabaabbbba
babbbabbabbbabbbaaabbbab
bbbaabbbaabaaaaabaababba
bbbbbbbaabbaabbaabababbaaaaaaabbaabaabbaabababaa
aabbabaababbabababbabaaa
abbbbaaabbababababbabbbb
baaabaaaaabaabaabbaabaab
baaaaabbbaabbbbbaaabbaaa
baaabbabbbaaaaaabbaaaaabababbbabaaabbaaababaaaabaabbbbababaabbab
aaabbbbababbabbaaaaaabab
abbabbabaaababaaaabaababbabaabbb
bbabbbbaabaababbbabbabbabbaaaabb
aabbababaabbababababaaaa
babbbbaabbabbbaabbbaaabb
aaaabaaabbababaababbabaa
babaaabbababbbaaaababbab
aaaabaabbabbaaaaaababbaabababaab
abaababbbbbaaaaababbbbbb
abaaaababbbbbbbbbaaabbaa
babbbbaaaaaabbaabbbababa
bbabababbbabbbbaabababba
abbbaaaaaabbaaaabbabbaab
baaabbbbbaabbbabbbabbabaaabbbbbabaaababbababaaaa
bbbabbbababababbbaaaaaaaabbbababbaaaaabbbabaabaaaaaaaaab
ababbaaaaabbbbbbabaabbbaababaaabaabbabbbabbaaaab
aabaaaabababbababaabaaaa
babaabbbbabbbabaabbabaaa
baababbbbbbbbabbaabaabba
bbbbaaaaaaabaaababbaaaaa
aabaabaabbbbaabbbbbaabba
bbbbbaababaaaaaaaaaaaaab
abaaaaaaababbbaaabaabaabbbababbaabbbbaaaabbabbbbaabbbbbb
babaabbaaabaaaaaaaaaabab
bbababbaabaaaabaaaabbaba
abaabbbbbaabbbbaaaabbabbbbabbaabaabbbabbabaaaabb
aababaababbbbbbaabbbaabb
baababbbabbbbbbaabaababa
aaaababbbaababbababbbbab
bbabaaaaabbbbbabaaabaaabaaababaaaabbabba
abaaaaabbaaaabbabbbabaaa
abbaababaabaaaaabbababbbabbbababaaaabaabaaababab
babbbbaabbabaaabbbababbabaabbabaabbaabaabbabaabb
aaababbaaaaabbababaaabaaabbbbbbb
abaaabbbbbaaabbabaabaaaa
bbbaabbbbabbaabbaabaabbb
babbaababaaabbbbabaabaabbbabbbaabbababbbabbaaabbbbabbbabbabbbbbb
bbaababbbbaaaaabbbabbbbabbbabbbbabbaaaaa
bbbabaababaababbbaaaabbb
abbaaaaabaabaaaaabbaabbbbaaabbbabaaabbbabbbbabaaabaababbbbaababa
baaaaabbabbbabbaaaaabbbb
aabaaaabbaabaaabbabbbbab
bbababbabbbbaaabbababbbbbbbbaaaabbbaaabbbbaaabaabbbaaaba
aaaaaaaababbbaaabaaaaaab
abbabbbaaaaabbaaaaaaabbb
aaababaaaabbaaaaaaababaabbbababa
aaabaaabbabbbabbaabababb
bbabbbaaababbaaaaaaaaaba
aaaabbbababaabbabaabaaabbbbabbbaaaabbababbaaaabbaaaaaaba
bbbbabaabbbbaabbbaaabaabaaaaabaaaaabbbab
bbbbaaaaabaabaabbabbbbba
abbabaabaabaabaabbaabbba
abaabbbabaaababbbabaabbbaabaaaaabaaaaaaa
abbaababbaabbbbbaaabaaba
babaaabbaabaaaaaababaaaa
baaabaaabbababbbbbaaaabbbaabbbba
bbbbbbbbabaaabaaaaabbaaa
aaaabbabaabbbabbaababaabbabbbbabbbabaaba
bbaababbbaaababbabbbabbbaaabbbabbbbaaaba
bbbabbbababababaaabababb
aabbabbbaabbaababababbaabaabaaaaaaabbbbb
aababababbbbaabbaaabbbab
aabbaaaaaaaaaaaaabbbbaba
aaaabaaabbbbabbaaabbababbaaabbbabbbaabab
bbaabbabaabbbbaaabaabbaa
bbaaabbbbbabbbabbaabaaaabbabaaba
abbbbaabbabbbbaabbbaabba
bbabaaaaaaaaabaaababaabb
baabaaababaaaaaabbababaa
abaaaababaabbbabbbbbbaaa
baabbababbbababbaaabbaabababbaab
abbabaabbabbaabbbaaabbba
abaabaabababbabaaabababb
aabaabaaaabaaaaaababbaab
abaaabaabbabbbaabbaabbba
bbbbaaabbaaabbbbababaaaa
aaababbaabaabbbabbababababaabbab
bbbaabbabbbbbbaabbbbabaaaaaabbbabbbbababaaabbabaaabaaabaababbaabaaababab
baaabaabbaababbbabaababbabbaaaba
bbbaaabbabaabaababababbb
bbabababaaabbaababbabbbb
aabaabaaabbaabbabaababab
bbbabbaaabbbbbabbabbaabbaabaaabb
baaabaabbbaabbabbabaaabbaabaaabb
aabaabaabbbabaabaabbabaaabbaaabbaaaaaaab
ababbabaaabbababbbabbbab
babbbbaaaabbabababbbaaaaababbaab
aaaabaaabbbbabbaaabaaaaaababbbbbbbaaaaaa
bbbbaaababbbbaabbbbbbbab
bbbaabaabaabbbbbaabaaabb
aaaabbabaaaaabaaabaaabab
baabbbabbbbbabbaababbaab
babbbabaabaaaabbbabbbbba
bbbbabaababbbbaabbaabaaa
aabbababbbaabbbbbaaabbbbabbaaaaabbaababbaaaabbab
bbaabbbbbbababbababaabab
bbababbaabbababbbabbbbab
ababbbbabbabbbabaaabbbabaabbaaab
bbabbbaabbabbbabaaabbbbbbabaabbbaabaaabbababaaaaaaaaababbaaaaaaa
aabaabaaabbabbbaabbbaaba
baaabbbbbbabbbbaaaaababa
babbbaabbaaababbabbbbbbb
bbbaaabbbbabbbbaabbabaaa
bbbabaababbaababbabbbaababbabbaabbabbabb
bbaababbbbabababbbabaaba
bbbbbbaaabbaababbbbabbbbbaababaa
aaababbabbababbabaaaabbb
aababbbbbaaaaabbbaaaaabbbbbaaabbaabaaabaabaabbaabbaabbba
babbabbaababaaaaaababbaabbaabbabaaaababaababbaab
abaababbbaaababbbababaaa
bbbbbbbbababaabbabababaaaababaabaababaabbaabaaababaaaababbaabbaa
bbaabbbbaaabbaabbaaaaaba
bbababaabaabbbbbbaababaa
abbabbbbbbababaaaabbabbbbbababaabbabaabbbbabbbbbabaabbbb
bbabaaababbbbaaabbbabbabbabaabbababaabba
aaaaabaabbbbabbabbaababa
abaabbabbbbabaabaaaaaaaaaababbab
aaaaabbaaaabbaababbabbbaababbaaababaaabbabbbaaab
aabbabbbbaaabbbbabaaabab
babbababaaaabbbaabbbbbaa
aaaabbababbabbbababbbbba
babaaaabbaaababaaabaababbbaabbabbaaabaaabababaaabaabbabbbaabababbbbababbabbaabaabaabaaba
babababaabbababbaababbaa
abaabbbaaaaabbabbbbaabab
abaabbbaabbbbaaaaababbaa
bbabaabbaabaabbaabaabbaa
aaababaaabbbbaaabbaaaaaa
bbbabbabbaabaaaaaabbbbababbabbbb
bbbbbbbabbbaaabbababbabaaabbabbbbbbaabaaabababbbaaabbabb
bbbaabaaaaaabbaaaaaaabab
abaabababababaabaababbabaaababaabbabaabbbbbbbbba
aabbabaaaabbaaaababaaaaa
abbaabbaabbbbaaaababaabb
babbabbbbbbbbbbbabaabbaa
bbabbbbababaaabbbbbababa
bbbbaaababaabbabaaabbabb
aaaabaaabbabaaaaaaabbabb
abbaaabbaaababbaaaabbbaabbbaabaaaabbaababababbbbabbbbbbaaaaaaabbbabbababaaaaaaaabbbaaababbbbbaab
baabaabaabbabbabbbbaaababbabababaababbabbbbaabaaabababaaabababbabbabbaaabababbbbbbbbbbbaaabbaaba
abbabbbbabbaaaababaaaaabaababbaabbabaaabaabbabbbabbbaabbaabbaaab
bbabbbbaaabbbabaabaabaaaabaaabab
babababababbbabbababbabaabaabbbabbaaabbb
abaaaabbaaabbbaabaaaabaa
bbaabaaabbaabbabaabbaaab
bbbbbabbbaaabaabbbaabbbbaabbbaabbaaaaaaabbaabaab
bbbbabbaaabbabbbaaabbbab
aaabbbbaaabbaaaabbbaaaaaaaabbbbababaaabaababbaab
bbbbbbbbbbbaabaabaaabbba
abaaaabaabaabaaabaaabaabbababaababbaaaababbabbbbabaaabba
baaabaabbababaabbbbabbbbbbbabbbbaaabbbab
aaabbbbaabbabaabbbabaaabaaabbaababbbaaba
bbbbaabbaabaabababaaabab
aaaaaaaaabbabbabababbbba
bbabaaaaaaaabbababbbaaba
babbabababaaaabbaaabbbaaaabbbabaaabbbbaabaaababbaaabbaba
aaabaaabbabbaaaaabbaaabb
aabbbaabaabaaaabbaababab
bbaabbbbbabbbabbbaabbbaa
bbababaaababbaaabaabbaaa
baaaabbabbbbabbbaaaaabab
abaabaaabbbbbbaabbaaabaa
babbaababbaabbbbbaabbababbabbbaababbbbba
bababababbabababaaaaabbb
aabbbbaabbbabaababababba
babaaabbaabbbabbbbabbbbbabbabbbababaabaa
baaabbbbbaaabaabababbbbb
baabbbbbbabbbaababaaabba
bbbbababbababaabbbabbbaaaaabaabaababbabbbaabaaaabaabaaaaabbbabbaaaaabbab
aaabbbaaabaabaababbabbbaaaaaabbabbbabbabaabbabbbaaaabaabbbabbaababbaaaab
abaabaabbabbaaaabbbaaaab
bbabbbababbbabaaabaaaaab
aaaabaaabbababaaabaababa
aaaaabaababbbabababaabaa
bbaaababbbaabbabbabaabbababbbaaa
abbaababbaabbabaaabaaaaa
aabbabbbbaaababbbbbbaaabbbbaabaaaababaababbababa
babbabbaabbaababbabaaaab
bbbbbbbaaabbabababababaaabababab
abbbaaaabaaaabbabaaabaaabbabaaaaaabbabbaaaabababaaaabbbb
babbbabbabbabbabaabbaaab
abaaabaaaabbababbbbbbaaa
bbbabbbbabbbbbbabbabaaba
bbbabbaaaababaabaabbbabaabaaaabbbbabbaaa
bbabaaabbbbababbaaababab
aabbbbbabababbbbbbaaaabb
abbabbabbbababaabbbbaaba
abaabaabbbaaaaabbabbbbaaabbababbbabaaabaaaabbaba
bbbabbbaaaabbbaaaaaaaaab
abbbbaabbbbaaaaaabbababa
ababbaabbbbaababbbaaabaaabbabbbabbbaababbbaabbba
babbabbaabbbbbbabbbabbbbababaaabbaaabbab
aaaabbaabbabbbbaaaaaaabb
bbbababbbbbbabaababbabaaaabbaabbbbbbbabbaabbbaabbaaabbababbbabbababbbabaaaabbbaabaaaabba
babbbabaabbaabbabbabbaaabbaaaaaaabaabbbb
babababaaaaaaaaabbbbbaaa
bbaabaaababaaabbbabbaabababaababbbbbabbb
baaababbbbbbaaaaaabbaaaabaaabbab
bbbbbabbaabbbaabaabbbaaa
bbbbabaaabaaaabaaaabaabb
babbaaaaaabaabaabaabbbaa
aabbbbaaaaaaaaaaaabbaabbbaaaaaba
aaabbbaaaaaabbbaababbabaaaaabaab
abbaabbabbabaaaaaabbaaba
ababbababbbabbbaabbbaaab
aaabbaabaaaababbaaaabbaaababaabbbabbbbbb
abbaabbaabaabbabbaabbabb
baababbbbbbaaabbaaabaaba
babbaaaababaabbabaaaaababaaababbaaabbaaa
bababbbbbbbabbbbbababbaa
bbaabaaabbababaabbabbababbabbaba
aaababaabaaababbaaaabbabbaaaaaab
bbaabaaabaaaabbabbbabbaaaaabbbbbaababbba
aaabaaabbbbabbaabbaaabaa
baaabaaaabaaaabbaaabbaaa
aabababaaababaabaaabaaba
bbababbbaabbabbbababbabaabbaabbabbabbabaabbbabab
bbbabbbbbbaabbabbaaabbaa
babbbabbaabbbaabbbaaaaaa
aabbabbbaaaaabbaababbbab
bbbbabbabbbbbaabaabbbaaa
abaabaaaaaaaaaaaabbbbbbaabbabbaabaaaaaaa
abbaabababaabbbabaaaabaa
aaaabbbaaabbabaaaaabbaaa
bababbbbbbabbbbabababbaa
bbbbaaaabaaaabbabbaaabaa
babbaababbbbaabbbaaaaaaa
bbbabbaabbababbaabbbbbaa
babbabbbbabbabbbbaabaaaa
abaabaaaaababbbbbaaabbba
bbabbbababbbbbbabbabbbababababaabbbbaaaababbbbbaaababbbabbbbbabaaabaaaaa
aaaaaaaaabbababbbaaabbab
baaabaaabbabbbbababaabaa
bbabbbbabbbbaabbbaaaaaab
bbaababbabaaabaaabbabbbbbabbaaab
bbbabaabaaabbbaaaabaabbb
aaaaabbbbbaaabaaaabaabbb
abaaabaabbbaaaaaabbbaabb
bbababbbbabbabbabbaaaaba
aabaaaabaaabbbbaaaaabbaaaababababbbbaaabbabababb
bbaaaaaabbabbbababbababa
aabaabaaabbbabbbaabaaabb
bbbbbaabbbbaaabbaabababb
bbbbbaabbbbbbaabbabbbbbb
bbaaabbabbbbbaabababaaaa
babaabbaaaaaaaaabbaaabbbaabaaaabbbbaabbb
baabaaabbbbbbaabbbbbabbb
baaababbbabbababbabaabab
aabbabaababbbabbbabbbaaaaaabbabaabaaabab
bbbbabaaabbabbabbbbaaaba
aaabbaabbabaabbaaaaaabbabaaabbab
abbbaaaaabbaabbbbbbbabababaaababbbabaabb
aaaaaaaababaaabbbabbbbba
abbabbaabbaabaaabbabaaba
abaabbbabbbaaabbbabbaaaabbabbababaababaabbaabaabbaaaabaa
aaaaaababaabbaaaaaaaaaab
aaababaaaabbabbbbbaaaaaa
aabbababaabbbaabbbbbbbab
bababbbbbabababaaabbabba
abbbabbbbaaababbbbbbbbab
bbaabbbabbaabaaababbaabbbababbabbbabbbabbaabababaabbbaaaaabaabababbbaaaaabbabaaaaaabbaaa
babbbaaaabbbabbabaaabbba
bbbaabbbabaaaabaaabaabbb
aaababbabbbababbbbaabbba
abaaaabaaabbabaaaabbaabbbaaabbbbbabbabaaabbbabaa
abaabbbabbbbbabbbbbababa
aabaabaaabbababbaaaabbabbaabbbaa
abbabbaabaaabaabbababbab
babbaababbabbbbaaabbbaabbbbaaaabaaababbb
bbbaabbbbaaaaaaaaabababbbaabbbba
babbbbaaaaaabbaabaaabbaabbabaaaaaaabaaaa
bbbabbababbabaabaabbbbbb
bbabbbbaabaabbbabbabbabb
bbabaaabbaabbbbbabbabbabbaaababbbbbababa
baaabaabaabaaaabaaaaaabb
aaaabbbaabaabaababababab
bbabbababbbbbbbabbbbabab
babbbabbbaaaaabbbbbbabbb
baaababbbbaaabbaabababaa
babbabbaaabbaabbabbabbbb
aabbbababbabbaaaabbaaaba
ababbaaabbbabbabbbabaabb
bbaabaaabbbbbaaabaaabbaabaabbbbaabbaabaababbaabbaaaaabbbaababaabaaaaabaaaabbaaab
babaaabbabaaabbbaaabaaba
babaabbbbabbaabbaabbabaabbbbaabbaaababbbbbbaaaabaabaaabb
aaababaaaabbabbbbaabbaab
abbaababaaaababbaaabbbbbbababbbabbbbabaababbaabbaabaaaaa
aabbaaaabbabbbbbaaabbbab
babbaabbabaaabaabaabbbabaaabbbbbabbaaabaaaabbbbb
aabaabababbaabbaabbbbbaa
aabbabaabbbaaabbbababbba
aabbabaabbbaabaaabbbbbaa
bbbbaaabbbabbababbbabaaa
aabbbbbaaababaabbbaaaaaa
bbbababbabaaaabbaaaaabbb
abaaaaababaaabbbaabbbbab
bbabbabaabaaaaabbaabaaba
bbaaabbbabbbabbababbbaababaabaabbaabbaaa
babbaaaabaabaabaabbbaaaaaaabbabbabaabaaaabaaabaabaababaaaaaaaaaa
abaabbabaabaabaababbbbaabbbabbaabbaabaaabaababab
baabaaabbbaabbbbbbaaaabb
aaaaabaabbaababbabaabaaaaababbab
aaaabaaabbaabbbbaaabbbbb
ababbbaaabaabbabaaaabaaabaaaaabbababbabaaaabbabbaabaaabbbbbababa
aaababbaaaabbbaaaabaaaaaaaababaaabbbaabbbaaaaaaabaaaabaa
aababbbbaabbbabbabbabbaababbabbababaabaa
aabbbbbabaaabaaabaaababa
bbbaaabbbaabbbabbbbababa
aaaaaaaababbbabbaabaabbb
aabababaaabbbbbabbaababa
abaabbabbabbbaabaaabaaba
bbabbbbaabaaaaabbbbababa
aababaababbbbbabbaabaaabbbbaabaabbabbabb
aaabbbbabbabbabaaaababbb
babbababaabaabaababbbbab
baaaaabbaaaabbaabaaaabaa
bbaaabbaaabbbaabababbababbbbbaababababba
abaabbaabaabaaababbbbbbbbbbbbbabbbbbabba
abbabbbabaaaabbabaaaabaa
bababbbbaabbabaabbabbbab
bbbabaababbabaabaababbab
bbbabbbababbbaaaaabaaaba
aaaababbaaababaaaaaaaabb
abbaabbbbabbabbbabbaaaaa
abbaabbbbaaabaabaabbbababbaaabaababbaaababbbbbaa
bbbabbbbaabbaabbaaaaaabb
bbabbaaaabaaaaabaaaaabbabaaaaaabaaabbbab
aaabbaababaaaaabaababaaaabbaabaa
babbaabaabbabbaaaaaabbbb
abaabbabaaaabaaabaabaaaa
baabbabbabbbababbabbbabaabbbbaaababaababbbabaabaabbaababbbbabbabbbbbaaaaabbabaaa
babbababbbbbaaaaaaabbaba
bbbbbaabaabaaaabaabaaaabbbababbbaaabbaab
baabbbababaabaaaaabbabbbaababbbbaaababbaabbabbabbabababbbabababbbbbbabababaabbaa
aaabbaaaaaabbababbbbbaabbbabbbbbabbaababbbabbbabbaaabbabbaaabbbaaababbaa
bbabaaaabbababaabaaabbbbabbabbbb
aaababbaaabaaaabbbaaaaba
abbabbabaaaababbaabbbaaa
bbbaabbbbabbabbbbbaaabaa
babbbabbababbabaabbbabab
bbbaabaabaaabbbbbababbba
bbabbbbababbbabaabbaaaba
bababababbababbbbaabbaab
baabbabaaaabbbbbbbbbbaba
baababbbbabbaabaabbabaabaabaaaabaabababb
bbababbabbaaababbaabbbaa
babaabbaaabaabaaabbbaaab
bbaabbabaaababaaababaaba
bbabbbbababbabbbabbbaaab
bbbaabbbaabaabaaabbabbabbabbaaaababbabbbbaaaabababbbaaba
bbababbaabbbabbabbababbaaaaabaab
baababbabbababaabbaaaaabbaaababbababbabb
bbababbabbaabaaabbaaabaa
abbabbbababaabbbabababaa
bbbbaaababbabbbabbabbabb
aabbaabbaaaababbababaaab
bbaaabbabaabbabaabbbbbaa
abbbbbababaabbabaaababbabbababbaababaabaabbbaabb
bbbabbbbbbaaaaaaaaaabaababababbb
bbaabbabababbbaaabababba
bbaabbabababbaaabaaaabaa
aabaabaaabaaaabbbbaabbba
baabbabaaabbabbbbabbbbaaabbaaabbababaaaa
bbaaabbabbababbbababbaab
aabbaabbbaabbababaababbbabbbabab
aaaabbabbabbbaaabbbbbabbabaaaaabbababbbaaaabbbbb
aabababaabaababbbabababaaabbabba
bbabbbaababbbbaaaaaaabab
aabbaabbbbbaaaaabaaaaaaa
abbabaabaabaaaaaabaaabab
bbabaaaaabbbbaaabbbbbbaaaabbabbbaababbaa
abbabbaaaaaaabbabbbababbbbbbbbbbbababaabaabbbabbbbbababa
abbbbbabaaaaabbaabbababa
aababababbaaaaababbbabaa
bbbaaaaabababababaabaaaa
babbbabbbabbaabbbabbbbab
aaaaaabbabaaaaabbaabbaabbbababaa
bbbbaaabaabbababaabbaaba
abaabbbabbbaabaabaaababa
babbabbbbaaababbabbbbabb
aabbbbaabbaabbbbabbababbabbabbabbbaaabbabbbbbbbbaaaaaaab
baabaaabbbababbbbbbbbbabbbaaaaaa
aabaaaaababaabbbabbbbaabaabaabaababbabbbbabbbbaaabbbaabbaaaabaabbaabaaba
ababbababbbbbbbbbabaabab
abaaaaaaaabaaaabbbaaaaba
abaaaababaabaaabbbaabbaa
bbababbaaaabaaabbaabbaab
babbaaaaabaabaababbbbabb
abaaaaaaaaababaaabbbaaaaabbababbabababbb
aaaaaaaababbabbbbbabbbab
abbbabbbbbbbbbaaababbabaabaabaaaaaaaaaababbabbbb
abbabbaaabaabbbabbabbaab
abaabbabbaaababaaabaabbbbababbbbaaaabaaa
abaababbbbabbbbaababbabb"""

sol = Solution()
print("---------------------------- Part 1\r\n")
print(sol.solveMessage(ruleList.split("\n"), input.split("\n")))

print("---------------------------- Part 2\r\n")
print(sol.solveMessageNewRules(ruleList.split("\n"), input.split("\n")))