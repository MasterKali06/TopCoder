"""
Problem Statement
In this problem we will consider some simple molecules from organic chemistry. Our molecules will consist of four
elements: hydrogen (H), oxygen (O), nitrogen (N), and carbon (C).
In each molecule, some pairs of atoms are held together by bonds. The following simple rules apply in all our molecules:
Each bond connects exactly two distinct atoms.
There can be multiple bonds connecting the same pair of atoms.
Each H atom has exactly 1 bond.
Each O atom has exactly 2 bonds.
Each N atom has exactly 3 bonds.
Each C atom has exactly 4 bonds.
Some example drawings of molecules that follow these rules are shown below. (The symbols '-' and '|' represent bonds,
'=' is used to represent two bonds between the same two atoms.)
          H       H H         H
          |       | |         |
H-O-H   H-C-H   H-C-C-O   H-C=C-H
          |       | | |     |
          H       H H H     H
With just a single bond, a hydrogen (H) atom can never hold a molecule together. Thus, if we have a molecule and we take
away all hydrogen atoms, the rest of the molecule will still hold together.

You are given a description of a molecule from which somebody removed all the hydrogen atoms. Your task is to determine
and return the number of hydrogen atoms that were present in the given molecule. (This number is always unique.)

The molecule part you are given consists of n atoms. Each of these is an oxygen, nitrogen, or carbon. The atoms are
numbered from 0 to n-1. You are given a string atoms with n characters. Character i of atoms specifies the element of atom i.
There are m bonds between these atoms. You are given tuple (integer)s X and Y with m elements each. For each i between
0 and m-1, inclusive, there is a bond between atoms with numbers X[i] and Y[i].
    
Class: OrganicChemistry
Method: countHydrogens
Parameters: string, tuple (integer), tuple (integer)
Returns: integer
Method signature: def countHydrogens(self, atoms, X, Y):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Notes
-
The numbers n and m are not given explicitly. In your program, you can determine n as the length of atoms and m as the length of X and Y.
Constraints
-
atoms will have between 1 and 50 characters, inclusive.
-
Each character of atoms will be 'O', 'N', or 'C'.
-
X will have between 0 and 200 elements, inclusive.
-
Y will have the same number of elements as X.
-
Each element of X and Y will be between 0 and (the length of atoms)-1, inclusive.
-
For each i, X[i] will not be equal to Y[i].
-
X and Y will describe a valid molecule without hydrogens: all atoms will be held together by the bonds, and each atom
will have at most as many bonds as it should have in the complete molecule.

Examples
0)  
"O"
{}
{}
Returns: 2
This is the molecule from the first example drawing (water):
H-O-H
After we removed both hydrogen atoms, what remained was a single oxygen atom with no bonds.

1)
"C"
{}
{}
Returns: 4
The second example drawing (methane).
  H
  |
H-C-H
  |
  H

2) 
"CCO"
{0, 1}
{1, 2}
Returns: 6
The third example drawing (ethanol). We have three atoms (C, C, O) and two bonds (0-1 and 1-2). After adding back all
the hydrogens the molecule looks as follows:
  H H
  | |
H-C-C-O
  | | |
  H H H

3)
"CC"
{0, 0}
{1, 1}
Returns: 4
The fourth example (ethene, also called ethylene): two carbons connected by two bonds.
    H
    |
H-C=C-H
  |
  H

4)   
"OO"
{1, 1}
{0, 0}
Returns: 0
A molecule of oxygen (O2): two oxygen atoms and two bonds between them. There are no hydrogens anywhere.
O=O

5) 
"OOO"
{0, 1, 2}
{1, 2, 0}
Returns: 0
A molecule of ozone (O3): three oxygen atoms with bonds that form a triangle. Again, there are no hydrogens anywhere.
O-O
|/
O
6)

    
"CCCCCC"
{0, 1, 2, 3, 5, 4}
{1, 2, 3, 4, 0, 5}
Returns: 12
Cyclohexane: six carbon atoms that form a simple cycle.
  C-C
 /   \
C     C
 \   /
  C-C
7)

    
"CCCCCC"
{0, 0, 1, 2, 3, 5, 4, 4, 3}
{1, 1, 2, 3, 4, 0, 5, 5, 2}
Returns: 6
Benzene: six carbon atoms forming a cycle, but now three pairs of carbons are each connected by two separate bonds.
  C=C
 /   \
C     C
\\   //
  C-C
8)

    
"CCN"
{0, 1}
{2, 2}
Returns: 7
Dimethylamine:
  H   H
  |   |
H-C-N-C-H
  | | |
  H H H
"""


class OrganicChemistry:
    def countHydrogens(self, atoms, X, Y):

        count = 0
        c = [0] * len(atoms)
        z = {"C": 4, "N": 3, "O": 2}

        for i in range(len(atoms)):
            for j in range(len(X)):
                if X[j] == i:
                    c[i] += 1
                if Y[j] == i:
                    c[i] += 1

        for i in range(len(atoms)):
            count += z.get(atoms[i]) - c[i]

        return count
