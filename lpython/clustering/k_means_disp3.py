### This program finds unusual points by deviding input points into clusters.
### To play with the program, change following variables:
#number_of_cluster
#max_number_of_points_noise_cluster
#a 
 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import sklearn.cluster as cluster
from collections import Counter # needed  to count the result of clustering 
import time
###Parameters
number_of_cluster=3 
max_number_of_points_noise_cluster=1 ## max number of points in the clutser that is unusual. 


####Helper Function 2 	
from operator import itemgetter
import heapq
import collections
def least_common_values(array, to_find=None):
    counter = collections.Counter(array)
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))	
###################################################################	
#sns.set_context('poster')
#sns.set_color_codes()

f = open('input.txt')

a = []

j= 0
for line in f.readlines():
	print("Line = ",line)
	tmp = [0.0,0.0,0.0]
	k = 0
	for value, t in enumerate(line.split()):
		tmp[k] = float(t)
		k = k + 1
	a.append(tmp)
	j = j + 1
print("rows=",j)
print("a=",a)	
		
###############################
A = np.array(a)
print("shape =", A.shape)

k_means = cluster.KMeans(n_clusters=number_of_cluster)
print("Clustered\n")
k_means.fit(A)
print(k_means.labels_)

#noise_clusters = Counter(k_means.labels_).least_common(max_number_of_points_noise_cluster)
noise_clusters = least_common_values(k_means.labels_,max_number_of_points_noise_cluster)

#indices = [] 
noise_points = []
for k, v in noise_clusters:
	#noise_points.append(a[(k_means.labels_).index(k)])
	#print("noise p=",a[k_means.labels_.index(k)])
	indexes = [i for i,x in enumerate(k_means.labels_) if x == k]
	for i in indexes:
		noise_points.append(a[i])
B = np.array(noise_points) 

print("Noise = ", noise_points)	
#### Separate normal points 
A1 = np.setdiff1d(A, B).view(A.dtype).reshape(-1, A.shape[1])
print("A",A)
print("A1",A1)
###display 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



#ax.scatter(A[:,0], A[:,1], A[:,2])
ax.scatter(A1[:,0], A1[:,1], A1[:,2])

ax.scatter(B[:,0], B[:,1], B[:,2],c='r')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

