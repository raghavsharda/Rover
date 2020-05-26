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
    # fig, ax = plt.subplots()
    # ax.set_aspect("equal")
    # cmap22 = mpl.colors.ListedColormap(['#D68910'])
    # cmap22.set_under('#D68910',1)
    # xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold_percentile,cmap=cmap22)
    # # crimeRates = np.transpose(crimeRates)[::-1] # for visual, to see crime rate.
    # plt.title('TITLE', fontweight ="bold")
    # ax.set_xticks(xAxis)
    # ax.set_yticks(yAxis)
    # plt.xlabel("Latitudes")
    # plt.ylabel("Longitudes")
    
    # # how to plot lines
    # point1 = [xAxis[1], yAxis[1]]
    # point2 = [xAxis[4], yAxis[5]]
    # x_values = [point1[0], point2[0]]
    # y_values = [point1[1], point2[1]]
    # plt.plot(x_values, y_values)

    # plt.grid()

    # for i in range(len(yAxis)-1):
    #     for j in range(len(xAxis)-1):
    #         ax.text(xAxis[j]+0.5,yAxis[i]+0.5, crimeRates.T[i,j], color="red", ha="center", va="center", fontweight="bold")
    
    # plt.show()
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
    ax.set_xticks(xAxis)
    ax.set_yticks(yAxis)
    plt.xlabel("Latitudes")
    plt.ylabel("Longitudes")


    # how to plot lines
    # It works
    point11 = [xAxis[1], yAxis[1]]
    point22 = [xAxis[4], yAxis[5]]
    x_values = [point11[0], point22[0]]
    y_values = [point11[1], point22[1]]
    plt.plot(x_values, y_values)


    # It does not work
    # point1 = [res[1].xCoordinate, res[1].yCoordinate]
    # point2 = [res[3].xCoordinate, res[3].yCoordinate]
    # x1_values = [point1[0], point2[0]]
    # y1_values = [point1[1], point2[1]]
    # plt.plot(x1_values, y1_values)

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
    gridSize = 20
    threshold = 50
    # gridSize=val
    crimeRates,xAxis,yAxis,threshold_percentile=createGridGraph(X,Y,gridSize,threshold)
    listofcoordinates = createBinnedCorodinates(xAxis, yAxis)
    dictOfVertexObjects = createVertex(listofcoordinates,xdistance,ydistance,gridSize)
    makeFriends(dictOfVertexObjects)
    grid_vertex_edges = setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold_percentile)
    
    startingPoint = "-73.590,45.490"
    finalPoint = "-73.590,45.530"
    vertexKey1,vertexRef1,vertexKey2,vertexRef2 = searchVertexKeys(startingPoint,finalPoint,dictOfVertexObjects)
    res = astar(dictOfVertexObjects,grid_vertex_edges,vertexRef1,vertexRef2)
    createGridGraph2(X,Y,gridSize,threshold,res)
    print("break")

if __name__ == '__main__':
    main()