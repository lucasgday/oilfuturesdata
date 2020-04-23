import yfinance as yf
import calendar
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('dark_background')
keys = list("FGHJKMNQUVXZ")
months = [calendar.month_name[i+1] for i in range(12)] 
today = dt.datetime.today()
daysAgo = 15
startDate = today - dt.timedelta(daysAgo)
fromYear = today.year

def getData(year,iMonth):
    ticker = 'CL'+keys[i-1]+str(year)[-2:]+'.NYM'
    data = yf.download(ticker, start = startDate).loc[:,['Adj Close','Volume']]
    data['exp'] = months[i-1]+' '+str(year)[-2:]
    data.set_index('exp', inplace = True, drop = True)
    return data
    
#1st year
for i in range(today.month+1,13):
    data = getData(fromYear,i)
    if i==today.month+1:
        table = pd.DataFrame(data[-1:])
        tablePast = pd.DataFrame(data[:1])        
    else:
        table = pd.concat([table, data[-1:]],axis=0)
        tablePast = pd.concat([tablePast, data[:1]],axis=0)

#2nd year
for i in range(1,13):
    data = getData(fromYear+1,i)
    table = pd.concat([table, data[-1:]],axis=0)
    tablePast = pd.concat([tablePast, data[:1]],axis=0)

fig, ax = plt.subplots(figsize=(12,8), nrows=3, ncols=1, 
                       gridspec_kw={'height_ratios':[3, 1, 1]})
ax[0].plot(table.index, table['Adj Close'], color='tab:blue', lw=3, 
           label='Today ({})'.format(today.date()))
ax[0].plot(table.index, tablePast['Adj Close'], color='red', lw=2, ls='--', 
           label=str(daysAgo)+' Days Ago')
ax[0].legend(loc='lower right', fontsize=14)
ax[0].set_ylabel("USD / bbl")
ax[1].bar(table.index, table['Volume'], width=0.5, color='tab:blue', alpha=0.75)
ax[2].bar(table.index, tablePast['Volume'], width=0.5, color='red', alpha=0.25)
ax[1].set_yscale('log')
ax[2].set_yscale('log')
ax[1].set_ylabel("Today's Volume")
ax[2].set_ylabel(str(daysAgo)+" Days Ago")

fig.subplots_adjust(hspace=0)
plt.xticks(rotation=45, horizontalalignment='right', fontsize=12, color='lightgray')
fig.suptitle("WTI Future Contracts", y=0.7, color="gold", fontsize=50, alpha=0.1)
plt.show()
