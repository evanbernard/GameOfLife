import pygame,sys,os

pygame.init()
screen = pygame.display.set_mode((1500,1120))
color = (255,255,255)

#two dimensional array
grid = []
for row in range(52):
	grid.append([])
	for column in range(36):
		grid[row].append(0)
#end two dimensional array
neighbour = []
for row in range(51):
	neighbour.append([])
	for column in range(35):
		neighbour[row].append(0)
		
def draw(grid,color):
	for u in range (0,35):
		for i in range (0,51):
			color = (255,255,255)
			if grid[i][u]==1:
				color = (50,100,150)
			pygame.draw.rect(screen, color, (1+30*i,1+ 30*u,28,28))


def main(grid,color,neighbour):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:		
				pygame.quit()
				sys.exit()
			#detect mouse click
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row = pos[1] // (30)
				column = pos[0] // (30)
				if row <=34 and column <= 50:
					grid[column][row] = 1
					#print("Click ", pos, "Grid coordinates: ", row, column)
					color = (50,100,150)
					pygame.draw.rect(screen, color, (1+30*column,1+ 30*row,28,28))
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					start(grid,color,neighbour)
			pygame.display.update()
			
def start(grid,color,neighbour):
	for u in range (0,35):
		for i in range (0,51):
			neighbour[i][u] = 0
			#get number of neighbours	
			#if grid[i][u] == 1:
			if grid[i-1][u] == 1:
				neighbour[i][u]+=1
			if grid[i+1][u] == 1:
				neighbour[i][u]+=1
			if grid[i][u-1] == 1:
				neighbour[i][u]+=1
			if grid[i][u+1] == 1:
				neighbour[i][u]+=1
			if grid[i-1][u-1] == 1:
				neighbour[i][u]+=1
			if grid[i+1][u+1] == 1:
				neighbour[i][u]+=1
			if grid[i-1][u+1] == 1:
				neighbour[i][u]+=1
			if grid[i+1][u-1] == 1:
				neighbour[i][u]+=1
			#print("row "+str(u)+" col "+str(i)+" "+str(neighbour[i][u]))	
			if neighbour[i][u] < 2:
				pygame.draw.rect(screen, (255,255,255), (1+30*i,1+ 30*u,28,28))
			if neighbour[i][u] > 3:
				pygame.draw.rect(screen, (255,255,255), (1+30*i,1+ 30*u,28,28))
			if neighbour[i][u] == 3:
				pygame.draw.rect(screen, (50,100,150), (1+30*i,1+ 30*u,28,28))
	for u in range (0,35):
		for i in range (0,51):			
			if neighbour[i][u] < 2 or neighbour[i][u] > 3:	
				grid[i][u] = 0	
			if neighbour[i][u] == 3:
				grid[i][u] = 1
			
draw(grid,color)		
main(grid,color,neighbour)
