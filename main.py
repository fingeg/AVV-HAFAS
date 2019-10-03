#!/usr/bin/python
from src.Models.Network import Network
from src.Parser import parser
from src.GUI import Main

print('Starting AVV routing scripts...')

network = Network()

dataDir = 'C:\\Users\\Finn\\Documents\\Projekte\\AVV\\AVV_HAFAS_540\\Datenpool\\OpenData\\AVV_HAFAS_540'
parser.parse(dataDir, network)

gui = Main.GUI(network)
gui.run()

