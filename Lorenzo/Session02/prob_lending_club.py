import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

filename='dat/loansData.csv'
loansData = pd.read_csv(filename)
colname=['Amount.Requested','Amount.Funded.By.Investors']
data=[loansData[colname[0]],loansData[colname[1]]]
loansData.dropna(inplace=True)

loansData.boxplot(column=colname[0])
plt.savefig('boxplot.pdf', bbox_inches='tight')
plt.show()

sns.violinplot(data,color="Paired", bw=1);
plt.savefig('violinplot.pdf', bbox_inches='tight')
plt.show()

loansData.hist(column=colname[0])
plt.savefig('histogram.pdf', bbox_inches='tight')
plt.show()

stats.probplot(loansData[colname[0]], dist='norm',plot=plt)
plt.savefig('qqplot.pdf', bbox_inches='tight')
plt.show()