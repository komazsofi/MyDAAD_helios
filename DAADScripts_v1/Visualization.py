
# coding: utf-8

# 

# 1.) Importing example datasets from LiDAR simulation tool (HELIOS https://github.com/nlukac/helios-FWF)
# File structure is the following: [x,y,z,intensity,echowidth,returnNumber,returnNumPerPulse,FWFIndex,objectId]

# In[6]:

import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('als', help='als point cloud')
parser.add_argument('tls', help='tls point cloud')
parser.add_argument('mls', help='mls point cloud')
parser.add_argument('uls', help='uls point cloud')
args = parser.parse_args()

als_data=pd.read_csv(args.als,sep=' ',
                     names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex',
                            'objectId'])
tls_data=pd.read_csv(args.tls,sep=' ',
                     names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex',
                            'objectId'])
mls_data=pd.read_csv(args.mls,sep=' ',
                     names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex',
                            'objectId'])
uls_data=pd.read_csv(args.uls,sep=' ',
                     names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex',
                            'objectId'])


# 2.) Visualization of the point clouds measured by different platforms

# In[26]:

import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(141, projection='3d')
ax2 = fig.add_subplot(142, projection='3d')
ax3 = fig.add_subplot(143, projection='3d')
ax4 = fig.add_subplot(144, projection='3d')

ax1.scatter(als_data['x'].values,als_data['y'].values,als_data['NormalizedZ'].values, 
            c=als_data['returnNumber'].values,vmin=1, vmax=4,cmap=cm.hsv)

ax2.scatter(tls_data['x'].values,tls_data['y'].values,tls_data['NormalizedZ'].values, 
            c=tls_data['returnNumber'].values,vmin=1, vmax=4,cmap=cm.hsv)

ax3.scatter(mls_data['x'].values,mls_data['y'].values,mls_data['NormalizedZ'].values, 
            c=mls_data['returnNumber'].values,vmin=1, vmax=4,cmap=cm.hsv)

ax4.scatter(uls_data['x'].values,uls_data['y'].values,uls_data['NormalizedZ'].values, 
            c=uls_data['returnNumber'].values,vmin=1, vmax=4,cmap=cm.hsv)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_zlim([np.min(als_data['returnNumber'].values),np.max(als_data['NormalizedZ'].values)])

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_zlim([np.min(als_data['returnNumber'].values),np.max(als_data['NormalizedZ'].values)])

ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_zlim([np.min(als_data['returnNumber'].values),np.max(als_data['NormalizedZ'].values)])

ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_zlim([np.min(als_data['returnNumber'].values),np.max(als_data['NormalizedZ'].values)])

m = cm.ScalarMappable(cmap=cm.hsv)
m.set_array([1,4])
cbar = plt.colorbar(m)
cbar.set_label('Number of returns')

ax1.azim = 30
ax1.elev = 5
ax2.azim = 30
ax2.elev = 5
ax3.azim = 30
ax3.elev = 5
ax4.azim = 30
ax4.elev = 5

ax1.set_title('ALS')
ax2.set_title('TLS')
ax3.set_title('MLS')
ax4.set_title('ULS')

plt.show()

