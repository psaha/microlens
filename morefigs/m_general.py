def delimitate (tip):
    print str(tip)*70
    
def print_format (script_name, input_set):
    delimitate ("=")
    print "Format:"
    print "> python ", script_name, input_set
    delimitate ("-")

def in_sphere (point, center, radius):
    x, y, z = point[0]-center[0], point[1]-center[1], point[2]-center[2]
    if (x**2+y**2+z**2) > radius**2:
        ok = False
    else:
        ok = True
    return ok

def load_npz(name):
    file_input = numpy.load(name)
    print file_input.files()

    

def status (previous, counting, total_number):
    if counting > previous * total_number/100.:
        print previous,"%"
        previous = previous+1
    return previous

def simple_inquiry():
    answer = str(raw_input(">"))
    valid_answer = False
    while not valid_answer:
        if answer.lower() in ["yes", "y", "ye", "da","d", "ja", "si"]:
            yes = True
            valid_answer = True    
        if answer.lower() is "no":
            yes = False
            valid_answer = True
        if answer.lower() not in ["no","yes","y", "ye", "da","d", "ja", "si"]:
            valid_answer = False 
    return yes

import pylab as pt
def plot2d_scatter(x,y, title, x_label, y_label, file_save, non_zero, ratio, mark_zero_point):
    pt.plot(x,y,'r.')
    pt.xlabel(str(x_label))
    pt.ylabel(str(y_label))
    pt.title(str(title))
    if str(non_zero) == "non_zero" :
        pt.ylim(min(y)*ratio, max(y)*ratio)
        pt.xlim(min(x)*ratio, max(y)*ratio)
    else:
        pt.xlim(min(x), max(x)*ratio)
        pt.ylim(0, max(y)*ratio)
    if str(mark_zero_point) == "mark_zero_point":
        pt.plot(0,0,'bo')
    #pt.show()
    #plt.legend((legend1, legend2),'upper center', shadow=True, fancybox=True)
    pt.savefig(file_save, close = "True")
    pt.clf()
    pt.cla()

def quick_plot(x,y):
    pt.plot(x,y,'b.')
    pt.show()
    pt.clf()
    pt.cla()

def quick_plot_log(x,y, x_log, y_log):
    pt.plot(x,y,'b.')
    
    if x_log == True:
        pt.xscale('log')
    if y_log == True:
        pt.yscale('log')
    pt.xlim(min(x), max(x))
    pt.ylim(min(y), max(y))
    pt.show()
    pt.clf()
    pt.cla()

def plot_log(x,y, x_log, y_log, x_name, y_name):
    pt.plot(x,y,'b.')
    
    if x_log == True:
        pt.xscale('log')
    if y_log == True:
        pt.yscale('log')
    pt.xlim(min(x), max(x))
    pt.ylim(min(y), max(y))
    pt.xlabel(x_name)
    pt.ylabel(y_name)
    pt.show()
    pt.clf()
    pt.cla()

def plot_log_3(x,y1,y2,y3,x_log, y_log, x_name, y_name):
    
    pt.plot(x,y1,'b.')
    pt.plot(x,y2,'g.')
    pt.plot(x,y3,'r.')
    if x_log == True:
        pt.xscale('log')
    if y_log == True:
        pt.yscale('log')
    pt.xlim(min(x), max(x))
    pt.ylim(min(y3), max(y3))
    pt.xlabel(x_name)
    pt.ylabel(y_name)
    pt.show()
    pt.clf()
    pt.cla()

def quick_double_plot(x1,x2,y1,y2):
    pt.plot(x1,y1,'b.')
    pt.plot(x2,y2,'g.')
    pt.show()
    pt.clf()
    pt.cla()


def double_plot(x1,x2,y1,y2, x_label, y_label, legend1, legend2, save_name):
    pt.plot(x1,y1,'b.')
    pt.plot(x2,y2,'g.')
    pt.xlabel(str(x_label))
    pt.ylabel(str(y_label))
    pt.legend((legend1, legend2), 'upper right', shadow=False, fancybox=False)
    pt.savefig(save_name, close="True")
   # pt.show()
    pt.clf()
    pt.cla()
    
def double_plot_restricted(x1,x2,y1,y2,lim_x, lim_y,  x_label, y_label, legend1, legend2, save_name):
    pt.plot(x1,y1,'b.')
    pt.plot(x2,y2,'g.')
    pt.xlabel(str(x_label))
    pt.ylabel(str(y_label))
    pt.xlim(lim_x)
    pt.ylim(lim_y)
    pt.legend((legend1, legend2), 'upper right', shadow=False, fancybox=False)
    pt.savefig(save_name, close="True")
   # pt.show()
    pt.clf()
    pt.cla()

def limits_detection(x,y):
    limits_x = [-max([-min(x), max(x)]), max([-min(x), max(x)])]
    limits_y = [-max([-min(y), max(y)]), max([-min(y), max(y)])]
    if limits_x[1] >limits_y[1]:
        lo = limits_x
    else:
        lo = limits_y
    return lo
    
def four_subplots_3centered_1not(x1, y1, x2, y2, x3, y3, x4, y4,title, title2, x_label, y_label, save_name):
    
    pt.subplot(2,2, 1)
    pt.title(str(title))
    pt.plot(x1,y1, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.ylim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.xlabel(x_label[0])
    pt.ylabel(y_label[0])
    
    
    pt.subplot(2,2, 2)
    pt.plot(x2,y2, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x2,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.ylim(limits_detection(x3,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.xlabel(x_label[1])
    pt.ylabel(y_label[1])
    
    pt.subplot(2,2, 3)
    pt.plot(x3,y3, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.ylim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.xlabel(x_label[2])
    pt.ylabel(y_label[2])
    
    pt.subplot(2,2, 4)
    pt.plot(x4,y4, "g.")
    pt.plot([0],[0], "bo")
    pt.xlabel(x_label[3])
    pt.ylabel(y_label[3])
    #for redshift
    pt.xlim(0,5)
    
    pt.savefig(save_name)
    pt.clf()
    pt.cla()
    
def three_subplots_position(x1, y1, x2, y2, x3, y3, title, x_label, y_label, save_name):
    pt.subplot(2,2, 1)
    pt.title(str(title))
    pt.plot(x1,y1, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.ylim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.xlabel(x_label[0])
    pt.ylabel(y_label[0])
    
    
    pt.subplot(2,2, 2)
    pt.plot(x2,y2, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x2,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.ylim(limits_detection(x3,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.xlabel(x_label[1])
    pt.ylabel(y_label[1])
    
    pt.subplot(2,2, 3)
    pt.plot(x3,y3, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.ylim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.xlabel(x_label[2])
    pt.ylabel(y_label[2])
    
    pt.savefig(save_name)
    pt.clf()
    pt.cla()
    
def four_subplots_2_zoom(x1, y1, x2, y2, x3, y3, x4, y4,title, title2, x_label, y_label, original_scale, zoom_limits, save_name):
    
    pt.subplot(2,2, 1)
    pt.title(str(title))
    pt.plot(x1,y1, "r.")
    pt.plot([0],[0], "bo")
 #   pt.xlim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
 #   pt.ylim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.xlabel(x_label[0])
    pt.ylabel(y_label[0])
    pt.xlim(original_scale[0], original_scale[1])
    
    pt.subplot(2,2, 2)
    pt.plot(x2,y2, "r.")
    pt.plot([0],[0], "bo")
 #   pt.xlim(limits_detection(x2,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
 #   pt.ylim(limits_detection(x3,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.xlabel(x_label[1])
    pt.ylabel(y_label[1])
    pt.xlim(zoom_limits[0], zoom_limits[1])
    
    pt.subplot(2,2, 3)
    pt.plot(x3,y3, "g.")
    pt.plot([0],[0], "bo")
  #  pt.xlim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
  #  pt.ylim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.xlabel(x_label[2])
    pt.ylabel(y_label[2])
    pt.xlim(original_scale[0], original_scale[1])
    
    pt.subplot(2,2, 4)
    pt.plot(x4,y4, "g.")
    pt.plot([0],[0], "bo")
    pt.xlabel(x_label[3])
    pt.ylabel(y_label[3])
    #for redshift
    pt.xlim(zoom_limits[0], zoom_limits[1])
    
    pt.savefig(save_name)
    pt.clf()
    pt.cla()

def six_subplots_3centered_3not(x1, y1, x2, y2, x3, y3, x4, y4,x5,y5,x6,y6, title, title2, x_label, y_label, save_name):
    
    pt.subplot(3,2, 1)
    pt.title(str(title))
    pt.plot(x1,y1, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.ylim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.xlabel(x_label[0])
    pt.ylabel(y_label[0])
    
    
    pt.subplot(3,2, 2)
    pt.plot(x2,y2, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x2,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.ylim(limits_detection(x3,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.xlabel(x_label[1])
    pt.ylabel(y_label[1])
    
    pt.subplot(3,2, 3)
    pt.plot(x3,y3, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.ylim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.xlabel(x_label[2])
    pt.ylabel(y_label[2])
    
    pt.subplot(3,2, 4)
    pt.plot(x4,y4, "g.")
    pt.plot([0],[0], "bo")
    pt.xlabel(x_label[3])
    pt.ylabel(y_label[3])
    #for redshift
    pt.xlim(0,5)
    
    pt.subplot(3,2, 5)
    pt.plot(x5,y5, "b.")
    pt.plot([0],[0], "bo")
    pt.xlabel(x_label[4])
    pt.ylabel(y_label[4])
    pt.xlim(0,5)
    
    pt.subplot(3,2, 6)
    pt.plot(x6,y6, "b.")
    pt.xlabel(x_label[5])
    pt.ylabel(y_label[5])
    pt.xlim(0,1)
    
    pt.savefig(save_name)
    pt.clf()
    pt.cla()
    
def six_subplots_6centered_0not(x1, y1, x2, y2, x3, y3, x4, y4,x5,y5,x6,y6, title, title2, x_label, y_label, save_name):
    
    pt.subplot(3,2, 1)
    pt.title(str(title))
    pt.plot(x1,y1, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.ylim(limits_detection(x1,y1)[0]*1.4, limits_detection(x1,y1)[1]*1.4)
    pt.xlabel(x_label[0])
    pt.ylabel(y_label[0])
    
    
    pt.subplot(3,2, 2)
    pt.plot(x2,y2, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x2,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.ylim(limits_detection(x3,y2)[0]*1.4, limits_detection(x2,y2)[1]*1.4)
    pt.xlabel(x_label[1])
    pt.ylabel(y_label[1])
    
    pt.subplot(3,2, 3)
    pt.plot(x3,y3, "r.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.ylim(limits_detection(x3,y3)[0]*1.4, limits_detection(x3,y3)[1]*1.4)
    pt.xlabel(x_label[2])
    pt.ylabel(y_label[2])
    
    pt.subplot(3,2, 4)
    pt.plot(x4,y4, "g.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x4,y4)[0]*1.4, limits_detection(x4,y4)[1]*1.4)
    pt.ylim(limits_detection(x4,y4)[0]*1.4, limits_detection(x4,y4)[1]*1.4)
    pt.ylabel(y_label[3])
    pt.xlabel(x_label[3])
    #for redshift
    
    pt.subplot(3,2, 5)
    pt.plot(x5,y5, "b.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x5,y5)[0]*1.4, limits_detection(x5,y5)[1]*1.4)
    pt.ylim(limits_detection(x5,y5)[0]*1.4, limits_detection(x5,y5)[1]*1.4)
    pt.xlabel(x_label[4])
    pt.ylabel(y_label[4])
    
    pt.subplot(3,2, 6)
    pt.plot(x6,y6, "b.")
    pt.plot([0],[0], "bo")
    pt.xlim(limits_detection(x6,y6)[0]*1.4, limits_detection(x6,y6)[1]*1.4)
    pt.ylim(limits_detection(x6,y6)[0]*1.4, limits_detection(x6,y6)[1]*1.4)
    pt.xlabel(x_label[5])
    pt.ylabel(y_label[5])
    
    pt.savefig(save_name)
    pt.clf()
    pt.cla()

    
    
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

def quick_plot_3d(x,y,z):

    fig = pylab.figure()
    ax = Axes3D(fig)
    
    ax.scatter(x, y, z)
    
    pyplot.show()
#    pyplot.clf()
#    pyplot.cla()

def plot_3d(x,y,z, title, x_title, y_title, z_title,  mark_zero):
    fig = pylab.figure()
    ax  = Axes3D(fig)
    ax.scatter(x,y,z)
    
    ax.set_title(title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_zlabel(z_title)
    if mark_zero =="mark_zero":
        ax.scatter([0],[0],[0])
    pyplot.show()
#    pyplot.clf()
#    pyplot.cla()

    
import os    
def make_directory(name):
    if not os.path.exists(str(name)):
        os.makedirs(str(name))
    else:
        delimitate("-")
        print "Directory already exists"
        print "Overwrite?"
        if not simple_inquiry():
            print "Specify new name (please include path):"
            name = raw_input(">")
        os.makedirs(str(name))    
            
import numpy            
def max_density_data(density_list, index_list, position_list, mass_list, redshift):
    maximum_density     = density_list.max()
    index_m_density     = index_list[numpy.where(density_list.max() == density_list)[0]]
    position_m_density  = position_list[numpy.where(density_list.max() == density_list)[0]]
    mass_m_density      = mass_list[numpy.where(density_list.max() == density_list)[0]]
    
    
def distance(position1, position2, scale, units):
    distanta = (sum((position1 - position2)**2))**(0.5)
    rescaled = distanta*scale
    return rescaled, units


def reverse(lista):
    ista = lista
    i=0
    while i < len(ista)/2:
        third_glass = ista[i]
        ista[i] = ista[-i-1]
        ista[-i-1] = third_glass
        i = i+1
    return ista

import time    
def time_this_thing(string):
    print "-"*70
    print "Evaluating line:", string
    start = time.time()
    data = eval(string)
    elapsed = time.time() - start
    if elapsed < 1:
        print elapsed, "s"
    else:
        if elapsed < 60:
            print int(elapsed), "s"
        else:
            if elapsed <3600:
                print int(elapsed)/60, "m", int(elapsed)%60, 's'
            else:
                print int(elapsed)/3600, "h", (int(elapsed)%3600)/60, "m", (int(elapsed)%3600)%60, "s"
    return data

def extract_redshift(string):
    posi = string.find('.z')
    zet  = float(string[posi+2:posi+7])
    return zet

def histogram_overlap(x,y, binss, name):
    pyplot.hist(x,binss,cumulative = False, histtype ="step", color = "blue", alpha = 0.5, label = r"cusp coeff. = 0.6")
    pyplot.hist(y,binss, cumulative = False, histtype ="step", color = "green", alpha = 0.5, label = r"cusp coeff. = 1.0")
    pyplot.xlabel('ratio', fontsize=18)
    pyplot.ylabel('N( > ratio)', fontsize=18)
    pyplot.legend()
    pyplot.show()
