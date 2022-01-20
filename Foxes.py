"""
Created on Wed Jan 30 13:11:41 2019

@author: esalathe

Example of a coupled system of ODEs to model the population dynamics of a
preditor-prey system (foxes and rabbits)
"""

from scipy.integrate import odeint
from numpy import linspace, array
from matplotlib.pyplot import plot, xlabel, ylabel, legend, show, figure, subplot


def lotka(t, V):
    # Poulation growth of Rabbits and Foxes
    # Note that rabbits is first column, foxes second

    # unpack
    r = V[0]
    f = V[1]

    # compute rates
    dr = a * r - b * r * f
    df = e * b * r * f - c * f

    # pack rates into numpy array
    rate = array([dr, df])
    return rate


# set some parameters
a = 0.1
b = 0.01
c = 0.1
e = 0.2

# set initial conditions
rabbit0 = 100
fox0 = 10
Y0 = array([rabbit0, fox0])  # pack the i.c. into a numpy array

# set the time interval for solving
Tstart = 0
Tend = 365 * 2  # 2 years

# Form Time array

T = linspace(Tstart, Tend, 500)

# solve the ODE
X = odeint(lotka, Y0, T, tfirst=True)

# unpack the results. In the output array, variables are columns, times are rows
rabbits = X[:, 0]
foxes = X[:, 1]

# make some nice plots
figure()

subplot(2, 1, 1)
plot(T, rabbits, label='Rabbits')
plot(T, foxes, label='Foxes')
xlabel('Day')
ylabel('Population')
legend()

subplot(2, 1, 2)
plot(rabbits, foxes)
xlabel('Rabbits')
ylabel('Foxes')

show()
