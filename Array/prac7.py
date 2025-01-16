def solution(dirs):
    x, y = 0, 0
    paths = set()
    ways = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    for i in dirs:
        dx = x + ways[i][0]
        dy = y + ways[i][1]
        if ((-5 <= dx <= 5) and (-5 <= dy <= 5)):
            paths.add((x,y,dx,dy))
            paths.add((dx,dy,x,y))
            x, y = dx, dy
    return len(paths)//2
