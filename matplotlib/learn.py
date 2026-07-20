import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

x=[1,2,3,4]
y=[2,4,6,8]

#plot the set of x and set of y  plot(x,y) 
## color => color of curve (hex,colorname)
plt.plot(x,y,color="red")

#title to our graph which will shown as heading
##plt.title('our first graph', fontdict={ 'fontname':'Comic Sans MS' , "fontsize":20})
plt.title('our first graph', fontdict={"fontsize":20})
#title to xaxis
plt.xlabel('X')
#title to yaxis
plt.ylabel('Y')

### tick should set after ploting plt.plot(x,y)
### tick should not be agressively equi distance
#x ticks (x number line numbers)
plt.xticks([1,2,3,4])
#y ticks (y number line numbers)
plt.yticks([2,4,6,8,10])

#show plot
plt.show()