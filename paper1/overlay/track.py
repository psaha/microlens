from pylab import imread, imshow, plot, show
img = imread('causticmap.jpg')
imshow(img)
plot([100, 500],[300, 200],c='r')
show()

