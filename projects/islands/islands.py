islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def dft_recursive(node, visited, islands):
    if node not in visited:
        visited.add(node)

        neighbors = getNeighbors(node, islands)
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, islands)

def getNeighbors(node, islands):
    row, col = node
    land = []

    # if row able to step back, add coordinates to land
    if row < len(islands) - 1 and islands[row + 1][col] == 1:
        land.append((row + 1, col))
    # if row able to step forward, add coordinates to land
    if row > 0 and islands[row - 1][col] == 1:
        land.append((row - 1, col))
    # if col able to step back, add coordinates to land
    if col < len(islands) - 1 and islands[row][col + 1] == 1:
        land.append((row, col + 1))
    # if col able to step forward, add coordinates to land
    if col > 0 and islands[row][col - 1] == 1:
        land.append((row, col - 1))

    return land

def island_counter(islands):
    visited = set()
    total_islands = 0
    # iterate through matrix
    for row in range(len(islands)):
        for col in range(len(islands)):
            node = (row, col)
            # when we hit a 1, if not visited, run a dft/bft
            if islands[row][col] == 1 and node not in visited:
                dft_recursive(node, visited, islands)
                total_islands += 1
    
    return total_islands

print("Number of islands for `islands` = {0}".format(island_counter(islands))) # returns 4
print("Number of islands for `big_islands` = {0}".format(island_counter(big_islands))) # returns 13