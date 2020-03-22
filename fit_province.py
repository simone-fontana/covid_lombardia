import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime, math, pandas, numpy, sys, os
from scipy.optimize import curve_fit
import sklearn.metrics
import covid

def sigmoid(x, x0, y0, a,b):
     y = a / (1 + numpy.exp(-b*(x-x0))) + y0
     return y

def esp(x,a,b,c):
    return a*numpy.exp(b*x)+c

def grm(x,A,K,B,v,Q,C,M): 
    return A + (K-A)/((C+Q*numpy.exp(-B*(x-M)))**(1/v))

popolazione_province = {
    'BG': 1114590, 
    'BS': 1265954, 
    'CO': 599204,
    'CR': 358955,
    'LC': 337380,
    'LO': 230198,
    'MN': 412292,
    'MI': 3250315, 
    'MB': 873935,
    'PV': 545888,
    'SO': 181095,
    'VA': 890768, 
}

province = covid.load_dati_province("Lombardia")
province = province.loc[province['sigla_provincia'].isin(['LO','BG','BS','MI'])]
province = province.groupby("denominazione_provincia")
inizio = datetime.datetime(2020, 2, 10)


for i, (provincia, dati) in enumerate(province):
        fig, ax = plt.subplots()
        ax.set_title(provincia)
        popolazione = popolazione_province[dati.iloc[0]['sigla_provincia']]

        dati.plot(x='data', y='totale_casi', ax=ax, linestyle='--', marker='*', label='dati')

        x_data = mdates.date2num(dati['data'].to_numpy())
        y_data = dati['totale_casi'].to_numpy()

        # p_opt, p_cov = curve_fit(sigmoid, x_data, y_data, p0=[737501, 0, 1000, 1], maxfev=50000, method='lm')
        p_opt, p_cov = curve_fit(grm, x_data, y_data, p0=[14,10000, 0.1,0.1,0.1,0.1,737501], maxfev=50000000, method='lm')
        x_fitted = numpy.linspace(x_data[0], x_data[-1]+60, 200)
        y_fitted = grm(x_fitted, *p_opt)
        ax.plot(mdates.num2date(x_fitted), y_fitted, label='previsione')
        ax.legend(loc='upper left', shadow=True, fontsize='medium')
        ax.set_ylabel("totale_casi")
        y_predicted = grm(x_data, *p_opt)
        r = sklearn.metrics.r2_score(y_data, y_predicted)

        print(f'{provincia}: {r}')
        print(f'{provincia}: {p_opt}')
        covid.format_date_xaxis(ax,4)
        fig.set_size_inches(12, 8)
        fig.savefig(f"docs/images/{provincia}_sigmoid.png", format='png', dpi=600, pad_inches=0.2, bbox_inches='tight')
plt.show()