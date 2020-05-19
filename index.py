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
        xydict = {'X':round(coordinate[0],3),'Y':round(coordinate[1],3)}
        listofcoordinates.append(xydict)
    
    return listofcoordinates

def createGridGraph(X,Y,gridSize ,thresohold):
    crimaRates,xAxis,yAxis=np.histogram2d(X, Y, bins = gridSize) 
    threshold_percentile = np.percentile(crimaRates,thresohold)
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold_percentile,cmap=cmap22)
    crimaRates = np.transpose(crimaRates)[::-1]
    plt.title('TITLE', fontweight ="bold")
    plt.show()
    return(xAxis, yAxis)

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

    return(X,Y)

def main():
    # val = float(input("Enter cell size in in format 0.00F: "))
    # threshold = float(input("Enter threshold value Eg. 50% "))
    X,Y = getDataFromShapeFile()
    gridSize=2
    thresohold = 49 # meaning 50 percentile
    # gridSize=val
    xAxis,yAxis=createGridGraph(X,Y,gridSize,thresohold)
    listofcoordinates = createBinnedCorodinates(xAxis, yAxis)
    dictOfVertexObjects = createVertex(listofcoordinates)
    makeFriends(dictOfVertexObjects)

if __name__ == '__main__':
    main()
