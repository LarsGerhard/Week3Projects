"""
Our goal is to solve the one-dimensional, time-independent Schrodinger
equation wave function for an electron in a harmonic (i.e., quadratic) potential

Note that in theory the wavefunction goes all the way out to x = ±∞, but you can
get good answers by using a large but finite interval. Try using x = −10a to +10a,
with the wavefunction ψ = 0 at both boundaries. (In effect, you are putting the
harmonic oscillator in a 20a wide box with impenetrable walls.) The wavefunction
is real everywhere, so you don’t need to use complex variables, and you can use
evenly spaced points in x for the solution (use linspace to create 100 points
from -10a to +10a). The first derivative of the wave function is arbitrary since
the solutions are equivalent relative to a normalizing factor, so set it to 1.

Load modules
"""

from scipy.integrate import odeint
from scipy.constants import hbar, eV, c
from numpy import linspace, arange, array, zeros, log, exp, sin, cos, sqrt, pi, e
from matplotlib.pyplot import plot, xlabel, ylabel, legend, show, figure, subplot, xlim

"""Set parameters for the problem"""

V0 = 20
a = 1.E-11

m = eV / c**2

"""\1) Write down the time-independent Schrodinger equation for this problem and 
convert it from a second-order equation to two first-order ones 
(ie for $\psi$ and $\psi\prime$). 
Follow the lotka example in python to write a two-variable rate function 
for dpsi and dpsi_p.

Create our diff eq
"""


def schrodinger(x, V):
    # unpack
    psi = V[0]
    psi_p = V[1]

    # compute rates
    dpsi = psi_p
    V = V0 * (x**2 / a**2)
    dpsi_p =  - 2 * (m / hbar) * (E - V) * psi

    # pack rates into column vector
    rate = array([dpsi, dpsi_p])
    return rate


"""2) Use odeing to solve a test case for  E = 413 eV. Set the initial 
values of $\psi(x=-10a)=0$ and $\psi'(x=-10a)=1$ (the first derivative 
is arbitrary since the solutions are equivalent to a normalization factor)

Plot over the range -5a < x < 5a 

"""

from matplotlib.pyplot import plot, xlim

psi0 = 0
dpsi0 = 1
Y0 = array([psi0, dpsi0])  # pack the i.c. into array

# set the space interval for solving
Xstart = -10
Xend = 10

# Form space array with 100 points to solve the diff eq

X = linspace(Xstart,Xend, 100)

# solve the ODE for 3 values of E and
# make some nice plots


E = 100
solution = odeint(schrodinger, Y0, X,  tfirst = True)
# unpack
psi = solution[:, 0]
dpsi = solution[:, 1]

plot(X, psi)
xlim(-5 * a, 5 * a)

