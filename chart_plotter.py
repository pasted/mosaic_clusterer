import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D

class ChartPlotter():

   def render(this_transposed_array, this_mean_shift):
      these_labels = this_mean_shift.labels_
      these_cluster_centers = this_mean_shift.cluster_centers_
   
      these_labels_unique = np.unique(these_labels)
      these_n_clusters_ = len(these_labels_unique)
   
      print("number of estimated clusters : %d" %these_n_clusters_)
      
      fig = plt.figure(1)
      ax = fig.add_subplot(111, projection='3d')
   
      colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
   
      for k, col in zip(range(these_n_clusters_), colors):
         my_members = these_labels == k
         cluster_center = these_cluster_centers[k]
         ax.scatter(this_transposed_array[my_members, 0], this_transposed_array[my_members, 1], this_transposed_array[my_members, 2], col + '.')
         #plt.plot(this_transposed_array[my_members, 0], this_transposed_array[my_members, 1], this_transposed_array[my_members, 2], col + '.')
         #plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
      
      ax.set_xlabel('Reference Allele Depth')
      ax.set_ylabel('Alternative Allele Depth')
      ax.set_zlabel('Geneotype quality')
      plt.title('Estimated number of clusters: %d' % these_n_clusters_)
      plt.show()

