import numpy as np 
import matplotlib.pyplot as plt 
from sys import exit

burn_in = 100

chains = np.genfromtxt('test.chain', skip_header=burn_in)

i = 7
j = 8

f, axarr = plt.subplots(2,1, figsize=(6,12))

axarr[0].plot(chains[:,5], chains[:,6])
axarr[0].set_xlim(10, 30)
axarr[0].set_ylim(0, 1.0)
axarr[0].set_xlabel('$\mathtt{R_p}$', fontsize=16)
axarr[0].set_ylabel('$\mathtt{R_n/R_p}$', fontsize=16)


axarr[1].plot(chains[:,7], chains[:,8])
axarr[1].set_xlim(-1, 1)
axarr[1].set_ylim(-1, 1)
axarr[1].set_xlabel('$\mathtt{\\alpha/R_p}$', fontsize=16)
axarr[1].set_ylabel('$\mathtt{\\beta/R_p}$', fontsize=16)


plt.savefig('mcmc.eps')
plt.show()