import numpy as np 
import matplotlib.pyplot as plt 
import sys

burn_in = 300
infile = 'cc_forward.chain'

if len(sys.argv)>1:
	infile = sys.argv[1]
	print "Analyzing file: ", infile

chains = np.genfromtxt(infile, skip_header=burn_in, skip_footer=1)

spec = 'xm'
fs = 22

f, axarr = plt.subplots(3,2, figsize=(15,22))

axarr[0,0].plot(chains[:,6], chains[:,7], spec)
axarr[0,0].set_xlim(1, 100)
axarr[0,0].set_ylim(0, 1)
# axarr[0,0].set_ylim(-20, -5)
axarr[0,0].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[0,0].set_ylabel('$\mathtt{R_n/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,7]), np.std(chains[:,7])), fontsize=fs)
axarr[0,0].set_title('$\mathtt{Best\ chi-square = %1.3f}$'%np.amin(chains[:,1]), fontsize=22)

axarr[0,1].plot(chains[:,8], chains[:,9], spec)
axarr[0,1].set_xlim(-1, 1)
axarr[0,1].set_ylim(-1, 1)
axarr[0,1].set_xlabel('$\mathtt{\\alpha/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,8]), np.std(chains[:,8])), fontsize=fs)
axarr[0,1].set_ylabel('$\mathtt{\\beta/R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,9]), np.std(chains[:,9])), fontsize=fs)
axarr[0,1].set_title('$\mathtt{Sample\ Size=%i}$'%len(chains), fontsize=22)

axarr[1,1].plot(chains[:,3], chains[:,4], spec)
# axarr[1,1].set_xlim(750, 850)
# axarr[1,1].set_ylim(450, 550)
axarr[1,1].set_xlim(50, 150)
axarr[1,1].set_ylim(350, 450)
axarr[1,1].set_xlabel('$\mathtt{Start\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,3]), np.std(chains[:,3])), fontsize=fs)
axarr[1,1].set_ylabel('$\mathtt{End\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,4]), np.std(chains[:,4])), fontsize=fs)

axarr[1,0].plot(chains[:,6], chains[:,5], spec)
axarr[1,0].set_xlim(1, 100)
axarr[1,0].set_ylim(0.5, 2.5)
axarr[1,0].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[1,0].set_ylabel('$\mathtt{Norm\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,5]), np.std(chains[:,5])), fontsize=fs)

axarr[2,0].plot(chains[:,6], chains[:,3], spec)
axarr[2,0].set_xlim(1, 100)
axarr[2,0].set_ylim(50, 150)
axarr[2,0].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[2,0].set_ylabel('$\mathtt{Start\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,3]), np.std(chains[:,3])), fontsize=fs)

axarr[2,1].plot(chains[:,6], chains[:,4], spec)
axarr[2,1].set_xlim(1, 100)
axarr[2,1].set_ylim(350, 450)
axarr[2,1].set_xlabel('$\mathtt{R_p\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,6]), np.std(chains[:,6])), fontsize=fs)
axarr[2,1].set_ylabel('$\mathtt{End\ [mean=%1.2f;\ std=%1.2f]}$'%(np.mean(chains[:,4]), np.std(chains[:,4])), fontsize=fs)

plt.savefig(infile.replace('.chain', '.eps'))
# plt.show()
