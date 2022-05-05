#prototype kalman filter visulisation 
from array import array
import re
import matplotlib as mp
from matplotlib import pyplot 
import numpy as np 
import random
import scipy
import pprint


def kalman_filter(x,y):
    """
    this function is used to implement the kalman filter
    it is quite simple, useing just the first estimate of the state
    """
    #initialize variables
    x_estimate = np.zeros(len(x))
    p_estimate = np.zeros(len(x))
    K = np.zeros(len(x))
    x_estimate[0] = x[0]
    p_estimate[0] = 1
    for i in range(1,len(x)):
        #prediction
        x_estimate[i] = x_estimate[i-1]
        p_estimate[i] = p_estimate[i-1] + 0.1
        #update
        K[i] = p_estimate[i]/(p_estimate[i]+0.3)
        x_estimate[i] = x_estimate[i] + K[i]*(y[i]-x_estimate[i])
        p_estimate[i] = (1-K[i])*p_estimate[i]
    return x_estimate

def visualize(x,y,x_estimate):
    mp.pyplot.plot(x,y,'r.',label='measurement')
    mp.pyplot.plot(x,x_estimate,'b-',label='estimate')
    mp.pyplot.legend()
    mp.pyplot.show()

def generate_sin_wave(n):
    """
    this function is used to generate a sin wave
    to change the frequency of the sin wave, change the value of
    n in the generate_sin_wave_with_noise function
    """
    x = np.linspace(0,10,n)
    y = np.sin(x)
    return x,y

def noise(z):
    """
    function to generate noise
    to change the amplitude of the noise change n
    """
    return np.random.normal(0,1,z)

def genrate_sin_wave_with_noise(n):
    n = n
    x,y = generate_sin_wave(n)
    z = n
    y = y + noise(z)
    return x,y

genrate_sin_wave_with_noise(100)
x,y = genrate_sin_wave_with_noise(100)
x_estimate = kalman_filter(x,y)
visualize(x,y,x_estimate)