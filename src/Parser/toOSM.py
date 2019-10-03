
def parseToOSM(network):
    fileContent = '<?xml version="1.0" encoding="UTF-8"?>\n \
        <osm version="0.6" generator="CGImap 0.0.2"> \
        <bounds minlat="%f" minlon="%f" maxlat="%f" maxlon="%f"/>\n' % \
                  (network.field[1][0], network.field[0][0], network.field[1][1], network.field[0][1])

    # Add all bus stops
    for code in network.stops.keys():
        stop = network.stops[code]
        fileContent += '\t<node id="0%s" lat="%f" lon="%f" version="1" changeset="203496"' \
                       ' user="80n" uid="1238" visible="true" timestamp="2019-10-02T11:40:26Z">\n' \
                       '\t\t<tag k="%s" v="bus_stop"/>\n' \
                       '\t</node>\n' % \
                       (stop.code, stop.y, stop.x, stop.names[0])

    # Add all foot paths
    for code in network.stops.keys():
        stop = network.stops[code]
        for footPath in stop.footPaths.keys():

            fileContent += '\t<way id="%s%s" version="1" changeset="203496"' \
                           ' user="80n" uid="1238" visible="true" timestamp="2019-10-02T11:40:26Z">\n' \
                           '\t\t<nd ref="0%s"/>\n' \
                           '\t\t<nd ref="0%s"/>\n' \
                           '\t\t<tag k="%s" v="foot_way"/>\n' \
                           '\t</way>\n' % \
                           (footPath[-4:], stop.code[-4:], footPath, stop.code, stop.names[0])

    fileContent += '</osm>'
    file = open('busStops.osm', 'w')
    file.write(fileContent)
    file.close()
