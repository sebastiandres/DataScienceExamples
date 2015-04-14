
# coding: utf-8

# In[2]:

get_ipython().magic(u'matplotlib inline')


# In[3]:

import numpy as np
from numpy.random import randn
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from skimage.measure import structural_similarity as ssim
# from matplotlib import rc


# In[4]:

mpl.rcParams['pdf.fonttype'] = 42
sns.set_palette("deep", desat=.6)
mpl.rcParams['font.sans-serif'].insert(0, 'Open Sans')
mpl.rcParams['font.sans-serif'].insert(0, 'Helvetica')
mpl.rcParams['font.family'] = 'sans-serif'
sns.set(context="paper", font="Open Sans",rc={"figure.figsize": (12,6)})
np.random.seed(9221999)
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# rc('text', usetex=True)


# In[5]:

# vp1 = np.loadtxt('dat/vp1.dat')
# vpreal = np.loadtxt('dat/vpreal.dat')
# vpref = np.loadtxt('dat/vpref.dat')
# dg_real = pd.read_csv('dat/dg_real.csv')
# dg_DG = pd.read_csv('dat/dg_DG.csv')
dg_all = pd.read_csv('dat/dg_all_fil.csv')
# dg_res = pd.read_csv('dat/dg_res.csv')
# dg=pd.read_csv('dat/dg.csv')
matrix=np.loadtxt('dat/matrix.dat')
vp1_map=np.loadtxt('dat/vp1_map.dat')
vpreal_map=np.loadtxt('dat/vpreal_map.dat')
vs1_map=np.loadtxt('dat/vs1_map.dat')
vsreal_map=np.loadtxt('dat/vsreal_map.dat')
rho1_map=np.loadtxt('dat/rho1_map.dat')
rhoreal_map=np.loadtxt('dat/rhoreal_map.dat')
phi1_map=np.loadtxt('dat/phi1_map.dat')
phireal_map=np.loadtxt('dat/phireal_map.dat')
vp_co2=np.loadtxt('dat/Vp_co2.dat')


# In[13]:

fig = plt.Figure()
fig.set_canvas(plt.gcf().canvas)
ax1 = plt.subplot(2,4,1)
sns.regplot("GD1_Vp", "observed_Vp", dg_all, ax=ax1,scatter_kws={"s": 10,"marker": ".", "color": "#4C1F00","alpha":.3},line_kws={"linewidth": 1, "color": "#4C1F00"})
ax1.set_ylim([3500, 6500])
ax1.set_xlim([3500, 6500])
ax1.set_ylabel('observed')
ax1.set_xlabel('')
ax1.set_title('Vp',fontsize=14)
# ax1.set_title('One random SGS realization',fontsize=12)
ax2 = plt.subplot(2,4,2)
sns.regplot("GD1_Vs", "observed_Vs", dg_all, ax=ax2,scatter_kws={"s": 10,"marker": ".", "color": "#803300","alpha":.3},line_kws={"linewidth": 1, "color": "#803300"})
ax2.set_ylim([1500, 4000])
ax2.set_xlim([1500, 4000])
ax2.set_ylabel('')
ax2.set_xlabel('')
ax2.set_title('Vs',fontsize=14)
# ax2.set_title('After inversion workflow',fontsize=12)
# ax2.annotate('Vs', (3750, 1650), textcoords='data', size=10)
ax3 = plt.subplot(2,4,3)
sns.regplot("GD1_rho", "observed_rho", dg_all, ax=ax3,scatter_kws={"s": 10,"marker": ".", "color": "#E65C00","alpha":.3},line_kws={"linewidth": 1, "color": "#E65C00"})
ax3.set_ylim([2300, 2500])
ax3.set_xlim([2300, 2500])
ax3.set_ylabel('')
ax3.set_xlabel('')
ax3.set_title(r'$\rho$',fontsize=15)
# ax3.annotate('rho', (2475, 2315), textcoords='data', size=10)
ax4 = plt.subplot(2,4,4)
sns.regplot("GD1_phi", "observed_phi", dg_all, ax=ax4,scatter_kws={"s": 10,"marker": ".", "color": "#FF7519","alpha":.3},line_kws={"linewidth": 1, "color": "#FF7519"})
ax4.set_ylim([0, 0.15])
ax4.set_xlim([0, 0.15])
ax4.set_ylabel('')
ax4.set_xlabel('')
ax4.set_title(r'$\phi$',fontsize=15)
trans = ax4.get_xaxis_transform() # x in data untis, y in axes fraction
ann = ax4.annotate('One random SGS realization', xy=(0.16, 0.95 ),rotation='90', xycoords=trans,fontsize='14')
# ax4.annotate('phi', (0.125, 0.005), textcoords='data', size=10)
fig.text(0.98,0.35,'After GD',fontsize=15)
ax5 = plt.subplot(2,4,5)
sns.regplot("GD_Vp", "observed_Vp", dg_all, ax=ax5,scatter_kws={"s": 10,"marker": ".", "color": "#4C1F00","alpha":.3},line_kws={"linewidth": 1, "color": "#4C1F00"})
ax5.set_ylim([3500, 6500])
ax5.set_xlim([3500, 6500])
ax5.set_ylabel('observed')
ax5.set_xlabel('simulated')
# ax5.set_title('Vp',fontsize=15)
# ax5.annotate('rho', (2475, 2315), textcoords='data', size=10)
ax6 = plt.subplot(2,4,6)
sns.regplot("GD_Vs", "observed_Vs", dg_all, ax=ax6,scatter_kws={"s": 10,"marker": ".", "color": "#803300","alpha":.3},line_kws={"linewidth": 1, "color": "#803300"})
ax6.set_ylim([1500, 4000])
ax6.set_xlim([1500, 4000])
ax6.set_ylabel('')
ax6.set_xlabel('simulated')
# ax6.annotate('rho', (2475, 2315), textcoords='data', size=10)
ax7 = plt.subplot(2,4,7)
sns.regplot("GD_rho", "observed_rho", dg_all, ax=ax7,scatter_kws={"s": 10,"marker": ".", "color": "#E65C00","alpha":.3},line_kws={"linewidth": 1, "color": "#E65C00"})
ax7.set_xlim([2300, 2500])
ax7.set_ylim([2300, 2500])
ax7.set_ylabel('')
ax7.set_xlabel('simulated')
# ax7.annotate('phi', (0.125, 0.005), textcoords='data', size=10)
ax8 = plt.subplot(2,4,8)
sns.regplot("GD_phi", "observed_phi", dg_all, ax=ax8,scatter_kws={"s": 10,"marker": ".", "color": "#FF7519","alpha":.3},line_kws={"linewidth": 1, "color": "#FF7519"})
ax8.set_xlim([0, 0.15])
ax8.set_ylim([0, 0.15])
ax8.set_ylabel('')
ax8.set_xlabel('simulated')
trans = ax8.get_xaxis_transform() # x in data untis, y in axes fraction
ann = ax8.annotate('Final inversion result', xy=(0.16, 0.85 ),rotation='90', xycoords=trans,fontsize='14')
# ax8.annotate('phi', (0.125, 0.005), textcoords='data', size=10)
# fig.text(0.98,0.35,'After GD',rotation='270',fontsize=15)
plt.tight_layout()


# In[14]:

fig.savefig('correlation.pdf', transparent=False,bbox_inches='tight',  pad_inches=0.08)


# In[36]:

sns.set(context="paper", font="Open Sans",rc={"figure.figsize": (16,4)})
fig = plt.figure()
ax = fig.add_subplot(1, 4, 1)
# fig, ((ax1, ax2,ax3,ax4)) = plt.subplots(1, 4, sharex=False, sharey=True)
pp_x = sm.ProbPlot(matrix[::150,8], fit=False)
pp_y = sm.ProbPlot(matrix[::150,0], fit=False)
pp_x.qqplot(other=pp_y,line='45',ax=ax)
# ax = fig.axes[0]
points, fit_line = ax.lines
points.set_color("#0066CC")
fit_line.set_color("#CC0000")
ax.set_xlabel("simulated")
ax.set_ylabel("observed")
ax.set_title('Vp',fontsize=14)
ax = fig.add_subplot(1, 4, 2)
# fig, ((ax1, ax2,ax3,ax4)) = plt.subplots(1, 4, sharex=False, sharey=True)
pp_x = sm.ProbPlot(matrix[::150,9], fit=False)
pp_y = sm.ProbPlot(matrix[::150,1], fit=False)
pp_x.qqplot(other=pp_y,line='45',ax=ax)
# ax = fig.axes[0]
points, fit_line = ax.lines
points.set_color("#0066CC")
fit_line.set_color("#CC0000")
ax.set_xlabel("simulated")
ax.set_ylabel("")
ax.set_title('Vs',fontsize=14)
ax = fig.add_subplot(1, 4, 3)
# fig, ((ax1, ax2,ax3,ax4)) = plt.subplots(1, 4, sharex=False, sharey=True)
pp_x = sm.ProbPlot(matrix[::150,10], fit=False)
pp_y = sm.ProbPlot(matrix[::150,2], fit=False)
pp_x.qqplot(other=pp_y,line='45',ax=ax)
# ax = fig.axes[0]
points, fit_line = ax.lines
points.set_color("#0066CC")
fit_line.set_color("#CC0000")
ax.set_xlabel("simulated")
ax.set_ylabel("")
ax.set_title(r'$\rho$',fontsize=15)
ax.set_xticklabels(['2300','','','2450','','','2600','','','2750'])
ax.set_yticklabels(['2300','','','2450','','','2600','','','2750'])
ax = fig.add_subplot(1, 4, 4)
# fig, ((ax1, ax2,ax3,ax4)) = plt.subplots(1, 4, sharex=False, sharey=True)
pp_x = sm.ProbPlot(matrix[::150,11], fit=False)
pp_y = sm.ProbPlot(matrix[::150,3], fit=False)
pp_x.qqplot(other=pp_y,line='45',ax=ax)
# ax = fig.axes[0]
points, fit_line = ax.lines
points.set_color("#0066CC")
fit_line.set_color("#CC0000")
ax.set_xlabel("simulated")
ax.set_ylabel("")
ax.set_title(r'$\phi$',fontsize=15)


# In[37]:

fig.savefig('qqplot.pdf', transparent=False, bbox_inches='tight', pad_inches=0.05)


# In[86]:

sns.set(context="paper", font="Open Sans",rc={"figure.figsize": (8,6)})
sns.set_style("white")
fig, ((ax1, ax2,ax3,ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex=False, sharey=True)
ax1.imshow(vpreal_map,cmap='RdBu_r',aspect='auto')
ax1.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
ax1.set_title('Vp',fontsize=14)
a=matrix[:,0]
b=matrix[:,4]
ssim_1 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax1.set_xlabel('SSIM='+str(round(ssim_1,2)),fontsize=10,color='white')
ax1.set_yticklabels(['0','0','250','500','750','1000','1250','1500'])
ax1.tick_params(axis='y',which='left',bottom='off',top='off',labelbottom='off')
# ax1.text(0.2,0.565,'SSIM='+str(round(ssim_1,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax1.set_xlabel('SSIM='+str(round(ssim_1,2)),fontsize=10)
fig.text(0.05,0.54,'Depth [m]',rotation='90',fontsize=13)
fig.text(0.92,0.89,'One random SGS realization',rotation='90',fontsize=13)
ax2.imshow(vsreal_map,cmap='RdBu_r',aspect='auto')
ax2.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
ax2.set_title('Vs',fontsize=14)
a=matrix[:,1]
b=matrix[:,5]
ssim_2 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax2.set_xlabel('SSIM='+str(round(ssim_2,2)),fontsize=10)
ax2.text(0.373,0.565,'SSIM='+str(round(ssim_2,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax3.imshow(rhoreal_map,cmap='RdBu_r',aspect='auto')
ax3.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
ax3.set_title(r'$\rho$',fontsize=15)
a=matrix[:,2]
b=matrix[:,6]
ssim_3 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax3.set_xlabel('SSIM='+str(round(ssim_3,2)),fontsize=10,color='white')
ax3.text(0.573,0.565,'SSIM='+str(round(ssim_3,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
phi = ax4.imshow(phireal_map,cmap='RdBu_r',aspect='auto')
# cbar_ax = fig.add_axes([0.5, 0.5, .4, .015])
# fig.colorbar(phi, cax=cbar_ax,orientation='horizontal')
ax4.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='off')
ax4.set_title(r'$\phi$',fontsize=15)
a=matrix[:,3]
b=matrix[:,7]
ssim_4 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax4.set_xlabel('SSIM='+str(round(ssim_4,2)),fontsize=10)
# ax4.text(0.805,0.565,'SSIM='+str(round(ssim_4,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax4.set_xlabel('SSIM='+str(round(ssim_4,2)),fontsize=10)
# ax4.yaxis.tick_right()
# ax4.set_ylabel('Depth [m]')
# ax4.yaxis.set_label_position('right')
ax5.imshow(vp1_map,cmap='RdBu_r',aspect='auto')
a=matrix[:,0]
b=matrix[:,8]
ssim_5 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax5.set_title('SSIM='+str(round(ssim_5,2)),fontsize=10)
ax5.set_xticklabels(['0','0','250','500','750','1000'])
fig.text(0.46,0.05,'Distance [m]',rotation='0',fontsize=13)
# ax5.text(0.2,0.448,'SSIM='+str(round(ssim_5,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax5.set_title('SSIM='+str(round(ssim_5,2)),fontsize=10)
ax6.imshow(vs1_map,cmap='RdBu_r',aspect='auto')
a=matrix[:,1]
b=matrix[:,9]
ssim_6 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax6.set_title('SSIM='+str(round(ssim_6,2)),fontsize=10)
ax6.set_xticklabels(['0','0','250','500','750','1000'])
ax6.text(0.373,0.448,'SSIM='+str(round(ssim_6,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax7.imshow(rho1_map,cmap='RdBu_r',aspect='auto')
a=matrix[:,2]
b=matrix[:,10]
ssim_7 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax7.set_title('SSIM='+str(round(ssim_7,2)),fontsize=10)
ax7.set_xticklabels(['0','0','250','500','750','1000'])
ax7.text(0.573,0.448,'SSIM='+str(round(ssim_7,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
phi2=ax8.imshow(phi1_map,cmap='RdBu_r',aspect='auto')
a=matrix[:,3]
b=matrix[:,11]
ssim_8 = ssim(a.reshape(301,200,order='F'), b.reshape(301,200,order='F'))
# ax8.set_title('SSIM='+str(round(ssim_8,2)),fontsize=10,color='white')
ax8.set_xticklabels(['0','0','250','500','750','1000'])
fig.text(0.92,0.42,'Final inversion result',rotation='90',fontsize=13)
# ax8.text(0.805,0.448,'SSIM='+str(round(ssim_8,2)),fontsize=10,transform=fig.transFigure,backgroundcolor='white')
cbar_ax = fig.add_axes([0.384, 0.505, .25, .015])
fig.colorbar(phi2, cax=cbar_ax,orientation='horizontal')
cbar_ax.set_xticklabels(['','','','','','','',''])
ax8.set_title('SSIM='+str(round(ssim_8,2)),fontsize=10)
# ax8.yaxis.tick_right()
# ax8.yaxis.set_label_position('right')
# ax8.set_ylabel('Depth [m]')
# fig.tight_layout()
fig.text(0.644,0.505,'1',rotation='0',fontsize=9)
fig.text(0.364,0.505,'0',rotation='0',fontsize=9)


# In[114]:

fig.savefig('ssim.pdf', transparent=True, bbox_inches='tight', pad_inches=0.1)


# In[87]:

G_REF=np.loadtxt('dat/G_REF.dat')
G_SGS=np.loadtxt('dat/G_SGS.dat')
G_DG=np.loadtxt('dat/G_DG.dat')
mapsgs=np.loadtxt('dat/map_sgs.dat')
mapdg=np.loadtxt('dat/map_dg.dat')


# In[125]:

sns.set(context="paper", font="Open Sans",rc={"figure.figsize": (6,2)})
sns.set_style("white")
fig, ((ax1, ax2)) = plt.subplots(1, 2, sharex=False, sharey=True)
ax1.imshow(mapsgs,cmap='RdBu_r',aspect='auto')
# ax1.tick_params(axis='x',which='both',bottom='on',top='off',labelbottom='off')
ax1.set_title('One random SGS realization',fontsize=12)
ax1.set_xticklabels(['0','0','250','500','750','1000'])
ax1.set_yticklabels(['0','0','50','100','150','200','250','300'])
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Distance (m)')
ssim_sgs=ssim(G_REF[:,3].reshape(301,200,order='F')[210:270], G_SGS[:,3].reshape(301,200,order='F')[210:270])
ax2.text(0.356,0.17,'SSIM=0.82',fontsize=10,transform=fig.transFigure,backgroundcolor='white')
ax2.imshow(mapdg,cmap='RdBu_r',aspect='auto')
# ax2.tick_params(axis='x',which='both',bottom='on',top='off',labelbottom='off')
ax2.set_title('Final inversion result',fontsize=12)
ax2.set_xticklabels(['0','0','250','500','750','1000'])
ax2.set_xlabel('Distance (m)')
ssim_dg=ssim(G_REF[:,3].reshape(301,200,order='F')[210:270], G_DG[:,3].reshape(301,200,order='F')[210:270])
ax2.text(0.777,0.17,'SSIM=0.89',fontsize=10,transform=fig.transFigure,backgroundcolor='white')


# In[126]:

fig.savefig('ssim_res.pdf', transparent=True, bbox_inches='tight', pad_inches=0.05)


# In[ ]:



