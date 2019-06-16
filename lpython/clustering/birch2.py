from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle
from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import Birch, MiniBatchKMeans
from sklearn.datasets.samples_generator import make_blobs
#######################################
#TBD: Add with param info in plot -Mnj
#######################################

#################Parameters########################
#threshold_value = 1.7 # n_c = None : Clusters, using partial_fit: 12779
#threshold_value = 5.0 # n_c = None : Clusters, using partial_fit: 1680  
#threshold_value = 6.0 # n_c = None : Clusters, using partial_fit: 1195
threshold_value = 7.0 # n_c = None  : Clusters, using partial_fit: 899
#n_c = 100
n_c = None

###### visual configuration ###########
plot_project_xz=False
plot_project_yz=False
normal_data_alpha=.25
noise_data_alpha=0.5
###############################################
#read data
X = np.loadtxt("input.txt",dtype=float)
print("Shape of X=",X.shape)
#######################################
birch_model = Birch(threshold=threshold_value, n_clusters=n_c,compute_labels=True)
t = time()
result = birch_model.fit(X)
#result = birch_model.partial_fit(X)
result = birch_model.predict(X)
time_ = time() - t
print("Birch took %0.2f seconds" % ( (time() - t)))
print("Result=",result)
#plot the result

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

labels = birch_model.labels_
#print("Labels=",labels)
unique_labels = set(labels)
print("unique_labels=",unique_labels)


n_clusters = np.unique(labels).size

print("n_clusters : %d" % n_clusters)
print(range(n_clusters))

core_samples_mask = np.zeros_like(labels, dtype=bool)
print("len(unique_labels)=",len(unique_labels))
core_samples_mask[len(unique_labels)] = True
print("Here1")
print("x=",X[:,0])
ax.scatter(X[:,0], X[:,1], X[:,2], marker='.')

print("Here2")

for k in unique_labels:
    col = 'b'
    if k == -1:
        col = 'r'
'''
    class_member_mask = (labels == k)
    
    xy = X[class_member_mask & core_samples_mask]
    print("xy0=",xy)
    ax.scatter(xy[:,0], xy[:,1], xy[:,2], c=col, marker='.', alpha=normal_data_alpha)
    if(plot_project_xz):
        ax.plot(xy[:,0], xy[:,2], 'b+', zdir='y',alpha=normal_data_alpha)
    if(plot_project_yz):
        ax.plot(xy[:,1], xy[:,2], 'b+', zdir='x',alpha=normal_data_alpha)
    print("xy1=",xy)
    xy = X[class_member_mask & ~core_samples_mask]
    ax.scatter(xy[:,0], xy[:,1], xy[:,2],c=col,alpha=noise_data_alpha)
    if(plot_project_xz):
        ax.plot(xy[:,0], xy[:,2], 'g+', zdir='y',alpha=noise_data_alpha)
    if(plot_project_yz):
        ax.plot(xy[:,1], xy[:,2], 'r+', zdir='x',alpha=noise_data_alpha)
'''    
plt.title('Birch: Number of clusters= %d' % n_clusters)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')        
plt.show