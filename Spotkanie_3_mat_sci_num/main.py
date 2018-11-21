import matplotlib.pyplot as plt
from scipy.fftpack import fft
from numpy import sin, linspace, pi,abs
from matplotlib.widgets import Slider,Button 

#Parametry sinusoidy
A0 = 1 #Amplituda
T = 2 * pi  #Okres
w = (2 * pi) / T #predkosc katowa
fi = 0 #kat

x = linspace(0, 2 * pi, 1000) #tworzymy przestrzen argumentow
yt = A0 * sin(w * x + fi ) #Dla kazdego argumentu obliczamy wartosc funkcji sin
fig,(ax1,ax2) = plt.subplots(2,1,sharex=True) #tworzymy instancję okna (fig) oraz subplota (ax)

#Zwiekszamy odstepy miedzy wykresami w oknie
plt.subplots_adjust(left=0.25,bottom=0.25)
fig.suptitle("Sine wave and fft",fontsize=16)

#Podajemy granice wykresow
ax1.axis([0, 2*pi,-2,2])
ax2.axis([0, 2*pi,0,2])

#labels for sine wave
ax1.set_ylabel('Amplitude')
ax1.set_xlabel('Time')

#labels for fft
ax2.set_ylabel('Amplitude')
ax2.set_xlabel('Frequency')


#Draw sine wave and fft
lsin, = ax1.plot(x,yt)
lfft, = ax2.plot(x,abs(fft(yt)))

#Sliders handlers to change A,T and fi manually. Args -> size, text, range etc.
S_Amplitude = Slider(plt.axes([0.25, 0.12, 0.65, 0.03]), 'Amplitude', 0,2,valinit=1,valstep=0.2)
S_T = Slider(plt.axes([0.25, 0.06, 0.65, 0.03]), 'T', pi,3*pi,valinit=2*pi,valstep=0.1)
S_fi = Slider(plt.axes([0.25, 0.01, 0.65, 0.03]), 'fi', -2*pi,2*pi,valinit=0,valstep=0.1)

#Place button allowing user to reset above values
B_reset = Button(plt.axes([0.01, 0.01, 0.15, 0.05]), 'Reset',color='r')

#Function executed when button is clicked
def reset_b(event):
    S_Amplitude.reset()
    S_T.reset()
    S_fi.reset()

#function executed when any of values changed
def update(val):
    w = (2*pi)/S_T.val
    vec = S_Amplitude.val * sin( w * x + S_fi.val)
    lsin.set_ydata(vec)
    lfft.set_ydata(abs(fft(vec)))
    fig.canvas.draw_idle()

#These functions will check for any action from either sliders or button
#And execute functions passed as argument
S_Amplitude.on_changed(update)    
S_T.on_changed(update)
S_fi.on_changed(update)
B_reset.on_clicked(reset_b)

fig.savefig("ex.pdf")

#draw figure
plt.show()
