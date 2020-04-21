#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:53:29 2020

@author: lucasgday
"""
from oil_functions import getdata, price_plot, volume_plot

def main():
    years = int(input("How many years of futures do you want to download?\n"))
    prices, vol_futures = getdata(years,"2d")  #"2d" is the period to look for
    price_plot(prices)
    volume_plot(vol_futures)
    
main()