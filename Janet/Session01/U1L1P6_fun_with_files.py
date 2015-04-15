# HW: Playing around with files.
# Link: https://courses.thinkful.com/data-001v2/project/1.1.6

from collections import defaultdict

dd = defaultdict(dict)   #SF# Excellent, I love default dics!

#SF# I'm not really sure what you wanted to do from here on...

    #header = next(inputfile)

def get_entry():
    with open('./data/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputfile:
    #print header
        for line in inputfile:
            line = line.strip().split(',')
            yield line


header = get_entry()

for line in get_entry():
    if line[1] == 'Total National Population':
        #print line
        continent = line[0]
        pop_type = line[2]
        population_2010 = int(line[5])
        population_2100 = int(line[6])
        entry = dd[continent]
        #dd[continent].extend({})
        #entry[pop_type] = population_2010
        entry['total_2010'] =  entry['total_2010'] + population_2010 if 'total_2010' in entry else population_2010
        entry['total_2100'] =  entry['total_2100'] + population_2100 if 'total_2100' in entry else population_2100
        entry['delta'] = float(entry['total_2100']/entry['total_2010']) * 100


#print dd
for key, entry in dd.iteritems():
    print entry['delta']

#with open('./data/scrubbed_2010_population.csv', 'w') as output:
#    output.write('continent,population2010\n')
#    for key, value in dd.iteritems():
#        print key, '\n', value
#        output.write(key + ',' + value + '\n' )
