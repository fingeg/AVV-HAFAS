
class ParseLine:
    def __init__(self, stopsNetwork):
        self.stopsNetwork = stopsNetwork
        
    def bahnhof(self, attributes):
        code = attributes[0]
        operator = attributes[1].replace(',', '')
        names = ' '.join(attributes[2:]).split('$')
        area = attributes[-1].replace(',', '')
        self.stopsNetwork.addStop(code, names, operator, area)
    
    def bfkoord(self, attributes):
        if attributes[0].startswith('%'): return
        code = attributes[0]
        x = float(attributes[1])
        y = float(attributes[2])
        self.stopsNetwork.stops[code].setCoordinates(x, y)

    def umsteigb(self, attributes):
        code = attributes[0]
        if not code == '9999999':
            changeTime = int(attributes[2])
            self.stopsNetwork.stops[code].changeTimes['normal'] = changeTime
    
    def umsteigv(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[3])
        v1 = attributes[1]
        v2 = attributes[2]
        isGlobal = code == '@@@@@@@'
        if not isGlobal:
            self.stopsNetwork.stops[code].changeTimes['operation']['%s:%s' % (v1, v2)] = changeTime
        else:
            self.stopsNetwork.globalChangeTimes['%s:%s' % (v1, v2)] = changeTime
    
    def umsteigl(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[9])
        name = ':'.join(attributes[1:9])
        self.stopsNetwork.stops[code].changeTimes['line'][name] = changeTime
    
    def umsteigz(self, attributes):
        code = attributes[0]
        changeTime = int(attributes[5])
        name = ':'.join(attributes[1:5])
        self.stopsNetwork.stops[code].changeTimes['track'][name] = changeTime

    def metabf(self, attributes):
        if attributes[0].startswith('%'): return
        if attributes[0].startswith('*'):
            # TODO: Implement the attributes, information, change and showing options
            pass
        elif attributes[0].endswith(':'):
            attributes[0] = attributes[0].replace(':', '')
            for code in attributes:
                stop = self.stopsNetwork.stops[code[-7:]]
                stop.stopsGroup = attributes.copy()
                del stop.stopsGroup[attributes.index(code)]
                if len(code) > 7:
                    stop.groupType = code[0]
        else:
            code1 = attributes[0]
            code2 = attributes[1]
            time = attributes[2]
            self.stopsNetwork.stops[code1].footPaths[code2] = time
            self.stopsNetwork.stops[code2].footPaths[code1] = time




