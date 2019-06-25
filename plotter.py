import matplotlib.pyplot as plt
import csv
from scipy.stats import kde
import numpy as np
z=[]
for i in range(1,2):
    x = []
    y = []
    with open('Plot/'+str(i)+'ul.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    
    # plt.plot(x,y, label='Loaded from file!')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Interesting Graph\nCheck it out')
    # plt.legend()
    # plt.show()
    outpath = "Plot/density/"
    x=np.array(x)
    y=np.array(y)
    #print (np.mean(x), np.mean(y))
    # Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
    nbins=100
    k = kde.gaussian_kde([x,y])
    xi, yi = np.mgrid[x.min()*0:x.max():nbins*1j, y.min()*0:y.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    
    # Make the plot
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
    plt.draw()
    #fig.savefig(path.join(outpath,str(i)+"ul.jpeg"))+
    print(i)
    #plt.savefig('Plot/'+str(i)+'ur.png', dpi=100)
    plt.show()