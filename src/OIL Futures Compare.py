import yfinance as yf, calendar, datetime as dt, matplotlib.pyplot as plt, pandas as pd

daysAgo = 15
plt.style.use('dark_background')
keys=list("FGHJKMNQUVXZ")
months = [calendar.month_name[i+1] for i in range(12)] 
today = dt.datetime.today()
fromYear = today.year

def getData(year,iMonth,daysAgo=0):
    ticker = 'CL'+keys[i-1]+str(year)[-2:]+'.NYM'
    if daysAgo == 0:
        data = yf.download(ticker)[-1:].loc[:,['Adj Close','Volume']]
    else:
        data = yf.download(ticker)[(-daysAgo):(-daysAgo+1)].loc[:,['Adj Close','Volume']]        
    data['exp']=months[i-1]+' '+str(year)[-2:]
    data.set_index('exp',inplace=True,drop=True)
    return data
    
for i in range(today.month+1,13):
    data = getData(fromYear,i,0)
    dataPast = getData(fromYear,i,daysAgo)
    if i==today.month+1:
        table = pd.DataFrame(data)
        tablePast = pd.DataFrame(dataPast)        
    else:
        table = pd.concat([table,data],axis=0)
        tablePast = pd.concat([tablePast,dataPast],axis=0)

for i in range(1,13):
    data = getData(fromYear+1,i,0)
    table = pd.concat([table,data],axis=0)
    dataPast = getData(fromYear+1,i,daysAgo)
    tablePast = pd.concat([tablePast,dataPast],axis=0)
    
fig, ax = plt.subplots(figsize=(12,8),nrows=2,ncols=1,gridspec_kw={'height_ratios':[2, 1]})
ax[0].plot(table.index,table['Adj Close'], color='tab:blue', lw=3, label='Today Contracts Prices')
ax[0].plot(table.index,tablePast['Adj Close'], color='red', lw=2, ls='--', label=str(daysAgo)+' Days Ago')
ax[0].legend(loc='lower right', fontsize=14)
ax[1].bar(table.index,table['Volume'],width=0.5, color='tab:blue', alpha=0.75)
ax[1].bar(table.index,table['Volume']+tablePast['Volume'], bottom=table['Volume'] ,width=0.5, color='red', alpha=0.75)
ax[1].set_yscale('log')

fig.subplots_adjust(hspace=0)
plt.xticks(rotation=45, horizontalalignment='right', fontsize=12, color='lightgray')
plt.show()
