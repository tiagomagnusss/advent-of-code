class Solution:
    """
    Part 1
    """
    def countActive(self, input: str, zpos: int=8) -> int:
        activeCells = 0
        # input é 8x8
        # mapa z, y, x
        map = {0: {}}
        for y, row in enumerate(input.split("\n")):
            map[0][y] = {}
            for x, cell in enumerate(row):
                if cell == "#":
                    activeCells += 1
                map[0][y][x] = cell
        
        # preenche o mapa com zpos planos
        after = zpos
        before = -after
        while after > 0 and before < 0:
            map[after] = {}
            map[before] = {}
            for y, row in map[0].items():
                map[after][y] = {}
                map[before][y] = {}
                for x, cell in row.items():
                    map[after][y][x] = "."
                    map[before][y][x] = "."
            after -= 1
            before += 1

        qty = 0
        cycles = 2
        planeOrder = [0]
        for i in range(1,zpos+1):
            planeOrder.append(i)
            planeOrder.append(-i)
        while cycles > 0:
            for z, plane in zip(planeOrder, map.values()):
                print(f"plane {z}")
                for y, row in plane.items():
                    rowStr = ""
                    for x, cell in row.items():
                        rowStr += cell
                    print(rowStr)

            for z, plane in zip(planeOrder, map.values()):
                for y, row in plane.items():
                    for x, cell in row.items():
                        neighbours = 0
                        # verifica os dois planos adjacentes
                        for possiblePlaneIx in [z-1, z, z+1]:
                            if possiblePlaneIx in map:
                                possiblePlane = map[possiblePlaneIx]
                                
                                # verifica as duas linhas adjacentes
                                for possibleRowIx in [y-1, y, y+1]:
                                    if possibleRowIx in possiblePlane:
                                        planeRow = possiblePlane[possibleRowIx]

                                        # verifica o meio para outros planos ou outras linhas
                                        if (possiblePlaneIx != z or possibleRowIx != y) and planeRow[x] == "#":
                                            neighbours += 1
                                        # direita
                                        if x+1 in planeRow and planeRow[x+1] == "#":
                                            neighbours += 1
                                        # esquerda
                                        if x-1 in planeRow and planeRow[x-1] == "#":
                                            neighbours += 1
                                            
                        if cell == "." and neighbours == 3:
                            map[z][y][x] = "#"
                        elif cell == "#" and neighbours not in [2,3]:
                            map[z][y][x] = "."
            cycles -= 1

        qty = 0
        for z, plane in map.items():
            for y, row in plane.items():
                for x, cell in row.items():
                    if cell == "#":
                        qty += 1

        return qty

input2 = """.....
.....
..#..
...#.
.###."""

input = """..##.##.
#.#..###
##.#.#.#
#.#.##.#
###..#..
.#.#..##
#.##.###
#.#..##."""

print("---------------------------- Part 1\r\n")
sol = Solution()
res = sol.countActive(input)
print(res)

print("---------------------------- Part 2\r\n")
res = sol.countActive(input)
print(res)
