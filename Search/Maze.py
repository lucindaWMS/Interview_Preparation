#DFS solve Maze

import math

min_step = math.inf 

def dfs(start_x, start_y, end_x, end_y, maze, step):


	next_step = [[0, 1], #go right
				[0, -1], #go left
				[1, 0],  #go down
				[-1, 0]] #go up

	if start_x == end_x and start_y == end_y:
		global min_step
		if step < min_step:
			min_step = step
		return

	for i in range(len(next_step)):
		next_x = start_x + next_step[i][0]
		next_y = start_y + next_step[i][1]

		if (next_x < 0) or (next_y < 0) or (next_x >= len(maze)) or (next_y >= len(maze[0])):
			continue
		if (maze[next_x][next_y] == 0) and (book[next_x][next_y] == 0):
			book[next_x][next_y] = 1
			dfs(next_x, next_y, end_x, end_y, maze, step+1)
			book[next_x][next_y] = 0
	return

if __name__ == '__main__':
	start_x = 0
	start_y = 0
	end_x = 3
	end_y = 2
	maze = [[0, 0, 1, 0],
			[0, 0, 0, 0],
			[0, 0, 1, 0],
			[0, 1, 0, 0],
			[0, 0, 0, 1]]
	book = []
	for i in range(len(maze)):
		book.append([0] * len(maze[0]))
	book[start_x][start_y] = 1
	dfs(start_x, start_y, end_x, end_y, maze, 0)
	print(min_step)
