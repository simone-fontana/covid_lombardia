import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime, math, pandas, numpy, sys, os
import scipy.stats


def format_date_xaxis(axis, spacing):
    axis.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    axis.xaxis.set_major_locator(mdates.DayLocator(interval=spacing))
    axis.grid(True)

def draw_date_info(axis, inizio_misure):
    axis.axvline(inizio_misure, color='red', linestyle=':', label="Inizio misure restrittive")
    axis.axvspan(datetime.datetime(2020, 3, 11), datetime.datetime(2020, 3, 22), ymin=0, ymax=1, alpha=0.1, color='green', label="Periodo di incubazione")

def load_dati_province(regione):
    os.system("wget -Nq https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")
    dati_province = pandas.read_csv("dpc-covid19-ita-province.csv")
    dati_province = dati_province.loc[dati_province["denominazione_regione"] == regione]
    dati_province = dati_province[dati_province["denominazione_provincia"] !="In fase di definizione/aggiornamento"]
    dati_province['data'] = pandas.to_datetime(dati_province['data'],format='%Y-%m-%d %H:%M:%S')
    return dati_province
                                    

if __name__ == "__main__":

    inizio_misure = datetime.datetime(2020, 3, 9)

    os.system("wget -N https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
    dati_lombardia = pandas.read_csv("dpc-covid19-ita-regioni.csv")

    province_lombardia = load_dati_province("Lombardia").groupby("denominazione_provincia")

    fig_incrementi, ax_incrementi = plt.subplots()
    fig_tasso, ax_tasso = plt.subplots()
    fig_totali, ax_totali = plt.subplots()
    fig_lombardia, ax_ospedale = plt.subplots()

    ax_incrementi.set_title(
        "Nuovi casi (differenza totale_casi rispetto al giorno precedente)")

    ax_totali.set_title("Casi totali")

    ax_tasso.set_title("Incremento dei nuovi casi rispetto al giorno precedente")

    dati_lombardia.plot(x='data', y='ricoverati_con_sintomi', ax=ax_ospedale)
    dati_lombardia.plot(x='data', y='terapia_intensiva', ax=ax_ospedale)
    dati_lombardia.plot(x='data', y='totale_ospedalizzati', ax=ax_ospedale)
    dati_lombardia.plot(x='data', y='dimessi_guariti', ax=ax_ospedale)
    dati_lombardia.plot(x='data', y='deceduti', ax=ax_ospedale)
    dati_lombardia.plot(x='data', y='isolamento_domiciliare', ax=ax_ospedale)

    ax_ospedale.set_title("Dati Lombardia")
    format_date_xaxis(ax_ospedale,4)

    # for (column_name, column_data) in dati_lombardia[
    #         "ricoverati_con_sintomi", "terapia_intensiva", "totale_ospedalizzati",
    #         "isolamento_domiciliare", "totale_attualmente_positivi",
    #         "nuovi_attualmente_positivi", "dimessi_guariti", "deceduti",
    #         "totale_casi", "tamponi"].iteritems():
    #     dati_lombardia.plot(x='data', y=column_name)
    correlazioni_dopo = []
    correlazioni_distanza = []

    for i, (provincia, group) in enumerate(province_lombardia):

        incrementi = group["totale_casi"].diff()
        group['data'] = pandas.to_datetime(group['data'], format='%Y-%m-%d %H:%M:%S')
        distanza_inizio_misure = (group['data'] - inizio_misure).dt.total_seconds()

        group['distanza_inizio_misure'] = distanza_inizio_misure
        group['incrementi'] = incrementi
        tasso_crescita = group['incrementi'].diff()
        group['tasso_crescita'] = tasso_crescita

        group.plot(x='data', y='incrementi', ax=ax_incrementi, linestyle='--', marker='.', label=provincia)
        group.plot(x='data', y='totale_casi', ax=ax_totali, linestyle='--', marker='.', label=provincia)
        group.plot(x='data', y='tasso_crescita', ax=ax_tasso, linestyle='--', marker='.', label=provincia )
        
        group['dopo'] = numpy.where(group["distanza_inizio_misure"] > 0, 1, 0)
        
        corr_dopo = group[['dopo','incrementi','tasso_crescita']].corr(method='pearson')
        group = group.loc[group['distanza_inizio_misure']>0]
        corr_distanza = group[['distanza_inizio_misure', 'incrementi', 'tasso_crescita']].corr(method='spearman')
        correlazioni_dopo.append({'prov':provincia, 'corr_inc':corr_dopo.iloc[0]['incrementi'], 'corr_tasso':corr_dopo.iloc[0]['tasso_crescita']})
        correlazioni_distanza.append({'prov':provincia, 'corr_inc':corr_distanza.iloc[0]['incrementi'], 'corr_tasso':corr_distanza.iloc[0]['tasso_crescita']})


    format_date_xaxis(ax_incrementi,4)
    format_date_xaxis(ax_totali,4)
    format_date_xaxis(ax_tasso,4)

    correlazioni_dopo = pandas.DataFrame(correlazioni_dopo)
    correlazioni_distanza = pandas.DataFrame(correlazioni_distanza)

    with open("docs/corr_dopo.md ", "w") as corr_dopo_file:
        corr_dopo_file.write(correlazioni_dopo[['prov','corr_inc', 'corr_tasso']].to_markdown(showindex=False))

    with open("docs/corr_distanza.md ", "w") as corr_dist_file:
        corr_dist_file.write(correlazioni_distanza[['prov','corr_inc', 'corr_tasso']].to_markdown(showindex=False))
        
    draw_date_info(ax_ospedale, inizio_misure)
    draw_date_info(ax_totali, inizio_misure)
    draw_date_info(ax_incrementi, inizio_misure)
    draw_date_info(ax_tasso, inizio_misure)


    ax_incrementi.legend(loc='upper left', shadow=True, fontsize='medium')
    ax_totali.legend(loc='upper left', shadow=True, fontsize='medium')
    ax_ospedale.legend(loc='best', shadow=True, fontsize='medium')
    # plt.show()

    fig_lombardia.set_size_inches(12, 8)
    fig_lombardia.savefig("docs/lombardia.png", format='png', dpi=600, pad_inches=0.2, bbox_inches='tight')

    fig_incrementi.set_size_inches(12, 8)
    fig_incrementi.savefig("docs/incrementi.png", format='png', dpi=600, pad_inches=0.2, bbox_inches='tight')

    fig_totali.set_size_inches(12, 8)
    fig_totali.savefig("docs/totale.png", format='png', dpi=600, pad_inches=0.2, bbox_inches='tight')

    fig_tasso.set_size_inches(12, 8)
    fig_tasso.savefig("docs/tasso.png", format='png', dpi=600, pad_inches=0.2, bbox_inches='tight')
