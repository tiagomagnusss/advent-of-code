class Solution:
    """
    Part 1
    """
    def dontKnow(self, numbers: [int], limit: int=2020) -> int:
        nMap = {}
        i = 0
        while i <= limit:
            n = numbers[i]
            x = (i - nMap[n]) if n in nMap else 0
            nMap[n] = i

            i += 1
            if i >= len(numbers):
                numbers.append(x)
        return numbers[limit - 1]

input = [13,16,0,12,15,1]

print("---------------------------- Part 1\r\n")
sol = Solution()
res = sol.dontKnow(input)
print(res)

print("---------------------------- Part 2\r\n")
res = sol.dontKnow(input, 30000000)
print(res)