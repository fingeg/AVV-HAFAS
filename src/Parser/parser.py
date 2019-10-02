from src.Models.StopsNetwork import StopsNetwork
from src.Parser.lineTypes import ParseLine
stopsNetwork = StopsNetwork()

def parse(directory):
    parser = ParseLine(stopsNetwork)

    parseFile(directory + '\\bahnhof', parser.bahnhof, 'bus stops')
    parseFile(directory + '\\bfkoord', parser.bfkoord, 'coordinates')
    parseFile(directory + '\\umsteigb', parser.umsteigb, 'change times')
    parseFile(directory + '\\umsteigv', parser.umsteigv, 'operation change times')
    parseFile(directory + '\\umsteigl', parser.umsteigl, 'line change times')
    parseFile(directory + '\\umsteigz', parser.umsteigz, 'track change times')
    parseFile(directory + '\\metabf', parser.metabf, 'footpaths')
    print('Finished parsing')

def parseFile(fileName, parser, log):
    file = open(fileName, 'r')
    lines = file.readlines()[1:]

    for line in lines:
        if line.startswith('*F'):
            continue
        attributes = ' '.join(line.split()).replace('\n', '').split(' ')
        parser(attributes)

    print('Found %d %s' % (len(lines), log))
