from thinkbayes2 import Pmf
import thinkplot

d6 = Pmf()

for x in [1, 2, 3, 4, 5, 6]:
    d6[x] = 1

d6.Normalize()
print(d6)

twice = d6 + d6

# If the sum of two dice is greater than 3, then we update the dictionary
twice[2] = 0
twice[3] = 0
twice.Normalize()
print(twice)

thinkplot.Hist(twice)
thinkplot.show()
