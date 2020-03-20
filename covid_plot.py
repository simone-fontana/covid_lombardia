import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime, math, pandas, sys


def format_date_xaxis(axis):
    axis.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    axis.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    axis.grid(True)

def draw_date_info(axis):
    axis.axvline(datetime.datetime(2020, 3, 9), color='red', linestyle=':', label="Inizio misure restrittive")
    axis.axvspan(datetime.datetime(2020, 3, 11), datetime.datetime(2020, 3, 22), ymin=0, ymax=1, alpha=0.1, color='green', label="Periodo di incubazione")

dati_province = pandas.read_csv("COVID-19/dati-province/dpc-covid19-ita-province.csv")

dati_lombardia = pandas.read_csv("COVID-19/dati-regioni/dpc-covid19-ita-regioni.csv")
dati_lombardia = dati_lombardia.loc[dati_lombardia["denominazione_regione"] ==
                                    "Lombardia"]

province_lombardia = dati_province.loc[dati_province["denominazione_regione"]
                                       == "Lombardia"]
province_lombardia = province_lombardia[
    province_lombardia["denominazione_provincia"] !=
    "In fase di definizione/aggiornamento"]
province_lombardia = province_lombardia.groupby("denominazione_provincia")

fig_incrementi, ax_incrementi = plt.subplots()
fig_totali, ax_totali = plt.subplots()
fig_lombardia, ax_ospedale = plt.subplots()

ax_incrementi.set_title(
    "Nuovi casi (differenza totale_casi rispetto al giorno precedente)")
format_date_xaxis(ax_incrementi)

ax_totali.set_title("Casi totali")
format_date_xaxis(ax_totali)

dati_lombardia['data'] = pandas.to_datetime(dati_lombardia['data'],
                                            format='%Y-%m-%d %H:%M:%S')

dati_lombardia.plot(x='data', y='ricoverati_con_sintomi', ax=ax_ospedale)
dati_lombardia.plot(x='data', y='terapia_intensiva', ax=ax_ospedale)
dati_lombardia.plot(x='data', y='totale_ospedalizzati', ax=ax_ospedale)
dati_lombardia.plot(x='data', y='dimessi_guariti', ax=ax_ospedale)
dati_lombardia.plot(x='data', y='deceduti', ax=ax_ospedale)
dati_lombardia.plot(x='data', y='isolamento_domiciliare', ax=ax_ospedale)

ax_ospedale.set_title("Dati Lombardia")
format_date_xaxis(ax_ospedale)

# for (column_name, column_data) in dati_lombardia[
#         "ricoverati_con_sintomi", "terapia_intensiva", "totale_ospedalizzati",
#         "isolamento_domiciliare", "totale_attualmente_positivi",
#         "nuovi_attualmente_positivi", "dimessi_guariti", "deceduti",
#         "totale_casi", "tamponi"].iteritems():
#     dati_lombardia.plot(x='data', y=column_name)


for i, (provincia, group) in enumerate(province_lombardia):

    incrementi = group["totale_casi"].diff()
    dates = pandas.to_datetime(group['data'], format='%Y-%m-%d %H:%M:%S')
    ax_incrementi.plot(dates, incrementi, '.--', label=provincia)
    ax_totali.plot(dates, group["totale_casi"], '.--', label=provincia)


draw_date_info(ax_ospedale)
draw_date_info(ax_totali)
draw_date_info(ax_incrementi)

ax_incrementi.legend(loc='upper left', shadow=True, fontsize='medium')
ax_totali.legend(loc='upper left', shadow=True, fontsize='medium')
ax_ospedale.legend(loc='best', shadow=True, fontsize='medium')
# plt.show()

fig_lombardia.savefig("docs/lombardia.svg", format='svg')
fig_incrementi.savefig("docs/incrementi.svg", format='svg')
fig_totali.savefig("docs/totale.svg", format='svg')