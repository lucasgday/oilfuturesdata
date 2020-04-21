# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:53:29 2020

@author: lucasgday
"""
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime

def getdata(years, period):
    this_year = datetime.date.today().year
    starting_year = int(str(this_year)[-2:])
    ending_year = int(str(this_year + years)[-2:])
    tickers = []
    column_names = []
    
    for i in range(starting_year,ending_year + 1):
        tickers.extend(["CLF{}.NYM".format(i), "CLG{}.NYM".format(i), 
                        "CLH{}.NYM".format(i), "CLJ{}.NYM".format(i), 
                        "CLK{}.NYM".format(i), "CLM{}.NYM".format(i), 
                        "CLN{}.NYM".format(i), "CLQ{}.NYM".format(i), 
                        "CLU{}.NYM".format(i), "CLV{}.NYM".format(i), 
                        "CLX{}.NYM".format(i), "CLZ{}.NYM".format(i)])
        column_names.extend(['Jan-{}'.format(i), 'Feb-{}'.format(i),
                         'Mar-{}'.format(i), 'Apr-{}'.format(i),
                         'May-{}'.format(i), 'Jun-{}'.format(i),
                         'Jul-{}'.format(i), 'Aug-{}'.format(i),
                         'Sep-{}'.format(i), 'Oct-{}'.format(i),
                         'Nov-{}'.format(i), 'Dec-{}'.format(i)])

        futures = pd.DataFrame()
        prices = pd.DataFrame(columns=column_names)
        vol_futures = pd.DataFrame(columns=column_names)

    j=0
    for ticker in tickers:
        print(ticker)
        
        futures = yf.download(ticker,period=period)
        prices[column_names[j]] = round(futures['Adj Close'],2)
        vol_futures[column_names[j]] = round(futures['Volume'],2)
        futures = pd.DataFrame()
        j+=1
        
    return prices, vol_futures

def price_plot(prices):
    plt.figure(figsize=(10,5))
    prices.iloc[-2,:].plot()
    plt.ylabel("USD / bbl")
    plt.grid(axis='y', alpha = .5)
    plt.title("Futures @ {}".format(prices.index[-2].date()))
    plt.savefig("prices_example.png")

def volume_plot(volume):
    plt.figure(figsize=(10,5))
    volume.iloc[-2,:].plot(kind='bar')
    plt.yscale('log')
    plt.ylabel("Nº of Traded Contracts")
    plt.grid(axis = 'y', which = 'major', alpha = .5)
    plt.grid(axis = 'y', which = 'minor', alpha = .1)
    plt.title("Futures @ {}".format(volume.index[-2].date()))
    plt.savefig("volume_example.png")