---
layout: page
title: Ultimi grafici
---

# Grafici e analisi dati sull'epidemia di COVID-19 in Lombardia
[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)

I grafici sono stati generati a partire dai dati forniti dalla [Protezione Civile](https://github.com/pcm-dpc/COVID-19) sotto licenza [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en)

## Dati complessivi Lombardia

L'area verde mostra il possibile periodo di incubazione per un contagio avvenuto appena prima dell'entrata in vigore delle misure restrittive.

[![Dati Lombardia]({{ site.baseurl }}/images/lombardia.png)](lombardia.png)

## Dati per provincia
[![Nuovi Contagiati]({{ site.baseurl }}/images/incrementi.png)](incrementi.png)

[![Contagiati Totali]({{ site.baseurl }}/images/totale.png)](totale.png)

[![Tasso crescita]({{ site.baseurl }}/images/tasso.png)](tasso.png)

## Correlazione

### Correlazione del numero dei nuovi contagiati e della crescita dei nuovi contagiati rispetto all'entrata in vigore delle misure restrittive

La correlazione è stata calcolata come [Point Biserial Correlation](https://en.wikipedia.org/wiki/Point-biserial_correlation_coefficient)

Non si nota nessuna significativa correlazione negativa tra l'entrata in vigore delle misure restrittive e il numero di nuovi casi o l'incremento di nuovi casi. Ciò vuol dire che, purtroppo, le misure restrittive non hanno ancora sortito l'effetto desiderato. Si noti, tuttavia, come ci si trovi ancora nel possibile periodo di incubazione di contagiati prima delle misure restrittive.


| Provincia             | Corr. nuovi casi | Corr. tasso crescita nuovi casi |
|:----------------------|-----------:|-------------:|
| Bergamo               |  0.835877  |    0.0236663 |
| Brescia               |  0.825811  |    0.06318   |
| Como                  |  0.841287  |    0.154936  |
| Cremona               |  0.634034  |   -0.0203637 |
| Lecco                 |  0.698422  |    0.18102   |
| Lodi                  | -0.0525226 |    0.0838703 |
| Mantova               |  0.754392  |    0.107806  |
| Milano                |  0.753188  |    0.198626  |
| Monza e della Brianza |  0.443595  |    0.253046  |
| Pavia                 |  0.723738  |    0.0815752 |
| Sondrio               |  0.381836  |    0.015516  |
| Varese                |  0.855604  |    0.10201   |



### Correlazione del numero dei nuovi contagiati e della crescita dei nuovi contagiati rispetto al numero di giorni in cui sono state in vigore le misure restrittive

La correlazione è stata calcolata come [Correlazione di Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)

Non si nota nessuna significativa correlazione negativa tra il numero di giorni di misure restrittive e il numero di nuovi casi o l'incremento di nuovi casi. Ciò vuol dire che, purtroppo, le misure restrittive non hanno ancora sortito l'effetto desiderato. Si noti, tuttavia, come ci si trovi ancora nel possibile periodo di incubazione di contagiati prima delle misure restrittive.

| Provincia             |  Corr. nuovi casi | Corr. tasso crescita nuovi casi |
|:----------------------|-----------:|-------------:|
| Bergamo               |  0.412587  |   0.160839   |
| Brescia               |  0.58042   |  -0.125874   |
| Como                  |  0.800737  |  -0.122808   |
| Cremona               | -0.104895  |  -0.167832   |
| Lecco                 |  0.664336  |   0.297724   |
| Lodi                  | -0.0839161 |  -0.0629371  |
| Mantova               |  0.78459   |  -0.126095   |
| Milano                |  0.776224  |  -0.00699301 |
| Monza e della Brianza |  0.692308  |   0.321678   |
| Pavia                 |  0.424564  |  -0.048951   |
| Sondrio               |  0.425575  |  -0.108582   |
| Varese                |  0.72028   |  -0.224168   |

