import numpy as np
import shapefile as shp
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from itertools import product
from matplotlib.colors import ListedColormap
from Graph import *

def createBinnedCorodinates(xAxis, yAxis):
    listofcoordinates=[]
    for coordinate in product(xAxis, yAxis):
        xydict = {'X':coordinate[0],'Y': coordinate[1]}
        listofcoordinates.append(xydict)
    return listofcoordinates

"""
This is called to generate first graph
Divided graphs into 2 to prevent crowding
"""
def createGridGraph(x,y,gridSize ,thresohold,xdistance,ydistance):
    crimeRates,xAxis,yAxis=np.histogram2d(x, y, bins = gridSize)
    # print(np.transpose(crimeRates)[::-1])
    threshold_percentile = np.percentile(crimeRates,thresohold)
    fig, ax = plt.subplots()
    plt.title('Montreal Crime Analytics', fontweight ="bold")
    plt.xticks(rotation=90)
    ax.set_xticks(xAxis)
    ax.set_yticks(yAxis)
    plt.xlabel("Latitudes")
    plt.ylabel("Longitudes")
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    ax.set_aspect("equal")
    hist, xbins, ybins, im = ax.hist2d(x,y, bins=gridSize,cmap=cmap22 , cmin=threshold_percentile)
    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            ax.text(xbins[j]+((xdistance/gridSize)/2),ybins[i]+((xdistance/gridSize)/2), hist.T[i,j], color="black", ha="center", va="center",fontsize=6.5)
    plt.show()
    return(crimeRates,xAxis,yAxis,threshold_percentile)

"""
This is called to generate second graph
Provides that final path that A* returns
"""
def createGridGraph2(X,Y,gridSize ,thresohold,res,touch):
    crimeRates,xAxis,yAxis=np.histogram2d(X, Y, bins = gridSize)
    print("Average " , np.average(crimeRates))
    print("Standard Deviation " , np.std(crimeRates))
    xAxis =np.around(xAxis,3)
    yAxis =np.around(yAxis,3)
    threshold_percentile = np.percentile(crimeRates,thresohold)
    print("Threshold Value " ,threshold_percentile)
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    cmap22 = mpl.colors.ListedColormap(['#D68910'])
    cmap22.set_under('#D68910',1)
    xyz = plt.hist2d(X,Y,bins=gridSize,cmin=threshold_percentile,cmap=cmap22)
    # crimeRates = np.transpose(crimeRates)[::-1] # for visual, to see crime rate.
    plt.title('Montreal Crime Analytics', fontweight ="bold")
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

    for y in touch:
        plt.scatter(y.xCoordinate, y.yCoordinate,marker = "+")
    
    plt.grid()
    plt.show()

"""
Get Data from shape file
Round till 4 for better calculations
"""
def getDataFromShapeFile():
    sf = shp.Reader(r'Shape\crime_dt.shp')
    X = []
    Y = []
    for i in range(len(sf.shapes())):
        s = sf.shape(i)
        geoj = s.__geo_interface__
        x, y = geoj["coordinates"]
        X.append(round(x, 4))
        Y.append(round(y, 4))

    return(X,Y)

def examples():
    s= """ 
         ===================================================================================
        |                                    Instructions                                   |
        |                                                                                   |
        | Enter cell size in the format '0.00X': 0.002                                      |
        | Enter the percentage threshold value in the format of 'XX': 50                    |
        | Enter Starting Point Coordinates in the format of '-XX.XXX,XX.XXX':-73.590,45.490 |
        | Enter Final Point Coordinates in the format of '-XX.XXX,XX.XX':-73.590,45.490     |  
        |                                                                                   |
         ===================================================================================
    """
    print(s)

def main():
    examples()
    
    gridSize = float(input("Enter cell size as per instructions and press enter:"))
    threshold = float(input("Enter the percenatge threshold value as per instructions and press enter':"))
    startingPoint = input("Enter Starting Point Coordinates as per instructions and press enter:")
    finalPoint = input("Enter Final Point Coordinates as per instructions and press enter:")
    gridSize=int(gridSize*10000)

    X,Y = getDataFromShapeFile()
    xdistance = max(X)-min(X)
    ydistance = max(Y)-min(Y)
    crimeRates,xAxis,yAxis,threshold_percentile=createGridGraph(X,Y,gridSize,threshold,xdistance,ydistance)
    listofcoordinates = createBinnedCorodinates(xAxis, yAxis)
    dictOfVertexObjects = createVertex(listofcoordinates,xdistance,ydistance,gridSize)
    makeFriends(dictOfVertexObjects)
    grid_vertex_edges = setHighCrimeAreas(crimeRates,dictOfVertexObjects,gridSize,threshold_percentile)
    vertexRef1,vertexRef2=findVertexForInputs(startingPoint,finalPoint,dictOfVertexObjects)
    # vertexKey1,vertexRef1,vertexKey2,vertexRef2 = searchVertexKeys(startingPoint,finalPoint,dictOfVertexObjects)
    tic = time.perf_counter()
    res,touch = astar(dictOfVertexObjects,grid_vertex_edges,vertexRef1,vertexRef2)
    toc = time.perf_counter()
    print(f"Time taken to find the path {toc - tic:0.4f} seconds")
    createGridGraph2(X,Y,gridSize,threshold,res,touch)
    print("Done")

if __name__ == '__main__':
    main()