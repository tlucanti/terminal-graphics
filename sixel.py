
import numpy as np

def preamble(width, height):
    DCS = '\033Pq"'

    out = ''
    out += f'{DCS}1;1;{width};{height * 8}'
    return out

def set_colors():
    out = ''
    return out


def epilogue():
    return '\033\\'

def put_pixel_next(c):
    out = ''
    out += f'#{c}.~'
    return out

def put(r, g, b):
    out = ''
    out += f'#1;2;{r};{g};{b}'
    out += f'#1.~'
    return out

def put_newline():
    return '$-'

def draw(array):
    c = 0
    out = ''
    h, w = array.shape

    out += preamble(h, w)
    out += set_colors()

    for y in range(h):
        for x in range(w):
            c += 1
            if array[y][x] == 1:
                if c % 2 == 0:
                    out += put(0, 0, 0)
                else:
                    out += put(99, 0, 99)
            else:
                out += put(0, 0, 99)
        out += put_newline()

    out += epilogue()

    print(end=out)

def main():
    x = 121
    y = x
    a = np.ones((x, y), dtype=np.uint8)
    a[1:x-1,1:y - 1] = 0

    #print(a)
    draw(a)

if __name__ == '__main__':
    main()


