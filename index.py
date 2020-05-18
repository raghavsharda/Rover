import numpy as np
import shapefile as shp
import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import product
from matplotlib.colors import ListedColormap



def findNeighbours(xCoordinate,yCoordinate,gridSize):
    xCoordinate = -73.59 
    yCoordinate =  45.49

    eastNeighbour=xCoordinate+gridSize*(1/100)
    westNeighbour=xCoordinate-(gridSize*(1/100))

    northNeighbour=yCoordinate+(gridSize*(1/100))
    southNeighbour=yCoordinate+(gridSize*(1/100))

    print("eastNeighbour",eastNeighbour,yCoordinate)
    print("westNeighbour",westNeighbour,yCoordinate)
    print("northNeighbour",xCoordinate,northNeighbour)
    print("southNeighbour",xCoordinate,southNeighbour)


def createBinnedCorodinates(xAxis, yAxis):

    for coordinate in product(xAxis, yAxis):
        print(coordinate)
        # print(type(coordinate))
        # print (round(coordinate[0], 3),", ",round(coordinate[1], 3))

def getGrid(X,Y,gridSize):
    crimaRates,xAxis,yAxis=np.histogram2d(X, Y, bins = gridSize) 
    threshold = np.percentile(crimaRates , 50)
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold,cmap=cmap22)
    crimaRates = np.transpose(crimaRates)[::-1]
    plt.title('TITLE', fontweight ="bold")
    createBinnedCorodinates(xAxis, yAxis)
    plt.show()

def getDataFromShapeFile():

    sf = shp.Reader(r'Shape\crime_dt.shp',encoding="ISO-8859-1")
    X = []
    Y = []
    for i in range(len(sf.shapes())):
        s = sf.shape(i)
        geoj = s.__geo_interface__
        x, y = geoj["coordinates"]
        X.append(round(x, 4))
        Y.append(round(y, 4))
        # X.append(x)
        # Y.append(y)

    return(X,Y)


def main():

    X,Y = getDataFromShapeFile()
    gridSize=2
    findNeighbours(-73.59 , 45.49 , gridSize )
    # getGrid(X,Y,gridSize)


if __name__ == '__main__':
    main()
