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
    return(crimeRates,xAxis, yAxis,threshold_percentile)

def createGridGraph2(X,Y,gridSize ,thresohold,res):
    crimeRates,xAxis,yAxis=np.histogram2d(X, Y, bins = gridSize) 
    xAxis =np.around(xAxis,3)
    yAxis =np.around(yAxis,3)
    threshold_percentile = np.percentile(crimeRates,thresohold)
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold_percentile,cmap=cmap22)
    # crimeRates = np.transpose(crimeRates)[::-1] # for visual, to see crime rate.
    plt.title('TITLE', fontweight ="bold")
    # degrees = 70
    plt.xticks(rotation=90)
    ax.set_xticks(xAxis)
    ax.set_yticks(yAxis)
    plt.xlabel("Latitudes")
    plt.ylabel("Longitudes")
    xPlotList=[]
    yPlotList=[]
    i=0
    for l in res:
        xPlotList.append(res[i].xCoordinate)
        yPlotList.append(res[i].yCoordinate)
        i+=1

    plt.plot(xPlotList, yPlotList)
    plt.grid()
    plt.show()

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
    gridSize = 10
    threshold = 75
    # gridSize=val
    crimeRates,xAxis,yAxis,threshold_percentile=createGridGraph(X,Y,gridSize,threshold)
    listofcoordinates = createBinnedCorodinates(xAxis, yAxis)
    dictOfVertexObjects = createVertex(listofcoordinates,xdistance,ydistance,gridSize)
    makeFriends(dictOfVertexObjects)
    grid_vertex_edges = setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold_percentile)
    
    startingPoint = "-73.590,45.490"
    finalPoint = "-73.550,45.530"
    vertexKey1,vertexRef1,vertexKey2,vertexRef2 = searchVertexKeys(startingPoint,finalPoint,dictOfVertexObjects)
    res = astar(dictOfVertexObjects,grid_vertex_edges,vertexRef1,vertexRef2)
    print(res)
    createGridGraph2(X,Y,gridSize,threshold,res)
    print("break")

if __name__ == '__main__':
    main()