import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime, math, pandas, numpy, sys
import scipy.stats


def format_date_xaxis(axis):
    axis.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    axis.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    axis.grid(True)

def draw_date_info(axis, inizio_misure):
    axis.axvline(inizio_misure, color='red', linestyle=':', label="Inizio misure restrittive")
    axis.axvspan(datetime.datetime(2020, 3, 11), datetime.datetime(2020, 3, 22), ymin=0, ymax=1, alpha=0.1, color='green', label="Periodo di incubazione")

inizio_misure = datetime.datetime(2020, 3, 9)
dati_province = pandas.read_csv("dpc-covid19-ita-province.csv")

dati_lombardia = pandas.read_csv("dpc-covid19-ita-regioni.csv")
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
correlazioni = []
print(f'provincia: correlazione :: p_value')
for i, (provincia, group) in enumerate(province_lombardia):

    incrementi = group["totale_casi"].diff()
    dates = pandas.to_datetime(group['data'], format='%Y-%m-%d %H:%M:%S')
    ax_incrementi.plot(dates, incrementi, '.--', label=provincia)
    ax_totali.plot(dates, group["totale_casi"], '.--', label=provincia)
    distanza_inizio_misure = (dates - inizio_misure).dt.total_seconds()

    group['distanza_inizio_misure'] = distanza_inizio_misure
    group['incrementi'] = incrementi
    group['dopo'] = numpy.where(group["distanza_inizio_misure"] > 0, 1, 0)
    print(group)
    corr_dopo, p_value_dopo = scipy.stats.mstats.pointbiserialr(group['dopo'], group['incrementi'])

    group = group.loc[group['distanza_inizio_misure']>0]
    corr_distanza, p_value_distanza = scipy.stats.mstats.pearsonr(group['distanza_inizio_misure'], group['incrementi'])
    correlazioni.append({'prov':provincia, 'corr_dopo':corr_dopo, 'p_value_dopo':p_value_dopo, 'corr_distanza':corr_distanza, 'p_value_distanza':p_value_distanza})

    # print(group.corr(method='spearman'))

correlazioni = pandas.DataFrame(correlazioni)

with open("docs/corr_dopo.md ", "w") as corr_dopo_file:
    corr_dopo_file.write(correlazioni[['prov','corr_dopo', 'p_value_dopo']].to_markdown())

with open("docs/corr_distanza.md ", "w") as corr_dist_file:
    corr_dist_file.write(correlazioni[['prov','corr_distanza', 'p_value_distanza']].to_markdown())
    
draw_date_info(ax_ospedale, inizio_misure)
draw_date_info(ax_totali, inizio_misure)
draw_date_info(ax_incrementi, inizio_misure)

ax_incrementi.legend(loc='upper left', shadow=True, fontsize='medium')
ax_totali.legend(loc='upper left', shadow=True, fontsize='medium')
ax_ospedale.legend(loc='best', shadow=True, fontsize='medium')
# plt.show()

fig_lombardia.savefig("docs/lombardia.svg", format='svg')
fig_incrementi.savefig("docs/incrementi.svg", format='svg')
fig_totali.savefig("docs/totale.svg", format='svg')

