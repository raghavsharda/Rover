import numpy as np
import shapefile as shp
import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import product
from matplotlib.colors import ListedColormap
from sklearn.feature_extraction import DictVectorizer
from Graph import *

def createBinnedCorodinates(xAxis, yAxis):
    listofcoordinates=[]
    for coordinate in product(xAxis, yAxis):
        xydict = {'X':coordinate[0],'Y': coordinate[1]}
        listofcoordinates.append(xydict)
    print(len(listofcoordinates))
    return listofcoordinates

def createGridGraph(X,Y,gridSize ,thresohold):
    crimeRates,xAxis,yAxis=np.histogram2d(X, Y, bins = gridSize) 
    threshold_percentile = np.percentile(crimeRates,thresohold)
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold_percentile,cmap=cmap22)
    # crimeRates = np.transpose(crimeRates)[::-1] # for visual, to see crime rate.
    plt.title('TITLE', fontweight ="bold")
    plt.show()
    return(crimeRates,xAxis, yAxis,threshold_percentile)

def getDataFromShapeFile():
    sf = shp.Reader(r'Shape\crime_dt.shp')
    X = []
    Y = []
    for i in range(len(sf.shapes())):
        s = sf.shape(i)
        geoj = s.__geo_interface__
        x, y = geoj["coordinates"]
        X.append(round(x, 3))
        Y.append(round(y, 3))

    return(X,Y)

def main():
    # gridSize = float(input("Enter cell size in in format 0.00F: "))
    # threshold = float(input("Enter threshold value Eg. 30% "))
    X,Y = getDataFromShapeFile()
    xdistance = max(X)-min(X)
    ydistance = max(Y)-min(Y)
    # Setting hard values for testing
    gridSize = 2
    threshold = 50
    # gridSize=val
    crimeRates,xAxis,yAxis,threshold_percentile=createGridGraph(X,Y,gridSize,threshold)
    listofcoordinates = createBinnedCorodinates(xAxis, yAxis)
    dictOfVertexObjects = createVertex(listofcoordinates,xdistance,ydistance,gridSize)
    makeFriends(dictOfVertexObjects)
    grid_vertex_edges = setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold_percentile)
    print("break")

if __name__ == '__main__':
    main()
