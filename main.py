import sys
import math


def askContinue():
    answer = input('Add a new coordinate ? [Y/n] ')

    return answer != 'n'


def computeNewCoords(latitude, longitude, radius):
    # number of km per degree = ~111 km(111.32 in google maps, but range varies between 110.567 km at the equator and
    # 111.699 km at the poles) 1 km in degree = 1 / 111.32km = 0.0089 1m in degree = 0.0089 / 1000 = 0.0000089
    coef = radius * 0.0000089
    # Earth radius
    earth_radius = 6378137

    print('Latitudes:')
    print('    Min: ' + str(round(latitude - coef, 6)))
    print('    Max: ' + str(round(latitude + coef, 6)))

    # pi / 180 = 0.018
    print('Longitudes:')
    print('   Min: ' + str(
        round(
            float(
                longitude - 2 * ((radius / earth_radius * math.cos(math.pi * latitude / 180)) * (180 / math.pi))
            ),
            6)))
    print('   Max: ' + str(
        round(
            float(
                longitude + 2 * ((radius / earth_radius * math.cos(math.pi * latitude / 180)) * (180 / math.pi))
            ),
            6)))


continueLoop = True

separateCoordinatesInput = input('Do you want to use separate latitude and longitude or enter a geolocation string '
                                 '(ex: 1.234, 4.567) ? Choices are S(eparate) or T(ogether).'
                                 'Default is Together [s/T]: ')
separateCoordinates = separateCoordinatesInput == 's'

while continueLoop:
    if separateCoordinates:
        latitude = float(input('Enter latitude: '))
        longitude = float(input('Enter longitude: '))
    else:
        coordinates = input('Enter coordinates: ')
        latitude, longitude = coordinates.split(',')
        latitude = float(latitude.strip())
        longitude = float(longitude.strip())
    radius = int(input('Enter radius in meters: '))

    computeNewCoords(latitude, longitude, radius)

    continueLoop = askContinue()

print('Bye')
