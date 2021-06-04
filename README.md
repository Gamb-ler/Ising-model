# Ising-model
Hi!
This is a simple python project using only numpy, math and matplotlib libraries.


### Initial Lattice
First we make a 20x20 , 10x10 matrices with randomly chosen arrays of 1, -1.

*Note: This program doesn't work well at low temperatures.*


### Steps
In each iteration we change an array to the average of its neighbors , OR NOT.
The condition under which the spin(array) flips is that the flip reduces the energy(de):

![cond11](https://user-images.githubusercontent.com/47470358/120799462-04991c80-c554-11eb-9524-12ea4f849258.png)

For being closer to reality we add a random flip (... or x<y).


And we do this for about 40000 iterations, hoping to be around the equilibrium point when we do our calculations.

### Calculations
When we are done with all the arrays, we calculate the wanted quantities ;eg. average energy, magnetisation per spin, specific heat capacity, magnetic susceptibility etc.

After that we change the system's temperature and do it all again.

At last we plot the quantities vs. temperature , ...<br><br>

and the end :)

