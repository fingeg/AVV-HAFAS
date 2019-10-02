class BusStop:

    def __init__(self, names, code, area, operator):
        # All names of this bus stop
        self.names = names

        # The code of this bus stop (7 letters)
        self.code = code

        # Coordinates of this bus stop (In degrees)
        self.x = 0
        self.y = 0

        # All bus lines which stops here
        self.lines = []

        # The operator and area of this bus stop
        self.operator = operator
        self.area = area

        # All types of change times that exists (keys: separated with ':'; values: time in minutes)
        self.changeTimes = {
            'normal': 3,
            'operation': {},
            'line': {},
            'track': {},
            'short': 1
        }

        # Describes to stops you can reach by walk (keys: code of aim; value: time in 'mmSss)
        self.footPaths = {}
        self.stopsGroup = []
        self.groupType = None

        # Describes when this stop can be used (As: start, aim and via)
        self.selectingMode = [True, True, True]  # [Start, Aim, Via]
        self.routingMode = [True, True, True]  # [Start, Aim, Via]


    def addLine(self, line):
        self.lines.append(line)

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y
