# Ising-model
Hi!
This is a simple python project using only numpy, math and matplotlib libraries.


### Initial Lattice
First we make a 20x20 , 10x10 matrices with randomly chosen arrays of 1, -1.

*Note: This program doesn't work well in the low temperatures.*


### Steps
In each iterattion we change an array to the average of its neighbors , OR NOT.
The condition under which the spin(array) flips is that the flip reduces the energy:
![cond11](https://user-images.githubusercontent.com/47470358/120798982-61480780-c553-11eb-87a8-9dc9c1d97bf0.png)
For being closer to reality we add a random flip (... or x<y).


And we do this for about 40000 iterations, hoping to be around the equilibriu, point when we do our calculations.

