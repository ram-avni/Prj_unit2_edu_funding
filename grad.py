import requests
from bs4 import BeautifulSoup
import pandas as pd

data = requests.get('https://www.governing.com/gov-data/high-school-graduation-rates-by-state.html')
html = BeautifulSoup(data.content,'html.parser')
html_page = list(html.children)[3]
body = html_page.find_all('body')
tables = body[0].find_all('table')
main_table = tables[0]
main_table = list(main_table)
main_table[3].get_text().split('\n')
data = []
for x in main_table[3].get_text().split('\n'):
    if x == '':
        continue
    else:
        data.append(x)

grad_dict = {}
i = 0
for x in range(52):
    grad_dict.update({data[i]: {2014: data[i+1].replace('%',''), 2013:data[i+2].replace('%',''),
                                2012: data[i+3].replace('%',''), 2011: data[i+4].replace('%',''),
                                2010: data[i+5].replace('%','')}})
    i+=6
grad_dict.pop("\xa0United States")
grad_dict = dict((k.upper().replace(' ','_'),v) for k, v in grad_dict.items())


grad_df = pd.DataFrame(grad_dict)
grad_df = grad_df.unstack().unstack()

grad_df = grad_df.reset_index()
grad_df = grad_df.rename(columns={'index':'STATE'})

grad_df = pd.melt(grad_df,var_name='YEAR',value_name='GRAD_PERCENT')
