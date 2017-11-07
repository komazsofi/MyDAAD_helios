
# coding: utf-8

# 1.) Point cloud import
# 
# The import based on the general info file which contained a.) the filename of the simulation output b.) the platform c.) the code name of the tree modell (PN1= Pinus Nigra 1 modell) separated by ','. Every 4 rows should related to one tree modell simulation via ALS, TLS, MLS and ULS platforms.
# 
# Importing example datasets related to generated datasets via LiDAR Simulation Tool (HELIOS https://github.com/nlukac/helios-FWF).
# Output file structure is the following: [x,y,z,intensity,echowidth,returnNumber,returnNumPerPulse,FWFIndex,objectId].
# 

# In[25]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workdir='/home/komazsofi/Munka/Heidelberg/DAAD_helios_sim/Data/'
treemodell='PN1'

general_data=pd.read_csv(workdir+'GeneralInfo_Sim.txt',sep=',',names=['filename','platform','treemodellid'])
general_data=general_data[(general_data['treemodellid']=='PN1')]

als=general_data[(general_data['platform']=='ALS')]
tls=general_data[(general_data['platform']=='TLS')]
mls=general_data[(general_data['platform']=='MLS')]
uls=general_data[(general_data['platform']=='ULS')]

als_data=pd.read_csv(workdir+als['filename'].values[0],sep=' ',names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex','objectId'])
tls_data=pd.read_csv(workdir+tls['filename'].values[0],sep=' ',names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex','objectId'])
mls_data=pd.read_csv(workdir+mls['filename'].values[0],sep=' ',names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex','objectId'])
uls_data=pd.read_csv(workdir+uls['filename'].values[0],sep=' ',names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex','objectId'])


# 2.) Visualization of the point clouds colored by number of returns according to different platforms

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

ax1.azim = 65
ax1.elev = 5
ax2.azim = 65
ax2.elev = 5
ax3.azim = 65
ax3.elev = 5
ax4.azim = 65
ax4.elev = 5

ax1.set_title('ALS')
ax2.set_title('TLS')
ax3.set_title('MLS')
ax4.set_title('ULS')

plt.show()

