import random
from time import sleep

width = 135
height = 32

def show_screen(screen):
    print(''.join(''.join(['█' if cell else ' ' for cell in row]) for row in screen))

screen = [[random.choice([True, False]) for _ in range(width)] for _ in range(height)]

while True:
    new_screen = [row[:] for row in screen]
    for i in range(height):
        for j in range(width):
            alive_neighbors = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not (k == 0 and l == 0):
                        ni, nj = i + k, j + l
                        if 0 <= ni < height and 0 <= nj < width:
                            if screen[ni][nj]:
                                alive_neighbors += 1

            if screen[i][j] and alive_neighbors in [2, 3]:
                new_screen[i][j] = True
            elif not screen[i][j] and alive_neighbors == 3:
                new_screen[i][j] = True
            else:
                new_screen[i][j] = False

    show_screen(new_screen)
    screen = new_screen
    sleep(0.1)
# print('#'*135*32)