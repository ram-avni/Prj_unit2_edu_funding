import pandas as pd
import numpy as np
import seaborn as sb
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


df = pd.read_csv('states_all.csv')
df.describe()
df.dropna(inplace=True)


df['PERCENT_OF_TOTAL'] = df['LOCAL_REVENUE'] / df['TOTAL_REVENUE']
df['PERCENT_OF_TOTAL']
df = df[df['YEAR']>2000]


feats = ['LOCAL_REVENUE','FEDERAL_REVENUE','PERCENT_OF_TOTAL','TOTAL_EXPENDITURE','INSTRUCTION_EXPENDITURE','SUPPORT_SERVICES_EXPENDITURE']


lr_model = ols(formula='PERCENT_OF_TOTAL~AVG_READING_4_SCORE', data=df).fit()
lr_model.summary()

n=4
row_groups = [feats[i:i+n] for i in range(0,len(feats),n)]

for i in row_groups:
    p = sb.pairplot(data=df, y_vars=['SUPPORT_SERVICES_EXPENDITURE'],x_vars=i,kind='reg',height=3)
for i in row_groups:
    p = sb.pairplot(data=df, y_vars=['AVG_READING_4_SCORE'],x_vars=i,kind='reg',height=3)
for i in row_groups:
    p = sb.pairplot(data=df, y_vars=['AVG_READING_8_SCORE'],x_vars=i,kind='reg',height=3)
for i in row_groups:
    p = sb.pairplot(data=df, y_vars=['AVG_MATH_4_SCORE'],x_vars=i,kind='reg',height=3)
for i in row_groups:
    p = sb.pairplot(data=df, y_vars=['AVG_MATH_8_SCORE'],x_vars=i,kind='reg',height=3)
