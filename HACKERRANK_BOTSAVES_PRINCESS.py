def displayPathtoPrincess(n, grid):
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))

    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]

    if drows < 0:
        for _ in range(abs(drows)):
            print("UP")
    else:
        for _ in range(drows):
            print("DOWN")

    if dcols < 0:
        for _ in range(abs(dcols)):
            print("LEFT")
    else:
        for _ in range(dcols):
            print("RIGHT")

# Read input
m = int(input())
grid = []

for _ in range(m):
    grid.append(input().strip())

# Call the function to display the path
displayPathtoPrincess(m, grid)
