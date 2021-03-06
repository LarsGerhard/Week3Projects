from numpy import linspace, array, sign

from scipy.constants import g

import numpy as np

m = 10

c = 0.2


def falling(t, X):
    """
    RATE_FUNC for Newton's 2nd Law  F = ma

    2nd order ODE
    a = d2x/dt2 = F/m

    """
    #  unpack

    y, v = X

    # compute derivatives
    dy = v
    dv = -g - sign(v) * c * v ** 2

    # pack rate array
    rate = array([dy, dv])

    return rate


# set some initial conditions
y0 = 100
v0 = 20
Y0 = [y0, v0]  # pack the i.c. into a column vector

# set the time interval for solving
Tstart = 0
Tend = 10  # s

# Form Time array

T = linspace(Tstart, Tend, 100)

# solve the ODE
from scipy.integrate import odeint

X = odeint(falling, Y0, T, tfirst=True)

# unpack the results. In the output array, variables are columns, times are rows
y = X[:, 0]
v = X[:, 1]

# make some nice plots
from matplotlib.pyplot import plot, xlabel, ylabel, legend, show, figure, subplot, xlim

plot(T, y, label='Height')
plot(T, v, label='Velocity')
xlabel('Seconds')
ylabel('m or m/s')
legend()
show()
