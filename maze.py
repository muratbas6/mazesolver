import matplotlib.pyplot as plt
import numpy as np


grid = np.array([[0,0,0,1,2],
                 [0,1,1,1,0],
                 [0,0,0,0,0],
                 [0,1,0,1,1],
                 [3,1,0,0,0]])


def search(x, y):
    if grid[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False

    print ('visiting %d,%d' % (x, y))


    grid[x][y] = 3

    if ((x < len(grid) - 1 and search(x + 1, y))
        or (y > 0 and search(x, y - 1))
        or (x > 0 and search(x - 1, y))
        or (y < len(grid) - 1 and search(x, y + 1))):
        return True

    return False


search(0, 0)


fig = plt.figure()
ax = fig.add_subplot(111,aspect = 'auto')
x1,x2,y1,y2 = plt.axis()
plt.axis((0,5,0,5))
plt.imshow(grid,extent=[0,5,0,5])
plt.show()