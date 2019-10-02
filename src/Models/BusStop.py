class BusStop:
    name = ''
    code = ''
    x = 0
    y = 0
    lines = []
    area = ''
    changeTime = 3

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def addLine(self, line):
        self.lines.append(line)
