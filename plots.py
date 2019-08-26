import pandas as pd
import numpy as np
import seaborn as sb
import grad.py
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

## Hypothesis: local revenue is correlated with higher test scores
## Might have to normalize test scores with revenue?
df = pd.read_csv('/home/xristsos/flatiron/projects/proj resources/us ed/states_all.csv')
df = pd.read_csv('/home/xristsos/flatiron/projects/proj resources/us ed/states_all_extended.csv')

## DATA CLENAING & SHAPING
df['LOCAL_PERCENT'] = df['LOCAL_REVENUE'] / df['TOTAL_REVENUE']
df['STATE_PERCENT'] = df['STATE_REVENUE'] / df['TOTAL_REVENUE']
df['FED_PERCENT'] = df['FEDERAL_REVENUE'] / df['TOTAL_REVENUE']

df = df[df['YEAR']<=2015]
df = df[df['YEAR']>=2010]

df.drop('ENROLL',axis=1,inplace=True)
df.drop('PRIMARY_KEY',axis=1,inplace=True)
df = df.reset_index()
df.drop(['index'],axis=1,inplace=True)

# Merging dataframes to include graduation rate
df = pd.merge(df,grad_df,left_index=True,right_index=True)
df['GRAD_PERCENT'].replace(to_replace='-',value=np.NaN,inplace=True)
df['GRAD_PERCENT'] = pd.to_numeric(df['GRAD_PERCENT'])

#Cleaning and adding more columns

df.drop(['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE'],axis=1,inplace=True)

df=df[['STATE','YEAR_x','ENROLL','GRAD_PERCENT','TOTAL_REVENUE','LOCAL_REVENUE','STATE_REVENUE','FEDERAL_REVENUE',
    'LOCAL_PERCENT','FED_PERCENT','STATE_PERCENT','TOTAL_EXPENDITURE','SUPPORT_SERVICES_EXPENDITURE','INSTRUCTION_EXPENDITURE']]

# New columns for money spent per student
df['total_per_student'] = df['TOTAL_REVENUE'] / df['ENROLL']
df['local_per_student'] = df['LOCAL_REVENUE'] / df['ENROLL']
df['fed_per_student'] = df['FEDERAL_REVENUE'] / df['ENROLL']
df['state_per_student'] = df['STATE_REVENUE'] / df['ENROLL']


df['GRAD_PERCENT'] = df['GRAD_PERCENT'].fillna(df['GRAD_PERCENT'].mean())
df['gov_funding'] = df['STATE_REVENUE'] + df['FEDERAL_REVENUE']
df['gov_percent'] = df['gov_funding'] / df['TOTAL_REVENUE']


## PLOTTING
fig, ax = plt.subplots(figsize=(14,12))
fig2, ax2 = plt.subplots(figsize=(14,12))
sb.barplot(ax=ax2,x='LOCAL_PERCENT',y='STATE',data=df,ci='sd')
sb.barplot(ax=ax,x='gov_percent',y='STATE',data=df,ci='sd')
fig
fig2
fig.savefig('gov_percent.png',bbox_inches='tight')
fig.savefig('local_percent',bbox_inches='tight')
sb.barplot(ax=ax,x='FED_PERCENT',y='STATE',data=df)



## MAKING THE MODEL
lr_model = ols(formula='GRAD_PERCENT~LOCAL_PERCENT', data=df).fit()
lr_model.summary()

## Code by Rami
cost_liv_dict = { 'Hawaii': 168.6,
                'District of Columbia': 146.5,
                'New York': 135.6,
                'California': 134.3,
                'Alaska':133.5,
                'Connecticut': 131.8,
                'Massachusetts': 130.4,
                'Oregon': 129.5,
                'New Jersey': 125.6,
                'Vermont': 123.8,
                'Rhode Island': 123.3,
                'Maryland': 121.1,
                'New Hampshire': 118.2,
                'Maine': 114.7,
                'Nevada': 106.5,
                'Washington': 106.0,
                'West Virginia': 103.7,
                'Pennsylvania': 103.0,
                'Delaware': 102.8,
                'Montana': 102.7,
                'South Dakota': 102.5,
                'Colorado': 101.9,
                'Minnesota': 101.5,
                'North Dakota': 101.2,
                'Florida': 100.5,
                'Arizona': 98.8,
                'Wisconsin': 98.1,
                'South Carolina': 97.5,
                'Illinois': 96.5,
                'North Carolina': 95.8,
                'Virginia': 94.5,
                'Louisiana': 93.4,
                'Wyoming': 92.8,
                'Texas': 92.6,
                'Ohio': 92.5,
                'Utah': 92.4,
                'Nebraska': 92.3,
                'Iowa': 92.0,
                'Georgia': 91.7,
                'Missouri': 91.5,
                'Arkansas': 91.4,
                'Michigan': 91.2,
                'Kansas': 90.9,
                'Tennessee': 90.3,
                'Alabama': 90.2,
                'Kentucky': 90.0,
                'Oklahoma': 89.7,
                'Idaho': 88.2,
                'Indiana': 88.0,
                'Mississippi': 83.5,
                'New Mexico': 100.0
                }
​
cost_liv_dict = dict((k.upper().replace(' ','_'),v) for k, v in cost_liv_dict.items())
​
#Create cost of living index columns
df['Cost_living'] = df['STATE'].map(cost_liv_dict)
df['total_index'] = df['TOTAL_REVENUE'] / df['Cost_living']
df['local_index'] = df['LOCAL_REVENUE'] / df['Cost_living']
df['state_index'] = df['STATE_REVENUE'] / df['Cost_living']
df['fed_index'] = df['FEDERAL_REVENUE'] / df['Cost_living']

#Code by rami
state_popul = {'HAWAII': 1.43,
     'DISTRICT_OF_COLUMBIA': 0.672,
     'NEW_YORK': 19.80,
     'CALIFORNIA': 39.1,
     'ALASKA': 0.738,
     'CONNECTICUT': 3.59,
     'MASSACHUSETTS': 6.79,
     'OREGON': 4.03,
     'NEW_JERSEY': 8.96,
     'VERMONT': 0.626,
     'RHODE_ISLAND': 1.06,
     'MARYLAND': 6.01,
     'NEW_HAMPSHIRE': 1.33,
     'MAINE': 1.33,
     'NEVADA': 2.89,
     'WASHINGTON': 7.17,
     'WEST_VIRGINIA': 1.84,
     'PENNSYLVANIA': 12.8,
     'DELAWARE': 0.945,
     'MONTANA': 1.03,
     'SOUTH_DAKOTA': 0.858,
     'COLORADO': 5.46,
     'MINNESOTA': 5.49,
     'NORTH_DAKOTA': 0.756,
     'FLORIDA': 20.27,
     'ARIZONA': 6.83,
     'WISCONSIN': 5.77,
     'SOUTH_CAROLINA': 4.90,
     'ILLINOIS': 12.86,
     'NORTH_CAROLINA': 10.0,
     'VIRGINIA': 8.38,
     'LOUISIANA': 4.67,
     'WYOMING': 0.586,
     'TEXAS': 27.47,
     'OHIO': 11.6,
     'UTAH': 3.00,
     'NEBRASKA': 1.90,
     'IOWA': 3.12,
     'GEORGIA': 10.2,
     'MISSOURI': 6.08,
     'ARKANSAS': 2.98,
     'MICHIGAN': 9.92,
     'KANSAS': 2.91,
     'TENNESSEE': 6.60,
     'ALABAMA': 4.86,
     'KENTUCKY': 4.42,
     'OKLAHOMA': 3.91,
     'IDAHO': 1.65,
     'INDIANA': 6.62,
     'MISSISSIPPI': 2.99,
     'NEW_MEXICO': 2.09}
​
df['State_popul'] = df['STATE'].map(state_popul)

# Creating dataframes by state population
group1 = df[df['State_popul']>10]
group2 = df[df['State_popul']<10]

# EDA
n = 4
row_groups= [feats[i:i+n] for i in range(0, len(feats), n) ]
for i in row_groups:
    group1_ = sb.pairplot(data=group1, y_vars=['GRAD_PERCENT'],x_vars=i, kind="reg", height=3.5)
for i in row_groups:
    group2_ = sb.pairplot(data=group4, y_vars=['GRAD_PERCENT'],x_vars=i, kind="reg", height=3.5)


group2_.savefig('states_below_10.png',bbox_inches='tight')
group1_.savefig('states_above_10.png',bbox_inches='tight')
