# 2D grid: a list where EACH element IS another list

number_grid = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])


# nested list -> for loop in loop
for row in number_grid:
    for col in row:
        print(col)
        