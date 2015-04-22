# https://courses.thinkful.com/data-001v2/project/2.2.3
"""
Challenge
Write a script called "chi_squared.py" that loads the data, cleans it,
performs the chi-squared test, and prints the result.
"""
""" #SF
Again, very good work. Good use of auxiliar library.
Nice use of os library.
Speachless!
"""

from scipy import stats
import collections
import lending_club_utils as utils
import matplotlib.pyplot as plt

loanData = utils.fetch_data_frame()

frequency = collections.Counter(loanData['Open.CREDIT.Lines'])

# render bar graph, following the lesson
plt.figure()
plt.bar(frequency.keys(), frequency.values(), width=1)
plt.show()

# calculate chi square
chi, p = stats.chisquare(frequency.values())
print("Chi value is %f and probability is %f" % (chi, p))
