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
        # print(coordinate)
        # print(type(coordinate))
        print (round(coordinate[0], 3),", ",round(coordinate[1], 3))

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
    getGrid(X,Y,gridSize)


if __name__ == '__main__':
    main()



















# np.fliplr(crimaRates)
# print(crimaRates)
# print("@@@@@@@\n@@@@@@@@")
# np.transpose(np.flip(crimaRates))
# print("@@@@@@@\n@@@@@@@@")
# print(np.flip(crimaRates))
# plt.show()


    # crimaRates , xAxis, yAxis = np.histogram2d(X, Y, bins = 20)
    # createBinnedCorodinates(xAxis, yAxis)
    # crimeRateMedian = np.median(crimaRates)
    # threshold = np.percentile(crimaRates , 50)
    # cmap22 = mpl.colors.ListedColormap(['#D68910'])
    # cmap22.set_under('#D68910',1)
    # xyz = plt.hist2d(X,Y,bins = 20,cmin=threshold , cmap = cmap22)
    # crimaRates = np.transpose(crimaRates)[::-1]
    # plt.title('TITLE', fontweight ="bold")
    # plt.show()
    # gridSize = 3






# shape=gpd.read_file(r'C:\Users\Raghav\Desktop\Projects\AI_Assignment-1\Shape\crime_dt.shp')
# shape.plot()

# feature = sf.shapeRecords()[0]
# first = sf.shape.__geo_interface__  
# print(first) # (GeoJSON format)

# s = sf.shape(0)
# geoj = s.__geo_interface__
# print(geoj)
# print(geoj["coordinates"])

# x1 = [-1,-1,10,10,-1]; y1 = [-1,10,10,-1,-1]
# x2 = [21,21,29,29,21]; y2 = [21,29,29,21,21]
# shapes = [[x1,y1],[x2,y2]]
# for shape in shapes:
#   x,y = shape
#   plt.plot(x,y)
# plt.show()

# X = []
# Y = []
# for i in range(len(sf.shapes())):
#     s = sf.shape(i)
#     geoj = s.__geo_interface__
#     x, y = geoj["coordinates"]
#     X.append(x)
#     Y.append(y)

# gridSize = 3
# crimaRates , xAxis, yAxis = np.histogram2d(X, Y, bins = gridSize) 
# crimeRateMedian = np.median(crimaRates)
# xyz = plt.hist2d(X,Y,bins=gridSize,cmin=crimeRateMedian)
# plt.show()


#     print(type(x), type(y))
# print(X)
# print(Y)
# plt.figure(facecolor="w")





# plt.hist2d(X, Y, 
#            bins = 20,  
#            norm = color.LogNorm(),
#            cmap ="viridis") 

# xyz = plt.hist2d(X,Y,bins=2,cmax=4285) 
# gridSize = 2
# calculate threshold

# xyz = plt.hist2d(X,Y,bins=gridSize,cmax=4285)
# print("plt" , xyz)
# plt.show()

# gridSize = 3
# crimaRates , xAxis, yAxis = np.histogram2d(X, Y, bins = gridSize) 
# crimeRateMedian = np.median(crimaRates)
# xyz = plt.hist2d(X,Y,bins=gridSize,cmin=crimeRateMedian)
# plt.show()


# abc = np.histogram2d(X, Y, bins = gridSize) 
# print("plt" , abc)
# print("np", xyz)




# ax = plt.gca()
# ax.set_facecolor('white')
# plt.show()















# # sum = 0
# gridSize = 3
# crimaRates , xAxis, yAxis = np.histogram2d(X, Y, bins = gridSize) 
# crimeRateMedian = np.median(crimaRates)
# print(crimeRateMedian)

# print(xAxis)
# print(yAxis)


# for i in range(len(abc[0][0])):
#     print(abc[0][i])
#     sum += np.sum(abc[0][i])

# print("Average is ", sum/(gridSize*gridSize))
# print("Mean is ", np.mean(X) , np.mean(Y))
# print("SD is ", np.std(X) ,np.std(Y))


# for i in range(len(abc[1])):
#     for j in range(len(abc[2]))



# print (sf)
# print (sf.shapeType)
# print (sf.shapeTypeName)
# print (sf.bbox)
# # print (sf.shapes())
# print(len(sf.shapes()))


# s = sf.shape(7)
# # ['%.3f' % coord for coord in sf.bbox]
# print(['%.3f' % coord for coord in sf.bbox])


# print(sf.fields)
# records = sf.records()
# print(records)

# sf.fields
# print(len(sf[3].points))


# shapeRecs = sf.shapeRecords()