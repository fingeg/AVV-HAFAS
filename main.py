#!/usr/bin/python

from src.Parser import parser

print('Starting AVV routing scripts...')

dataDir = 'C:\\Users\\Finn\\Documents\\Projekte\\AVV\\AVV_HAFAS_540\\Datenpool\\OpenData\\AVV_HAFAS_540'
parser.parse(dataDir)
