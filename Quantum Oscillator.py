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
from scipy.constants import hbar
from numpy import linspace, array, zeros, log, exp, sin, cos, sqrt, pi, e
from matplotlib.pyplot import plot, xlabel, ylabel, legend, show, figure, subplot, xlim

"""Set parameters for the problem"""

V0 =
a =
hbar =
m =

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
    dpsi =
    dpsi_p =

    # pack rates into column vector
    rate = array([dpsi, dpsi_p])
    return rate


"""2) Use odeing to solve a test case for  E = 413 eV. Set the initial 
values of $\psi(x=-10a)=0$ and $\psi'(x=-10a)=1$ (the first derivative 
is arbitrary since the solutions are equivalent to a normalization factor)

Plot over the range -5a < x < 5a 

"""

from matplotlib.pyplot import plot, xlim

psi0 =
dpsi0 =
Y0 = array([p0, dp0])  # pack the i.c. into array

# set the space interval for solving
Xstart =
Xend =

# Form space array with 100 points to solve the diff eq

X =

# solve the ODE for 3 values of E and
# make some nice plots


E =
solution = odeint()
# unpack
psi = solution[:, 0]
dpsi = out[:, 1]

plot(X, psi)
xlim(-5 * a, 5 * a)

"""3) A crude way to find the ground-state energy: Let's assume we're able to 
establish (e.g. from solving the square well) that the ground state energy
$E_o$ is in the range 100 to 200 eV. The correct value of $E$ will give $\psi(x=+10a)=0$.

a) Create a loop with E  increasing by steps of 2 eV in this range. 

b) Inside the loop (ie for each value of E), solve Schrodinger with i.c. as before.

c) Print out E and $\psi(x=+10a)$ at each step in the loop 
(what is the last value of the psi array?). Selecting the value of E that comes cloeses by inspecting the output.
"""

for E in arange():
    ...

"""4) Now get fancy and create a function of E that returns $\psi(x=+10a)$. Use brenq to solve for E. """


def PsiEnd(E):
    ...
    return psi[-1]


E0 = brentq(...)