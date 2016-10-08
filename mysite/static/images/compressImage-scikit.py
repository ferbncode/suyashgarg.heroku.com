from loadImage import loadFromFile, return2dImageMatrix
import numpy as np
import random as rd
import os

def randomInitialize(X, K):
    """randomly initialize few datapoints as points for 
    centroids for applying the kmeans algorithm"""
    a,b = X.shape
    randIndexes = np.random.randint(a, size=K)
    return X[randIndexes,:]

def findClosestCentroid(X, centroids):
    """find the closest centroids and and return the 
    centroid index number in an array"""
    K,n = centroids.shape
    # Now n has the no of features and K has the no of clusters.
    closestCentroidNo = np.zeros(len(X))
    noOfDataPoints = len(X)
    for i in range(noOfDataPoints):
        dataPoint = X[i];
        queryMat = np.tile(dataPoint, (K,1))
        squared_distance = np.square(centroids - queryMat).sum(1)
        min_squared_distance = min(squared_distance)
        indexOfMinElement = np.where(squared_distance == min_squared_distance)[0][0]
        closestCentroidNo[i] = indexOfMinElement
        # this gets kind of depenent issue
    return closestCentroidNo



def computeCentroids(X, closestCentroidNo, K):
    """Function computing the centroid locations again 
    to shift the position of the new centroid"""
    m,n = X.shape
    centroids = np.zeros((K,n))
    for i in range(K):
        indices = (closestCentroidNo == i)
        for j in range(n):
            if(indices.mean()!=0):
                centroids[i,j] = sum(X[:,j]*indices)/((indices.mean())*len(indices))
    return centroids
    
count = 0
for dir in ['.']:
    for ImgName in os.listdir('.'):
        a = ImgName
        a =  a.split('.')[0]
        if(a.isdigit()):
            Imgarray = loadFromFile(ImgName)
            a,b,c = Imgarray.shape
            TwoDarray = return2dImageMatrix(Imgarray).transpose()
            # I know this is shit code.
            K = 2

            from sklearn.cluster import KMeans

            clusterer = KMeans(n_clusters = K, max_iter=50, random_state=1)
            preds = clusterer.fit_predict(TwoDarray)

            #A = randomInitialize(TwoDarray,K)
        #max_iter = 100
        #for iter in range(max_iter):
        #   print "Started with iteration " + str(iter)
        #   closestCentroidNo = findClosestCentroid(TwoDarray,A)
        #   centroids = computeCentroids(TwoDarray, closestCentroidNo, K)
        #   print "Done with iteration " + str(iter) 
            primary_colors = [[ 170.15613748 ,181.99356247, 174.73522459],[  90.46210046,  123.38912947,  110.00291648]]

            for iter in range(len(TwoDarray)):
                TwoDarray[iter] = clusterer.cluster_centers_[preds[iter]]
        #print clusterer.cluster_centers_
        #print "The centroids are"
        #for centroid in centroids:
        #   print centroid
            TwoDarray = np.fliplr(TwoDarray)
            ThreeD = TwoDarray.reshape(a,b,c)
            import Image
            Im = Image.fromarray(ThreeD)
            count += 1
            Im.save("A{}.png".format(count))




