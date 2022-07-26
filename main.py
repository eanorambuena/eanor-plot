from engine import *

n, m = 20, 64 # Max = 20, 64
large = 20
bgcolor = red

matrix = []
for i in range(n):
    r = []
    for j in range(m):
        r.append(bgcolor)
    matrix.append(r)

N, M, L = large, n, m

space = []
for i in range(N):
    r = []
    for j in range(M):
        rr = []
        for k in range(L):
            rr.append(bgcolor)
        r.append(rr)
    space.append(r)

screen = Image()
p = Point(space, color = blue, bgcolor = green)
p.vx, p.vy = 1, 1

FPS = 1

for i in range(1):

    move(p, space, 1)

    P = identity(m)
    R = P
    T = P
    S = space[p.z]
    proy = dot(P, dot(R, dot(T, S)))

    screen.loadFromRGB(proy)
    screen.printRGB()
    sleep(1000 / FPS)
