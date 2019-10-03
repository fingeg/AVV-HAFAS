from src.Parser.lineTypes import ParseLine
from src.Parser.toOSM import parseToOSM
import os

def parse(directory, network):
    parser = ParseLine(network)

    parseFile(directory + '\\bahnhof', parser.bahnhof, 'bus stops')
    parseFile(directory + '\\bfkoord', parser.bfkoord, 'coordinates')
    parseFile(directory + '\\umsteigb', parser.umsteigb, 'change times')
    parseFile(directory + '\\umsteigv', parser.umsteigv, 'operation change times')
    parseFile(directory + '\\umsteigl', parser.umsteigl, 'line change times')
    parseFile(directory + '\\umsteigz', parser.umsteigz, 'track change times')
    parseFile(directory + '\\metabf', parser.metabf, 'footpaths')
    parseFile(directory + '\\bhfart', parser.bhfart, 'stops modes')
    parseFile(directory + '\\bfprios', parser.bfprios, 'stops priorities')
    parseFile(directory + '\\bitfeld', parser.bitfeld, 'timetables')

    #allFiles = os.listdir(directory)
    #for file in allFiles:
    #    if file.endswith('.LIN'):
    #        parseFile(directory + '\\' + file, parser.line, 'lines for line: ' + file.replace('.LIN', ''))

    print('Finished parsing')

    parseToOSM(network)

def parseFile(fileName, parser, log):
    file = open(fileName, 'r')
    lines = file.readlines()[1:]

    for line in lines:
        if line.startswith('*F'):
            continue
        attributes = ' '.join(line.split()).replace('\n', '').split(' ')
        parser(attributes)

    print('Found %d %s' % (len(lines), log))
