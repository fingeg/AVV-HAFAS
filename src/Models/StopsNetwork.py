from src.Models.BusStop import BusStop

class StopsNetwork:
    stops = {}
    globalChangeTimes = {}

    def __init__(self):
        pass

    def addStop(self, code, names, operator, area):
        stop = BusStop(names, code, area, operator)
        self.stops[code] = stop
