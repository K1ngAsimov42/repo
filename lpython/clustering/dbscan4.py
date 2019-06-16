### This program finds unusual points by deviding input points into clusters.
### To play with the program, change following variables:
#min_dist_between_cluster
#min_sample_around_a_sample
#
# Noise is shown in black
#### change log
# 3/01/2017   #  Creation     # 
# 3/02/2017   #  Creation     # 'alpha' is added for (trasparency) in scatter call. 'marker' argument is added
# 3/02/2017   # added abilitty to see projection on yz and zx planes,
# comments:  
## Performance:
#Number of points(M)# esp     #min_samples   # time        #memory                     #comment
#                   #         #              #             #                           #
# .4594M            # 100     #10            # too long    #apparently out of memory   #Try metric='precomputed'
# .459M             # 10      #10            # 24          #OK                         # 13 clusters
# .919M             # 10      #10            # 52          #OK                         # 17 clusters
# 1.83              # 10      #10            # 146         #OK                         # 42 clusters
# 1.83              # 10      #20            # 143         #OK                         # 15 clusters
# 1.83              # 10      #25            # 94          #OK                         # 432 clusters
# 1.83              # 05      #25            #             #OK                         # 432
# 1.83              # 10      #5             # 134         #OK                         # 82  (more unwanted noise noise compared to 10,25)
# 1.83              # 10      #50            # 130         #                           # 11
#Observations:
# 1.For this dataset, as the esp was decreasing the time was decreasing.

import numpy as np

import matplotlib
matplotlib.use('TkAgg') # makes it fast (not use qt) 

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from collections import Counter # needed  to count the result of clustering 
import time
###############################################
min_dist_between_cluster=10
min_sample_around_a_sample=50
###### visual configuration ######
plot_project_xz=False
plot_project_yz=False
normal_data_alpha=.25
noise_data_alpha=0.5
###############################################
#Generate sample data
X = np.loadtxt("input.txt",dtype=float)
print("Shape of X=",X.shape)

################Compute DBSCAN################################
t0 = time.time()
print("Min distance between clusters=", min_dist_between_cluster)
print("Min. number of sample around a sample=", min_sample_around_a_sample)
db = DBSCAN(eps=min_dist_between_cluster, min_samples=min_sample_around_a_sample).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)

t1 = time.time()
print("time=",(t1-t0))
print("Clustered\n")

core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

#plot the result

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Black removed and is used for noise instead.
unique_labels = set(labels)
print(Counter(labels))
print(unique_labels)

for k in unique_labels:
    #print("k=",k)
    if k == -1:
        # Red used for noise.
        col = 'r'
        print('col is red now')
	
    else:	
	    col='b'
        
    class_member_mask = (labels == k)
    
    xy = X[class_member_mask & core_samples_mask]
    ax.scatter(xy[:,0], xy[:,1], xy[:,2], c=col, marker='.', alpha=normal_data_alpha)
    if(plot_project_xz):
        ax.plot(xy[:,0], xy[:,2], 'b+', zdir='y',alpha=normal_data_alpha)
    if(plot_project_yz):
        ax.plot(xy[:,1], xy[:,2], 'b+', zdir='x',alpha=normal_data_alpha)
        
    xy = X[class_member_mask & ~core_samples_mask]
    ax.scatter(xy[:,0], xy[:,1], xy[:,2],c=col,alpha=noise_data_alpha)
    if(plot_project_xz):
        ax.plot(xy[:,0], xy[:,2], 'g+', zdir='y',alpha=noise_data_alpha)
    if(plot_project_yz):
        ax.plot(xy[:,1], xy[:,2], 'r+', zdir='x',alpha=noise_data_alpha)
    
plt.title('Estimated number of clusters: %d' % n_clusters_)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()


