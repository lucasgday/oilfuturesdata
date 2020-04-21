import yfinance as yf, calendar, datetime as dt, matplotlib.pyplot as plt, pandas as pd
plt.style.use('dark_background')

keys=list("FGHJKMNQUVXZ")
months = [calendar.month_name[i+1] for i in range(12)] 
today = dt.datetime.today()
fromYear = today.year

def getData(year,iMonth):
    ticker = 'CL'+keys[i]+str(year)[-2:]+'.NYM'
    data = yf.download(ticker)[-1:].loc[:,['Adj Close','Volume']]
    data['exp'] = months[i]+' '+str(year)[-2:]
    data.set_index('exp', inplace = True, drop = True)
    return data
    
for i in range(today.month,12):
    data = getData(fromYear,i)
    if i == today.month:
        table = pd.DataFrame(data)
    else:
        table = pd.concat([table,data],axis = 0)

for i in range(12):
    data = getData(fromYear+1,i)
    table = pd.concat([table,data],axis=0)
    
fig, ax = plt.subplots(figsize=(12,8),nrows=2,ncols=1,gridspec_kw={'height_ratios':[2, 1]})
ax[0].plot(table.index,table['Adj Close'], color='tab:blue')
ax[1].bar(table.index,table['Volume'],width=0.5, color='tab:blue')
ax[1].set_yscale('log')

fig.subplots_adjust(hspace=0)
plt.xticks(rotation=45, horizontalalignment='right', fontsize=12)
plt.show()
