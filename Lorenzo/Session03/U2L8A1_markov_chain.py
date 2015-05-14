# coding: utf-8

# Why: Applying markov chains with pandas and numpy
# Where: https://courses.thinkful.com/DATA-001v2/assignment/2.8.1
# Findings: The example is the same as http://en.wikipedia.org/wiki/Markov_chain

import pandas as pd
import numpy as np

# Very handy hack: control how you want to see your matrices!
np.set_printoptions(suppress=True, precision=4) # Supress avoids scientific notation in printing

# remind: the column seems to be ordered alphabetically
df = pd.DataFrame({'Bear Market': [.8, .15, .05], 
                   'Bull Market': [.075, .9,.025],
                    'Stagnant Market':[.25,.25 ,.5]
                  },
                  index=["Bear Market", "Bull Market","Stagnant Market"])
# Notice how different this is from
"""
df = pd.DataFrame({'Bear Market': [.8, .15, .05], 
                   'Bull Market': [.075, .9,.025],
                    'Stagnant Market':[.25,.25 ,.5]
                  },
                  index=["Bull Market", "Bear Market", "Stagnant Market"])
"""

#####################################################################################
#SF# Try answering the questions in order
#####################################################################################

# Question 1 # 
# Translate the Markov chain below to a matrix. What are the transition probabilities after 1 transition? #
A = np.array([[	.800, .150, .050],
              [.075, .900, .025], 
              [.250, .250, .500]])
# or #
A = df.as_matrix().T # Check how the matrix is delivered!

# OBS: each row should add up to one.

print A
print np.dot(A,A) # Obs, different notation if np.matrix!

# Question 2 #
# What are the transition probabilities after 2 transitions? After 5? After 10? What are the steady state probabilities?#
print np.linalg.matrix_power(A,2+1)
print np.linalg.matrix_power(A,5+1)
print np.linalg.matrix_power(A,10+1)
print np.linalg.matrix_power(A,30+1)

# Question 2b #
# What could you do with that information? # 
# Would you be optimistic, neutral or pesimistic about the market? # 

# Question 3 #
# Can you a name some real-life examples that could be modeled by Markov chains? #
# Can you name examples that cannot be treated as Markov chains? #
# Can you name an example of finite probabilistic states that cannot be modeled as Markov chains? #

# Extra Question: How can you know for sure when it converges? #
# IE, a more scientific method? #
tol,
np.norm( np.linalg.matrix_power(A,n+1) - np.linalg.matrix_power(A,n+1+1)) ) < tol





