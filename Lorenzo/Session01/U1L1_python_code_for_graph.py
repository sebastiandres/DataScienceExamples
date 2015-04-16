import numpy as np
# from numpy.random import randn
# import pandas as pd
# from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# import statsmodels.api as sm
# from skimage.measure import structural_similarity as ssim
# from matplotlib import rc


sns.set(context="paper", font="Open Sans")
sns.set_style("white")
fig, axs = plt.subplots(4,2, figsize=(5, 12), facecolor='w', edgecolor='k',sharex=False, sharey=False )
fig.subplots_adjust(hspace = .1, wspace=.2)

axs = axs.ravel()

ssim_v = np.loadtxt('dat/v.dat')
mapvp1 = np.loadtxt('dat/mapvp1.dat')
mapvp3 = np.loadtxt('dat/mapvp3.dat')
mapvs1 = np.loadtxt('dat/mapvs1.dat')
mapvs3 = np.loadtxt('dat/mapvs3.dat')
maprho1 = np.loadtxt('dat/maprho1.dat')
maprho3 = np.loadtxt('dat/maprho3.dat')
mapphi1 = np.loadtxt('dat/mapphi1.dat')
mapphi3 = np.loadtxt('dat/mapphi3.dat')

ssimap = [mapvp3,mapvp1,mapvs3,mapvs1,maprho3,maprho1,mapphi3,mapphi1]
ssimap_value = [ssim_v[0,0],ssim_v[0,1],ssim_v[1,0],ssim_v[1,1],ssim_v[2,0],ssim_v[2,1],ssim_v[3,0],ssim_v[3,1]]
title = ['Static optimization','Final inversion results','','','','','','']
xtick = ['','','','','','',('0','0','250','500','750','1000'),('0','0','250','500','750','1000')]
ytick = [('0','0','250','500','750','1000','1250','1500'),'',('0','0','250','500','750','1000','1250','1500'),'',('0','0','250','500','750','1000','1250','1500'),'',('0','0','250','500','750','1000','1250','1500'),'']
xlabel = ['','','','','','','Distance (m)','Distance(m)']
ylabel = ['Depth (m)','','Depth (m)','','Depth (m)','','Depth (m)','']
bbox_props = dict(boxstyle="square,pad=0.3", fc="white", lw=.5)

for i in range(8):
    
    im = axs[i].imshow(ssimap[i],cmap='RdBu_r',aspect='auto',vmin=0, vmax=1)
    axs[i].set_title(title[i], fontsize=13,fontweight='bold')
    axs[i].set_xticklabels(xtick[i])
    axs[i].set_yticklabels(ytick[i])
    axs[i].text(100, 280, 'SSIM = '+str(round(ssimap_value[i],2)), ha="center",va="center",size=10,bbox=bbox_props)
    axs[i].set_xlabel(xlabel[i])
    axs[i].set_ylabel(ylabel[i])
                
cax = fig.add_axes([0.93, 0.323, 0.02, 0.379])
fig.colorbar(im, cax=cax)
cax.set_yticklabels(['0','','','','','','','','','','1'],fontsize=12)
fig.text(0.52,0.81,'P-WAVE VELOCITY', ha="center",va="center",rotation='90',fontsize=12)
fig.text(0.52,0.61,'S-WAVE VELOCITY', ha="center",va="center",rotation='90',fontsize=12)
fig.text(0.52,0.41,'DENSITY', ha="center",va="center",rotation='90',fontsize=12)
fig.text(0.52,0.21,'POROSITY', ha="center",va="center",rotation='90',fontsize=12)

plt.show()