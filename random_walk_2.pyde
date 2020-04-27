pix = 10
stack = []
covered = []
direction = [[pix, 0], [-pix, 0], [0, pix], [0, -pix]]
pos = []
r = 255
g = 150
b = 150
cobj = {
    'r': 'h',
    'g': 'i',
    'b': 'h'
}


class Dot:

    def __init__(self, pos, r, g, b, cobj):
        self.pos = pos
        self.r = r
        self.g = g
        self.b = b
        self.cobj = cobj

def setup():
    global pos, r, g, b, cobj, pix
    size(800, 600)

    background(51)
    pos = [pix * int(random(width // pix)), pix * int(random(height // pix))]
    stack.append(Dot(pos, r, g, b, cobj))
    covered.append(pos)
    fill(r, g, b)
    noStroke()
    rect(pos[0], pos[1], pix, pix)

def draw():
    global stack, r, g, b, cobj, pix

    if len(stack) != 0:
        crnt = stack[len(stack) - 1].pos
        r = stack[len(stack) - 1].r
        g = stack[len(stack) - 1].g
        b = stack[len(stack) - 1].b
        cobj = stack[len(stack) - 1].cobj

        if cobj['r'] == 'i':
            if r < 255:
                r += 1
            else:
                cobj['r'] = 'h'
                cobj['b'] = 'd'
        elif cobj['r'] == 'd':
            if r > 150:
                r -= 1
            else:
                cobj['r'] = 'h'
                cobj['b'] = 'i'
        elif cobj['g'] == 'i':
            if g < 255:
                g += 1
            else:
                cobj['r'] = 'd'
                cobj['g'] = 'h'
        elif cobj['g'] == 'd':
            if g > 150:
                g -= 1
            else:
                cobj['g'] = 'h'
                cobj['r'] = 'i'
        elif cobj['b'] == 'i':
            if b < 255:
                b += 1
            else:
                cobj['b'] = 'h'
                cobj['g'] = 'd'
        elif cobj['b'] == 'd':
            if b > 150:
                b -= 1
            else:
                cobj['b'] = 'h'
                cobj['g'] = 'i'

        adj = get_adj(crnt)
        if adj != None:
            stack.append(Dot(adj, r, g, b, cobj))
            covered.append(adj)
            fill(r, g, b)
            rect(adj[0], adj[1], pix, pix)
        else:
            stack.pop()
    else:
        save('maze.jpg')
        print('done')
        noLoop()


def get_adj(current):
    global direction, covered, pix
    adj = []
    for dir in direction:
        x = current[0] + dir[0]
        y = current[1] + dir[1]

        if x >= 0 and y >= 0 and x <= width - pix and y <= height - pix and [x, y] not in covered:
            adj.append([x, y])
    if len(adj) != 0:
        return adj[int(random(len(adj)))]
    else:
        return None
