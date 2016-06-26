import numpy as np 
import matplotlib.pyplot as plt 
from sys import exit

burn_in = 100

chains = np.genfromtxt('dd.chain', skip_header=burn_in, skip_footer=1)

spec = 'xm'
fs = 22

f, axarr = plt.subplots(2,2, figsize=(15,15))

axarr[0,0].plot(chains[:,6], chains[:,7], spec)
axarr[0,0].set_xlim(10, 30)
axarr[0,0].set_ylim(0, 1)
axarr[0,0].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[0,0].set_ylabel('$\mathtt{R_n/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,7]), np.std(chains[:,7])), fontsize=fs)

axarr[0,1].plot(chains[:,8], chains[:,9], spec)
axarr[0,1].set_xlim(-1, 1)
axarr[0,1].set_ylim(-1, 1)
axarr[0,1].set_xlabel('$\mathtt{\\alpha/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,8]), np.std(chains[:,8])), fontsize=fs)
axarr[0,1].set_ylabel('$\mathtt{\\beta/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,9]), np.std(chains[:,9])), fontsize=fs)

axarr[1,1].plot(chains[:,3], chains[:,4], spec)
axarr[1,1].set_xlim(750, 850)
axarr[1,1].set_ylim(450, 550)
axarr[1,1].set_xlabel('$\mathtt{Start\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,3]), np.std(chains[:,3])), fontsize=fs)
axarr[1,1].set_ylabel('$\mathtt{End\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,4]), np.std(chains[:,4])), fontsize=fs)

axarr[1,0].plot(chains[:,6], chains[:,5], spec)
axarr[1,0].set_xlim(10, 30)
axarr[1,0].set_ylim(0.5, 2.5)
axarr[1,0].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[1,0].set_ylabel('$\mathtt{Norm\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,5]), np.std(chains[:,5])), fontsize=fs)


plt.savefig('dd.eps')
plt.show()
