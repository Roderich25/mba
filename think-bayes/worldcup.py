from scipy.special import gamma
from thinkbayes2 import Pmf, Suite
import thinkplot
import numpy as np
import math


# World Cup Problem
# In the 2014 FIFA World Cup, Germany played Brazil in a semifinal match.
# Germany scored after 11 minutes and again at the 23 minute mark.
# At that point in the match, how many goals would you expect Germany to score after 90 minutes?
# What was the probability that they would score 5 more goals?

# What are the parameters?
# The goal scoring rate lambda, in goals per game

# What are the hypotheses?
# A range of possible values for lambda.

# What is the prior?
# Gamma distribution with mean based on previous games

# Prior

def EvalGammaPdf(lam, a):
    return lam ** (a - 1) * math.exp(-lam) / gamma(a)


def MakeGammaPmf(lams, a):
    pmf = Pmf()
    for lam in lams:
        pmf[lam] = EvalGammaPdf(lam, a)
    pmf.Normalize()
    return pmf


lams = np.linspace(0, 8, 101)
pmf = MakeGammaPmf(lams, 1.3)  # 1.3 average number of goals per game
print(pmf)


class Soccer(Suite):
    # hypo: scoring rate in goals per game
    # data: interval time in minutes
    def Likelihood(self, data, hypo):
        x = data / 90
        like = hypo * np.exp(-hypo * x)
        return like


soccer = Soccer(pmf)
thinkplot.Pdf(soccer, color='0.6')
print(soccer.Mean())

soccer.Update(11)
thinkplot.Pdf(soccer, color='0.6')
print(soccer.Mean())

soccer.Update(12)
thinkplot.Pdf(soccer)
print(soccer.Mean())

thinkplot.show()
