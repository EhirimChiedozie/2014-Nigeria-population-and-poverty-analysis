import pandas
from matplotlib import pyplot as plt

df = pandas.read_csv('povertyrate.csv')#From the povertyrate.csv file
#print(df.isna().sum()). Checks for missing values
del df['HASC_2']
del df['CCA_2']
del df['NL_NAME_2']
del df['VARNAME_2']
new_df = df.T.drop_duplicates().T#Deleting duplicate columns
'''
The states is Nigeria are in the NAME_1 column. So, we want to analyse the 
poverty rate by their respective states'''

state_group = new_df.groupby(['NAME_1'])
'''We want to find the total number of people in each state, the total
number of poor people in each state and put this info in a new dataframe(pov_df)'''
state_populations = state_group['2014_Popul'].sum()
state_poverty = state_group['2014_Pover'].sum()
pov_df = pandas.concat([state_populations,state_poverty],axis='columns',sort=False)
'''Now, lets us get the percentage of poor people in each state 
add it to our new pov_df dataframe'''
pov_df['Pov_Pct'] = (pov_df['2014_Pover']/pov_df['2014_Popul'])*100
'''Then we visualize this data and see the state with the highest poverty percentage'''
plt.bar(pov_df.index,pov_df['Pov_Pct'])
plt.xlabel('Nigerian States')
plt.ylabel('Percentage of poor people in each state'.title())
plt.title('Poverty rate in nigeria'.title())
plt.xticks(rotation=90)
plt.show()
#Suppose we want to check the state with the highest populations
plt.bar(pov_df.index,pov_df['2014_Popul'])
plt.ylabel('Number of people'.title())
plt.title('Nigerian population by states'.title())
plt.xticks(rotation=90)
plt.show()
#Is there any relationship between the number of people in a state and the poverty rate?
pov_df.sort_values(by=['2014_Popul'],ascending=True,inplace=True)
plt.scatter(pov_df['2014_Popul'],pov_df['Pov_Pct'])
plt.xlabel('number of people')
plt.ylabel('percentage of poor people')
plt.title('relationship between a state\'s population and the number of poor people'.title())
plt.show()
'''We can see tha t htere is no linear relationship between
the population and poverty rate.'''
