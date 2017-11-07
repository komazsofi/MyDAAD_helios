
# coding: utf-8

# 1.) Import data one by one

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument('workdir', help='working directory') 
parser.add_argument('filename', help='the simulation output filename') 
args = parser.parse_args()

workdir=args.workdir 
filename=args.filename

CB=20

sim_data=pd.read_csv(workdir+filename,sep=' ',names=['x','y','NormalizedZ','intensity','echowidth','returnNumber','returnNumPerPulse','FWFIndex','objectId'])


# 2.) Organizing the data

# In[2]:

ground_sim_data=sim_data[(sim_data['objectId']==0)]
nonground_sim_data=sim_data[(sim_data['objectId']==1)]

def convert_treetype(name):
    if name=='PH':
        shape='spherical'
    if name=='PN':
        shape='conical'
    if name=='PoN':
        shape='cylinderical'
    return shape

nonground_sim_data['NormalizedZ_perc']=(100*nonground_sim_data.NormalizedZ)/np.max(nonground_sim_data.NormalizedZ)
nonground_sim_data_f=nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1)]


# 3.) Object based features 
# a.) Features related to the tree height

# In[10]:

def general_statistics_descriptors(NormalizedZ):
    import scipy.stats.stats as stat
    mean_z=np.mean(NormalizedZ)
    median_z=np.median(NormalizedZ)
    var_z=np.var(NormalizedZ)
    std_z=np.std(NormalizedZ)
    coeffvar_z=np.std(NormalizedZ)/np.mean(NormalizedZ)
    skew_z=stat.skew(NormalizedZ)
    kurto_z=stat.kurtosis(NormalizedZ)
    max_z=np.percentile(NormalizedZ,98)
    return mean_z,median_z,var_z,std_z,coeffvar_z,skew_z,kurto_z,max_z

a_mean_z,a_median_z,a_var_z,a_std_z,a_coeffvar_z,a_skew_z,a_kurto_z,max_z=general_statistics_descriptors(nonground_sim_data['NormalizedZ'].values)
#a_mean_z_n,a_median_z_n,a_var_z_n,a_std_z_n,a_coeffvar_z_n,a_skew_z_n,a_kurto_z_n,max_z_n=general_statistics_descriptors(nonground_sim_data['NormalizedZ_perc'].values)
a_mean_f,a_median_f,a_var_f,a_std_f,a_coeffvar_f,a_skew_f,a_kurto_f,max_f=general_statistics_descriptors(nonground_sim_data_f['NormalizedZ_perc'].values)

print a_mean_z,a_median_z,a_var_z,a_std_z,a_coeffvar_z,a_skew_z,a_kurto_z,max_z
print a_mean_f,a_median_f,a_var_f,a_std_f,a_coeffvar_f,a_skew_f,a_kurto_f,max_f


# b.) Number of points ratios (first, single multiple to all) and echo type ratios (25th,50th,75th perc to first, only single, only multiple)

# In[4]:

nofp_single_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1)].index))/np.float(len(nonground_sim_data.index))
nofp_first_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumber']==1)].index))/np.float(len(nonground_sim_data.index))
nofp_multi_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']>1)].index))/np.float(len(nonground_sim_data.index))

nofp_up25_single_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],25))].index))/np.float(len(nonground_sim_data.index))
nofp_up50_single_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],50))].index))/np.float(len(nonground_sim_data.index))
nofp_up75_single_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],75))].index))/np.float(len(nonground_sim_data.index))

nofp_up25_first_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumber']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],25))].index))/np.float(len(nonground_sim_data.index))
nofp_up50_first_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumber']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],50))].index))/np.float(len(nonground_sim_data.index))
nofp_up75_first_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumber']==1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],75))].index))/np.float(len(nonground_sim_data.index))

nofp_up25_multi_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']>1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],25))].index))/np.float(len(nonground_sim_data.index))
nofp_up50_multi_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']>1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],50))].index))/np.float(len(nonground_sim_data.index))
nofp_up75_multi_to_all=np.float(len(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']>1) & (nonground_sim_data['NormalizedZ']<np.percentile(nonground_sim_data['NormalizedZ'],75))].index))/np.float(len(nonground_sim_data.index))

print nofp_single_to_all,nofp_first_to_all,nofp_multi_to_all,nofp_up25_single_to_all,nofp_up50_single_to_all,nofp_up75_single_to_all,nofp_up25_first_to_all,nofp_up50_first_to_all,nofp_up75_first_to_all,nofp_up25_multi_to_all,nofp_up50_multi_to_all,nofp_up75_multi_to_all


# c.) Crown -- currently CB determined manually

# In[6]:

def crown_fea(nonground_sim_data,CB):
    from scipy.spatial import ConvexHull
    
    crown=nonground_sim_data[(nonground_sim_data['NormalizedZ_perc']>CB)]
    c_length=np.max(crown['NormalizedZ_perc'])-CB
    hull = ConvexHull(crown[['x','y']].values)
    x=crown['x'].values
    y=crown['y'].values
    c_width=np.sqrt(((np.max(x[hull.vertices])-np.min(x[hull.vertices]))**2)+((np.max(y[hull.vertices])-np.min(y[hull.vertices]))**2))
    
    return c_length,c_width,c_length/c_width

c_length,c_width,ratio_length_width=crown_fea(nonground_sim_data,CB)
print c_length,c_width,ratio_length_width
    


# 4.) Subset features

# In[7]:

def nofp_per_eq(nonground_sim_data):
    h=""
    nofp_tototal=""
    nofp_first_tototal=""
    nofp_single_tototal=""
    nofp_multi_tototal=""
    
    for i in range(0,100,10):
        
        h_s=i+10
        h+="%f," % (h_s)

        nofp_tototal_s=np.float(nonground_sim_data[(nonground_sim_data['NormalizedZ_perc']>i) & (nonground_sim_data['NormalizedZ_perc']<i+10)].shape[0])/np.float(nonground_sim_data['NormalizedZ_perc'].shape[0])
        nofp_tototal+="%f," % (nofp_tototal_s*100)

        nofp_first_tototal_s=np.float(nonground_sim_data[(nonground_sim_data['returnNumber']==1) & (nonground_sim_data['NormalizedZ_perc']>i) & (nonground_sim_data['NormalizedZ_perc']<i+10)].shape[0])/np.float(nonground_sim_data['NormalizedZ_perc'].shape[0])
        nofp_first_tototal+="%f," % (nofp_first_tototal_s*100)
        
        nofp_single_tototal_s=np.float(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']==1) & (nonground_sim_data['NormalizedZ_perc']>i) & (nonground_sim_data['NormalizedZ_perc']<i+10)].shape[0])/np.float(nonground_sim_data['NormalizedZ_perc'].shape[0])
        nofp_single_tototal+="%f," % (nofp_single_tototal_s*100)
        
        nofp_multi_tototal_s=np.float(nonground_sim_data[(nonground_sim_data['returnNumPerPulse']>1) & (nonground_sim_data['NormalizedZ_perc']>i) & (nonground_sim_data['NormalizedZ_perc']<i+10)].shape[0])/np.float(nonground_sim_data['NormalizedZ_perc'].shape[0])
        nofp_multi_tototal+="%f," % (nofp_multi_tototal_s*100)
        
    return h,nofp_tototal,nofp_first_tototal,nofp_single_tototal,nofp_multi_tototal

h,nofp_tototal,nofp_first_tototal,nofp_single_tototal,nofp_multi_tototal=nofp_per_eq(nonground_sim_data)
print h
print nofp_tototal 
print nofp_first_tototal
print nofp_single_tototal
print nofp_multi_tototal


# 5.) Export

# In[11]:

output_fea_obj = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (filename,filename[0:3],filename[4:-17],convert_treetype(filename[4:-18]),filename[-12:-11],
h,nofp_tototal,nofp_first_tototal,nofp_single_tototal,nofp_multi_tototal,
a_mean_z,a_median_z,a_var_z,a_std_z,a_coeffvar_z,a_skew_z,a_kurto_z,max_z,
a_mean_f,a_median_f,a_var_f,a_std_f,a_coeffvar_f,a_skew_f,a_kurto_f,max_f,
nofp_single_to_all,nofp_first_to_all,nofp_multi_to_all,nofp_up25_single_to_all,nofp_up50_single_to_all,nofp_up75_single_to_all,nofp_up25_first_to_all,nofp_up50_first_to_all,nofp_up75_first_to_all,nofp_up25_multi_to_all,nofp_up50_multi_to_all,nofp_up75_multi_to_all,
c_length,c_width,ratio_length_width)

print output_fea_obj

fileout = file(workdir+filename[:-4]+'with_geomfea.txt', "w")
fileout.write(output_fea_obj)
fileout.close()


# 5.) Run the downloaded script in terminal -- modify the script with this (add argparse for terminal based data processing):
# 
# import argparse
# 
# parser = argparse.ArgumentParser() parser.add_argument('workdir', help='working directory') parser.add_argument('filename', help='the simulation output filename') args = parser.parse_args()
# 
# workdir=args.workdir filename=args.filename
# 
# -- in the working directory run the bash file like this:
# 
# for i in *.xyz; do python /home/komazsofi/Munka/Heidelberg/DAAD_helios_sim/Python/DAAD_workflow_object_based_geometrical_feature_derivation_v2.py /home/komazsofi/Munka/Heidelberg/DAAD_helios_sim/Data2/ $i; done
# 
# -- than merge together the files:
# 
# cat *with_obj_geomfea.txt > Sim_obj_geom_fea.txt
# 
