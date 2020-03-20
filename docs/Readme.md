# Grafici e dati sull'epidemia di COVID-19 in Lombardia
[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)

I grafici sono stati generati a partire dai dati forniti dalla [Protezione Civile](https://github.com/pcm-dpc/COVID-19) sotto licenza [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en)

## Dati complessivi Lombardia
![Dati Lombardia](docs/lombardia.svg)

## Dati per provincia
![Nuovi Contagiati](docs/incrementi.svg)

![Contagiati Totali](docs/totale.svg)

## Correlazione

### Correlazione del numero dei nuovi contagiati rispetto all'entrata in vigore delle misure restrittive
| Provincia | Correlazione |  p-value |
| --- | --- | --- |
{% include_relative corr_dopo.md %}

### Correlazione del numero dei nuovi contagiati rispetto ai giorni di distanza dall'entrata in vigore delle misure restrittive
| Provincia | Correlazione |  p-value |
| --- | --- | --- |
{% include_relative corr_distanza.md %}

