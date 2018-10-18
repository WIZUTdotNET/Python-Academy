import matplotlib.pyplot as plt
import scipy.fftpack as fft
import numpy as np
from matplotlib.widgets import Slider 

A0 = 1
T = 2
w = (2 * np.pi) / T
fi = 0

fig,ax = plt.subplots()
plt.subplots_adjust(left=0.25,bottom=0.25)

plt.axis([0, (2 * np.pi - np.pi)/2,-2,2])

x = np.linspace(0, 2 * np.pi, 1000)
yt = A0 * np.sin( w * x + fi)

#plt.subplot('211')
l, = plt.plot(x,yt)
#plt.subplot('212')
#plt.plot(x,np.abs(fft.fft(yt)))

axcolor = 'lightgoldenrodyellow'
var_handler = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

var1 = Slider(var_handler, 'Amplitude', 0.0,2.0,valinit=1,valstep=0.2)

def update(val):
    A = var1.val
    l.set_ydata(A * np.sin( w * x + fi))
    fig.canvas.draw_idle()
    
var1.on_changed(update)
    
plt.show()



