import numpy as np

def to_xyz(cell_index):
    return [(0, 0, 0), (1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1), (2, -2, 0), (2, -1, -1),
            (2, 0, -2), (1, 1, -2), (0, 2, -2), (-1, 2, -1), (-2, 2, 0), (-2, 1, 1), (-2, 0, 2), (-1, -1, 2),
            (0, -2, 2), (1, -2, 1), (3, -3, 0), (3, -2, -1), (3, -1, -2), (3, 0, -3), (2, 1, -3), (1, 2, -3),
            (0, 3, -3),
            (-1, 3, -2), (-2, 3, -1), (-3, 3, 0), (-3, 2, 1), (-3, 1, 2), (-3, 0, 3), (-2, -1, 3), (-1, -2, 3),
            (0, -3, 3), (1, -3, 2), (2, -3, 1)][cell_index]

def from_xyz(x, y, z):
    return {(0, 0, 0): 0, (1, -1, 0): 1, (1, 0, -1): 2, (0, 1, -1): 3, (-1, 1, 0): 4, (-1, 0, 1): 5, (0, -1, 1): 6,
            (2, -2, 0): 7, (2, -1, -1): 8, (2, 0, -2): 9, (1, 1, -2): 10, (0, 2, -2): 11, (-1, 2, -1): 12,
            (-2, 2, 0): 13,
            (-2, 1, 1): 14, (-2, 0, 2): 15, (-1, -1, 2): 16, (0, -2, 2): 17, (1, -2, 1): 18, (3, -3, 0): 19,
            (3, -2, -1): 20,
            (3, -1, -2): 21, (3, 0, -3): 22, (2, 1, -3): 23, (1, 2, -3): 24, (0, 3, -3): 25, (-1, 3, -2): 26,
            (-2, 3, -1): 27,
            (-3, 3, 0): 28, (-3, 2, 1): 29, (-3, 1, 2): 30, (-3, 0, 3): 31, (-2, -1, 3): 32, (-1, -2, 3): 33,
            (0, -3, 3): 34,
            (1, -3, 2): 35, (2, -3, 1): 36}[(x, y, z)]


def get_shadowed_squares(cell_index,x,y,z,size):
    shadowed_squares = []
    x_c,y_c,z_c = to_xyz(cell_index)
    for _ in range(size):
        x_c += x
        y_c += y
        z_c += z
        if max(abs(x_c),abs(y_c),abs(z_c))<=3:
            shadowed_squares.append(from_xyz(x_c,y_c,z_c))
    return shadowed_squares

def a(arr):
    arr[0]=0

if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(l)
    a = l.pop(-1)
    print(l)