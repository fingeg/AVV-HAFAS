
class ParseLine:
    def __init__(self, network):
        self.network = network
        
    def bahnhof(self, attributes):
        code = attributes[0]
        operator = attributes[1].replace(',', '')
        names = ' '.join(attributes[2:]).split('$')
        area = attributes[-1].replace(',', '')
        self.network.addStop(code, names, operator, area)
    
    def bfkoord(self, attributes):
        if attributes[0].startswith('%'): return
        code = attributes[0]
        x = float(attributes[1])
        y = float(attributes[2])
        self.network.stops[code].setCoordinates(x, y)

        if self.network.field is None:
            self.network.field = [[x, x], [y, y]]
        else:
            self.network.field = [
                [
                    min(self.network.field[0][0], x),
                    max(self.network.field[0][1], x)
                ],
                [
                    min(self.network.field[1][0], y),
                    max(self.network.field[1][1], y)
                ]
            ]

    def umsteigb(self, attributes):
        codes = [attributes[0]]
        if codes[0] == '9999999':
            codes = self.network.stops.keys()
        for code in codes:
            changeTime = int(attributes[2])
            self.network.stops[code].changeTimes['normal'] = changeTime
    
    def umsteigv(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[3])
        v1 = attributes[1]
        v2 = attributes[2]
        isGlobal = code == '@@@@@@@'
        if not isGlobal:
            self.network.stops[code].changeTimes['operation']['%s:%s' % (v1, v2)] = changeTime
        else:
            for code in self.network.stops.keys():
                self.network.stops[code].changeTimes['operation']['%s:%s' % (v1, v2)] = changeTime
    
    def umsteigl(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[9])
        name = ':'.join(attributes[1:9])
        self.network.stops[code].changeTimes['line'][name] = changeTime
    
    def umsteigz(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[5])
        name = ':'.join(attributes[1:5])
        self.network.stops[code].changeTimes['track'][name] = changeTime

    def metabf(self, attributes):
        if attributes[0].startswith('%'): return
        if attributes[0].startswith('*'):
            # TODO: Implement the attributes, information, change and showing options
            pass
        elif attributes[0].endswith(':'):
            attributes[0] = attributes[0].replace(':', '')
            for code in attributes:
                stop = self.network.stops[code[-7:]]
                stop.stopsGroup = attributes.copy()
                del stop.stopsGroup[attributes.index(code)]
                if len(code) > 7:
                    stop.groupType = code[0]
        else:
            code1 = attributes[0]
            code2 = attributes[1]
            time = attributes[2]
            self.network.stops[code1].footPaths[code2] = time
            self.network.stops[code2].footPaths[code1] = time

    def bhfart(self, attributes):
        atrType = attributes[1]
        codes = [attributes[0]]
        if codes[0] == '@@@@@@@':
            codes = self.network.stops.keys()
        for code in codes:
            stop = self.network.stops[code]
            if atrType == 'B':
                selectingMode = '%03d' % int(bin(int(attributes[2])).replace('0b', ''))
                routingMode = '%03d' % int(bin(int(attributes[3])).replace('0b', ''))
                stop.selectingMode = [selectingMode[0] == '0', selectingMode[1] == '0', selectingMode[2] == '0']
                stop.routingMode = [routingMode[0] == '0', routingMode[1] == '0', routingMode[2] == '0']
        # TODO: Add all other attributes

    def bfprios(self, attributes):
        code = attributes[0]
        priority = attributes[1]
        self.network.stops[code].priority = int(priority)

    def bitfeld(self, attributes):
        code = attributes[0]
        timetable = ''
        for i in range(len(attributes[1])):
            rawDays = attributes[1][i]
            days = '%04d' % int(bin(int(rawDays, 16)).replace('0b', ''))
            timetable += days
        self.network.timetable[code] = timetable

    def line(self, attributes):
        if attributes[0].startswith('*Z'):
            pass