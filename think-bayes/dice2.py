from thinkbayes2 import Pmf, Suite
import thinkplot

# Probability of each dice given that when rolled the output is 6

dice = Pmf(['4-sided', '6-sided', '8-sided', '12-sided'])

dice['4-sided'] *= 0
dice['6-sided'] *= 1 / 6
dice['8-sided'] *= 1 / 8
dice['12-sided'] *= 1 / 12
dice.Normalize()
print(dice)

suite = Suite([4, 6, 8, 12])
suite[4] *= 0
suite[6] *= 1 / 6
suite[8] *= 1 / 8
suite[12] *= 1 / 12
suite.Normalize()
print(suite)


class Dice(Suite):
    # hypo is the number if sides in the die
    # dat is the outcome

    def Likelihood(self, data, hypo):
        return 0 if data > hypo else 1 / hypo


dice2 = Dice([4, 6, 8, 12])
dice2.Update(6)
print(dice2)

# After 5 more rolls!?
for roll in [8, 7, 7, 5, 4]:
    dice2.Update(roll)
dice2.Print()

# What happens if suddenly there's a 10?
dice2.Update(10)
dice2.Print()


class Tank(Suite):
    # hypo is the number of tanks
    # data is an observed serial number

    def Likelihood(self, data, hypo):
        return 0 if data > hypo else 1 / hypo


tank = Tank(range(100))
tank.Update(37)
print(tank.Mean())
print(tank)


tank.Update(17)
print(tank.Mean())
print(tank)
thinkplot.Pdf(tank)
thinkplot.show()
