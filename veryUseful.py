# -*- coding: utf-8 -*-
"""

useful commands

"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# Read company names into a dictionary


def read_names_into_dict():
    """
    Read company names into a dictionary
    """
    d = dict()
    with open("SP_500_firms.csv", encoding='utf8') as csvfile:
        input_file = csv.DictReader(csvfile)
        for row in input_file:
            # print(row)
            d[row['Symbol']] = [row['Name'], row['Sector']]
    return d


names_dict = read_names_into_dict()
comp_names = names_dict.keys()

# Read prices into pandas

# Open data with pandas
filename = 'SP_500_close_2015.csv'
price_data = pd.read_csv(filename, index_col=0)

print(type(price_data))
print(price_data.columns)

# Get specific company data from the dataframe
# This is a pandas "series" of first-day prices
first_prices = price_data.iloc[0]
print(type(first_prices))

first_column_prices = price_data.iloc[:, 0]  # First company by index

apple_prices = price_data['AAPL']  # Get by _column name
msft_prices = price_data['MSFT']

msft_prices.nlargest(5)

# Create dataframe from series, then add another series
custom_prices = apple_prices.to_frame('AAPL')
custom_prices = custom_prices.join(msft_prices.to_frame('MSFT'))

stacked_prices = custom_prices.stack()  # combine into a single column
print(stacked_prices.shape)
stacked_prices.max()  # max among all prices

print(custom_prices)

# Normalise data by first price
prices_scaled = price_data.divide(price_data.iloc[0])
# Plot
price_fig = prices_scaled.plot(legend=False, figsize=(6, 4))

# Save figure into working directory
plt.savefig('stocks_test.png', bbox_inches='tight')

# Loop through companies
for index, company in enumerate(price_data.columns):
    print(company, index)

# Turn into numpy matrix
price_matrix = price_data.values
# Into a 1D array
price_array = price_matrix.flatten()
