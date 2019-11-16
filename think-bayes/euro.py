from thinkbayes2 import Pmf, Suite
import thinkplot


# Assume that a coin has probability x of landing heads


class Euro(Suite):
    # data is 'H' or 'T'
    # hypo is the prob of heads

    def Likelihood(self, data, hypo):
        x = hypo / 100
        return x if data == 'H' else 1 - x


euro = Euro(range(101))
evidence = 'H'*140 + 'T'*110
for outcome in evidence:
    euro.Update(outcome)

print(euro)
print('Mean: ', euro.Mean())
print('Maximum Likelihood: ', euro.MaximumLikelihood())
print('Credible Interval: ', euro.CredibleInterval(90))
thinkplot.Pdf(euro)
thinkplot.show()
