from pylab import plot, errorbar, show
fil = open('curves.txt')
all = fil.readlines()
t = []
m = []
b = []
db = []
for l in all:
    s = l.split()
    t.append(int(s[0]))
    m.append(float(s[1]))
    b.append(float(s[2]))
    db.append(float(s[3]))

plot(t,m)
plot(t,b,'o')
errorbar(t,b,yerr=db,linestyle='none')

show()


