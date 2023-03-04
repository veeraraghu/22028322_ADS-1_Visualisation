# -*- coding: utf-8 -*-
"""
Student Id:22028322
Name:Veera Raghunatha Reddy Naguru
FAANG Stock Data visualisation
Data collected from Kaggle and link to download data is given below:
https://www.kaggle.com/datasets/aayushmishra1512/faang-complete-stock-data
"""
# Imported required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Defining Functions
# These functions are made by keeping common stocks data caolumn names
# in reference.


def data_trim_by_date(start_date, end_date, data):
    '''
    This function creates a Dataframe with records of data between given 
    start_date and end_date.

    Parameters
    ----------
    start_date : STR
        Enter starting date of your data to trim, in string format.
    end_date : STR
        Enter end date of your data to trim, in string format.
    data : pandas.DataFrame
        data['Date'] is our target column to perfom boolean operation 
        with "start_date" and "end_date" to get selective data.
        Make sure to check column names before calling this function.

    Returns
    -------
    pandas.DataFrame
        This function will return data recorded between 
        "start_date" and "end_date" with its index being reset .

    '''
    new_data = data[(data['Date'] >= start_date) & (data['Date'] < end_date)]
    new_data = new_data.reset_index(drop=True)

    return new_data


def returns(data):
    '''
    This function will create a single column DataFrame with return percentage 
    or the change in share value ('Close') with the previous day share value.
    Output data is in percentage.

    Parameters
    ----------
    data : pandas.DataFrame
        data['Close'] is our target column to calculate daily returns.
        Make sure to check column names before calling this function.

    Returns
    -------
    returns : pandas.DataFrame
        This function will return percentage change in Close value with 
        previous day Close value as a DataFrame.

    '''
    returns = data['Close'].pct_change()*100

    return returns


def volume(data):
    '''
    This function will calculate the total volume of shares sold or traded by 
    the company that is recorded in the given data.

    Parameters
    ----------
    data : pandas.DataFrame
        data['Volume'] is our target column to perform sum operation to get 
        total shares sold or traded by the company.
        Make sure to check column names before calling this function.

    Returns
    -------
    total_volume : Float
        This function will return total volume of shares sold or traded by 
        the company in millions as an integer.

    '''
    total_volume = data['Volume'].sum() / 1000000

    return total_volume


# Reading companies stock data
amzn = pd.read_csv('Amazon.csv')
apple = pd.read_csv('Apple.csv')
fbook = pd.read_csv('Facebook.csv')
google = pd.read_csv('Google.csv')
netflix = pd.read_csv('Netflix.csv')

# Looking at the top rows of all data
print('Amazon data', '\n', amzn.head(), '\n')
print('Apple data', '\n', apple.head(), '\n')
print('Facebook data', '\n', fbook.head(), '\n')
print('Google data', '\n', google.head(), '\n')
print('Netflix data', '\n', netflix.head(), '\n')

'''
Looking at all the top rows of data,
we can clearly say that the columns are similar in all the dataset.
But, the date values in all tables are different
'''

# Shape of Data of each company stock
print('Rows and columns in Amazon stocks data is ', amzn.shape)
print('Rows and columns in Apple stocks data is ', apple.shape)
print('Rows and columns in Facebook stocks data is ', fbook.shape)
print('Rows and columns in Google stocks data is ', google.shape)
print('Rows and columns in Netflix stocks data is ', netflix.shape, '\n')

'''
Since the number of records of all companies data is not same, 
we need to find a timeperiod where all companies stock records are available
'''

# start_date finds the starting date from where all companies data is recorded
start_date = max(amzn['Date'].min(), apple['Date'].min(),
                 fbook['Date'].min(), google['Date'].min(),
                 netflix['Date'].min())

# end_date finds the ending date until where all companies data is recorded
end_date = min(amzn['Date'].max(), apple['Date'].max(),
               fbook['Date'].max(), google['Date'].max(),
               netflix['Date'].max())

print('We have stocks data recorded of all companies from ', start_date,
      'until ', end_date, '\n')

# Creating new variables for data between the start_data and end_data
new_amzn = data_trim_by_date(start_date, end_date, amzn)
new_apple = data_trim_by_date(start_date, end_date, apple)
new_fbook = data_trim_by_date(start_date, end_date, fbook)
new_google = data_trim_by_date(start_date, end_date, google)
new_netflix = data_trim_by_date(start_date, end_date, netflix)

# Data is examined to check the start dates where data is recorded in of a year
# new_amzn.to_excel('new_amzn.xlsx')

# Shape of Data of each company stock
print('Rows and columns in Amazon stocks data is ', new_amzn.shape)
print('Rows and columns in Apple stocks data is ', new_apple.shape)
print('Rows and columns in Facebook stocks data is ', new_fbook.shape)
print('Rows and columns in Google stocks data is ', new_google.shape)
print('Rows and columns in Netflix stocks data is ', new_netflix.shape, '\n')

'''
We can see that all the datasets have same rows and columns 
'''

# Plotting company share performance
plt.figure(figsize=(10, 6))
plt.plot(new_amzn['Date'], new_amzn['Close'], label='Amazon')
plt.plot(new_apple['Date'], new_apple['Close'], label='Apple')
plt.plot(new_fbook['Date'], new_fbook['Close'], label='Facebook')
plt.plot(new_google['Date'], new_google['Close'], label='Google')
plt.plot(new_netflix['Date'], new_netflix['Close'], label='Netflix')
plt.xlabel('Year')
plt.ylabel('Daily Close in US$')
plt.title('Stock Performance over time')
# These dates are the first working days of years from 2013 to 2020
# and where our stocks data is recorded.
plt.xticks(['2013-01-02', '2014-01-02', '2015-01-02', '2016-01-04',
            '2017-01-03', '2018-01-02', '2019-01-02', '2020-01-02'],
           [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
plt.legend(loc='upper left')
plt.savefig('Stock_Performance_over_time.png')
plt.show()

'''
By looking at the line plot,
we can say that the Amazon stock value is increased than the value of Apple
'''

# Calculationg returns
new_amzn['Returns'] = returns(new_amzn)
new_apple['Returns'] = returns(new_apple)
new_fbook['Returns'] = returns(new_fbook)
new_google['Returns'] = returns(new_google)
new_netflix['Returns'] = returns(new_netflix)

# Plotting distributions of return percentage of each company
plt.figure(figsize=(10, 10))
plt.suptitle('Distributions of Daily Returns of each Company', fontsize=20)
plt.subplot(3, 2, 1)
plt.hist(new_amzn['Returns'], bins=20, label='Amazon',
         density=True, color='c')
plt.title('Amazon')
plt.xlabel('Returns Percentage Distribution')
plt.grid(True)
plt.legend()
plt.subplot(3, 2, 2)
plt.hist(new_apple['Returns'], bins=20, label='Apple',
         density=True, color='g')
plt.title('Apple')
plt.xlabel('Returns Percentage Distribution')
plt.grid(True)
plt.legend()
plt.subplot(3, 2, 3)
plt.hist(new_fbook['Returns'], bins=20, label='Facebook',
         density=True, color='b')
plt.title('Facebook')
plt.xlabel('Returns Percentage Distribution')
plt.grid(True)
plt.legend()
plt.subplot(3, 2, 4)
plt.hist(new_google['Returns'], bins=20, label='Google',
         density=True, color='m')
plt.title('Google')
plt.xlabel('Returns Percentage Distribution')
plt.grid(True)
plt.legend()
plt.subplot(3, 2, 5)
plt.hist(new_netflix['Returns'], bins=20, label='Netflix',
         density=True, color='r')
plt.title('Netflix')
plt.xlabel('Returns Percentage Distribution')
plt.grid(True)
plt.legend()
plt.tight_layout(pad=1)
plt.savefig('Distributions_of_Daily_Returns_of_each_Company.png')
plt.show()

print('All stocks have a 50% - 60% chance of daily profit')

# Calculating total volume of shares traded or sold
total_volume = [volume(new_amzn), volume(new_apple), volume(new_fbook),
                volume(new_google), volume(new_netflix)]
companies = ['Amazon', 'Apple', 'Facebook', 'Google', 'Netflix']

# Plotting total volume of shares over company in millions
plt.figure(figsize=(10, 6))
bars = plt.bar(companies, total_volume, color='g')
plt.xlabel('Company')
plt.ylabel('Shares sold/traded in millions')
plt.title('Total Volume Shares sold/traded by Company')
plt.bar_label(bars)
plt.savefig('Total_Volume_Shares_sold_traded_by_Company.png')
plt.show()

print('Most traded stock is ', companies[np.argmax(total_volume)], ' with ',
      max(total_volume), ' Millions of shares sold or traded.')
