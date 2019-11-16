from thinkbayes2 import Pmf

# Cookie Problem

# Prior 50%-50%
cookie = Pmf(['Bowl 1', 'Bowl 2'])

# p (Vanilla|Bowl1) = 30/40
cookie['Bowl 1'] *= 0.75
# p (Vanilla|Bowl2) = 20/40
cookie['Bowl 2'] *= 0.5

# Normalize, return values is p(D)
cookie.Normalize()

# Posteriors
print(cookie)

# Suppose we put the first cookie back, stir, choose again from the same bowl, and
# get a chocolate cookie

# p (Chocolate|Bowl1) = 10/40
cookie['Bowl 1'] *= 0.25
# p (Chocolate|Bowl2) = 20/40
cookie['Bowl 2'] *= 0.5

cookie.Normalize()
print(cookie)

