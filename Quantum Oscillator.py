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
from scipy.optimize import newton
from numpy import linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot, xlim

"""Set parameters for the problem"""

V0= 50
a=1.e-11 # m
hbar=197*1e-9 # hbar-c
m=0.511*1e6 # eV/c2

"""1) Write down the time-independent Schrodinger equation for this problem and 
convert it from a second-order equation to two first-order ones 
(ie for $\psi$ and $\psi\prime$). 
Follow the lotka example in python to write a two-variable rate function 
for dpsi and dpsi_p.

Create our diff eq
"""


def schrodinger(x, V, E):
    # unpack
    psi = V[0]
    psi_p = V[1]

    # compute rates
    Pot = V0 * (x ** 2 / a ** 2)
    dpsi_p = -(2 * m / hbar ** 2) * (E - Pot) * psi
    dpsi = psi_p

    # pack rates into column vector
    rate = array([dpsi, dpsi_p])
    return rate

def PsiEnd(E):
    solution = odeint(schrodinger, Y0, X, args=(E,), tfirst=True)
    # unpack
    psi = solution[:, 0]
    dpsi = solution[:, 1]


    return psi[-1]


"""2) Use odeing to solve a test case for  E = 413 eV. Set the initial 
values of $\psi(x=-10a)=0$ and $\psi'(x=-10a)=1$ (the first derivative 
is arbitrary since the solutions are equivalent to a normalization factor)

Plot over the range -5a < x < 5a 

"""

psi0 = 0
dpsi0 = 1
Y0 = array([psi0, dpsi0]) # pack the i.c. into array


# set the space interval for solving
Xstart=-10*a
Xend = 10*a # 2 years

# Form Time array

X = linspace(Xstart,Xend,100)

# solve the ODE for 3 values of E and
# make some nice plots


E = 66.62830653653002

Elevel = newton(PsiEnd,E)

solution = odeint(schrodinger, Y0, X, args=(Elevel,), tfirst=True)
# unpack
psi = solution[:,0]
dpsi = solution[:,1]

plot(X[30:-30],psi[30:-30])
xlim(-5*a,5*a)
show()

