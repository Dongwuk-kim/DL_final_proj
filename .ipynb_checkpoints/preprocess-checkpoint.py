# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:02:21 2019

@author: cobook
"""




import pandas as pd
import collections
import json
import numpy as np

def preprocess():
    #pd.read_excel("raw_data//daily_price.xlsx")
    print("Import Industry xlsx file...")
    df = pd.read_excel("raw_data//Industry_code.xlsx")
    df.columns = df.iloc[7]
    df = df[13:]
    df = df.set_index('Symbol')

    print("Import price xlsx file...")
    price = pd.read_excel("raw_data//daily_price.xlsx")
    price.columns = price.iloc[7]
    price = price[13:]
    price = price.set_index('Symbol')
    print("===============================")
  

    print("save json file ")
    
    #save as json file
    price_js = price.to_json(orient='columns')
    with open('data//daily_price.json', 'w') as outfile:
        json.dump(price_js, outfile)
    
        
    dummy_table = price.copy()
    for col in dummy_table.columns:
        dummy_table[col].values[:] = np.NaN
        
    for col in df.columns:
        dummy_table.loc[df.index[8:], col] = df.loc[df.index[8:], col]
    
        
    #backward_fill
    dummy_table = dummy_table.bfill()
    
    for col in dummy_table.columns:
        dummy_table.ioc[dummy_table.index, col] = df.ioc[dummy_table.index, col]
    
    small_price = price.loc[:, df.columns]
    
    
    #save as json file
    price_js = small_price.to_json(orient='columns')
    with open('data//daily_price_small.json', 'w') as outfile:
        json.dump(price_js, outfile)
    
    #save as json file
    price_js = dummy_table.to_json(orient='columns')
    with open('data//industry_code.json', 'w') as outfile:
        json.dump(price_js, outfile)
        


if __name__ == "__main__":
	preprocess()
