
# declaring maze size
N = 4

def print_solution(sol):
    """

    :param sol: final solution
    :return: None
    """
    for i in sol:
        print(i)

def isSafe(maze,x,y):
    """

    :param maze: input maze
    :param x: position in x axis
    :param y: position in y axis
    :return: checks whether there is a possible step in maze or not
    """
    if x>=0 and x<N and y>=0 and y<N and maze[x][y] == 1:
        return True
    return False


def solveMaze(maze):
    """

    :param maze: input maze
    :return: None
    """


    # form a empty matrix of NxN
    sol = [[0 for i in range(N)]for i in range(N)]


    if solveMazeUntillEnd(maze,0,0,sol) == False :
        print("solution doesnt exist")

    print_solution(sol)

def solveMazeUntillEnd(maze, x, y, sol):
    """

    :param maze: input maze that is to be solved
    :param x: position in x axis
    :param y: position in y axis
    :param sol: solution matrix
    :return: True or False
    """
    if x==N-1 and y==N-1:
        sol[x][y]=1
        return True
    if isSafe(maze,x,y)==True:
        sol[x][y]=1

        # going in horizontal direction
        if solveMazeUntillEnd(maze,x+1,y,sol):
            return True

        #going in vertical direction
        if solveMazeUntillEnd(maze,x,y+1,sol):
            return True

        sol[x][y]=0
        return False

if __name__=="__main__":

    maze = [[1,1,0,0],
            [1,1,1,0],
            [0,0,1,1],
            [0,1,0,1]]
    solveMaze(maze)



