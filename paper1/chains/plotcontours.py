import numpy
import pylab


def plotcontours(array1,array2,CL,spec,opaque,description):
	import numpy as np

	import matplotlib.pyplot as plt
	from matplotlib.patches import Ellipse

	def plot_point_cov(points, nstd=2, ax=None, **kwargs):
	    """
	    Plots an `nstd` sigma ellipse based on the mean and covariance of a point
	    "cloud" (points, an Nx2 array).

	    Parameters
	    ----------
	        points : An Nx2 array of the data points.
	        nstd : The radius of the ellipse in numbers of standard deviations.
	            Defaults to 2 standard deviations.
	        ax : The axis that the ellipse will be plotted on. Defaults to the 
	            current axis.
	        Additional keyword arguments are pass on to the ellipse patch.

	    Returns
	    -------
	        A matplotlib ellipse artist
	    """
	    pos = points.mean(axis=0)
	    cov = np.cov(points, rowvar=False)
	    return plot_cov_ellipse(cov, pos, nstd, ax, **kwargs)

	def plot_cov_ellipse(cov, pos, nstd=2, ax=None, **kwargs):
	    """
	    Plots an `nstd` sigma error ellipse based on the specified covariance
	    matrix (`cov`). Additional keyword arguments are passed on to the 
	    ellipse patch artist.

	    Parameters
	    ----------
	        cov : The 2x2 covariance matrix to base the ellipse on
	        pos : The location of the center of the ellipse. Expects a 2-element
	            sequence of [x0, y0].
	        nstd : The radius of the ellipse in numbers of standard deviations.
	            Defaults to 2 standard deviations.
	        ax : The axis that the ellipse will be plotted on. Defaults to the 
	            current axis.
	        Additional keyword arguments are pass on to the ellipse patch.

	    Returns
	    -------
	        A matplotlib ellipse artist
	    """
	    def eigsorted(cov):
	        vals, vecs = np.linalg.eigh(cov)
	        order = vals.argsort()[::-1]
	        return vals[order], vecs[:,order]

	    if ax is None:
	        ax = plt.gca()

	    vals, vecs = eigsorted(cov)
	    theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))

	    # Width and height are "full" widths, not radius
	    width, height = 2 * nstd * np.sqrt(vals)
	    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, **kwargs)

	    ax.add_artist(ellip)
	    return ellip

	if __name__ == '__main__':
	    #-- Example usage -----------------------
	    # Generate some random, correlated data
	    #f1 = np.genfromtxt('CC.chain',skip_header=1000)
	    #points = f1[:,2:4]
	    #print numpy.shape(points)
	    #points = np.random.multivariate_normal(
	    #        mean=(1,1), cov=[[0.4, 9],[9, 10]], size=1000
	    #        )
	    # Plot the raw points...
	    points = np.transpose([array1,array2])
	    x, y = points.mean(axis=0)
	    plt.plot(x, y, spec,label=description)
	    xx,yy = points.std(axis=0)
	    # Plot a transparent 3 standard deviation covariance ellipse
	    plot_point_cov(points, nstd=CL, alpha=opaque, color=spec)
	    plt.xlim(x-(CL+0.2)*xx,x+(CL+0.2)*xx)
	    plt.ylim(y-(CL+0.2)*yy,y+(CL+0.2)*yy)

burn=1000
files = ['GC','DC','CC']
spec = ['g','b','r']
labels = ['Gaussian Disk','Uniform Disk','Crescent']
for i in range(len(files)):
	f1 = numpy.genfromtxt(files[i]+'.chain',skip_header=burn)
	f2 = numpy.genfromtxt(files[i]+'2.chain',skip_header=burn)

	Rp = f1[:,2]
	Rn = f1[:,3]
	a = f1[:,4]
	b = f1[:,5]
	Rhalf = f2[:,2]

	points = [Rhalf,Rn/Rp]
	points = numpy.transpose(points)
	plotcontours(Rhalf,Rn/Rp,2,spec[i],0.8,labels[i])
pylab.legend(loc=4)
pylab.ylim(0,1.3)
pylab.xlim(20,65)
pylab.xlabel('$\mathtt{R_{1/2}}$',fontsize=18)
pylab.ylabel('$\mathtt{R_n/R_p}$',fontsize=18)
pylab.savefig('Rhalf_RnRp.eps')
pylab.show()

