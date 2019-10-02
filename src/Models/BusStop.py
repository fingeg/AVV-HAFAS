class BusStop:

    def __init__(self, names, code, area, operator):
        self.names = names
        self.code = code
        self.x = 0
        self.y = 0
        self.lines = []
        self.operator = operator
        self.area = area
        self.changeTimes = {
            'normal': 3,
            'operation': {},
            'line': {},
            'track': {},
            'short': 1
        }
        self.footPaths = {}
        self.stopsGroup = []
        self.groupType = ''

    def addLine(self, line):
        self.lines.append(line)

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y
