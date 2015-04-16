################################################################################
## Booleans ##
################################################################################

# What will be the values?
bool1 = (True or False) and False
bool2 = True or (False and False)
bool3 = True or False and False

print(bool1)
print(bool2)
print(bool3)

################################################################################
## Strings ##
################################################################################

# What will it print? Use this when debugging
print("#"*80+"\n")

# Formating tips
print("{0} don't think it {1} like it is, but it {2}".format("They", "be", "do"))
pi = 42.3141592
print(".1f->{0:.1f} .5f->{0:.5f} +.3E->{0:+.3E}".format(pi))

# https://docs.python.org/3.3/library/string.html#formatspec

# Common example in data science, do some finding and replacing
# Get the qualifiers
s1 = "Dumb ExAmPlE"
s2 = "Normal example"
s3 = "Smart EXAMPLE"
s4 = "Anything"
s_list = [s1, s2, s3, s4]

# Option 1
qualifiers_1 = []
for s in s_list:
    sanitized_s = s.lower() 
    if "example" in sanitized_s:
	q = sanitized_s.split(" ")[0]
        qualifiers_1.append(q)
	
# Option 2
qualifiers_2 = [s.lower().split(" ")[0] for s in s_list] # Bad
print qualifiers_2
qualifiers_3 = [s.lower().split(" ")[0] if ("example" in s.lower()) else None for s in s_list] # Good
print qualifiers_3
qualifiers_4 = [s.lower().split(" ")[0] for s in s_list if ("example" in s.lower())] # Best list comprhension

print qualifiers_4

################################################################################
## Lists ##

################################################################################
## Sets ##

################################################################################
## Dics ##

################################################################################
## Code Flow: if, for, while, try, functions ##

# When to use try? When to avoid it?

################################################################################
## Reading and writing a file ##

## This is very important

## Also suggest using numpy.load and numpy.loadtxt

