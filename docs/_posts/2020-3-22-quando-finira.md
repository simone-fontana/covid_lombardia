---
layout: post
title: Quando finirà?
excerpt_separator: <!--more-->
---

Nel tentativo di capire qualcosa di più dell'epidemia in Lombardia -  e anche per ammazzare la noia - ho provato ad analizzarne l'andamento nelle province più colpite: Bergamo, Brescia e Lodi.
<!--more-->

Ho utilizzato una [Logistica Generalizzata](https://en.wikipedia.org/wiki/Generalised_logistic_function) per modellare l'andamento del numero totale di contagi rispetto al tempo, in modo da avere una previsione di come l'epidemia si evolverà.  

In una prima fase si avrà una crescita esponenziale; questa fase non può, però, durare in eterno, in quanto il numero di possibili contagiati non può ovviamente superare l'intera popolazione. Dopo questa prima fase si avrà quindi un rallentamento della crescita. Questo rallentamento può essere dovuto a diversi fattori, come, ad esempio, all'introduzione di misure atte a limitare i contatti o a una riduzione della popolazione più suscettibile alla malattia (per evidenti, tristi, motivi). 

I parametri della logistica sono stati ottenuti cercando di minimizzare la differenza tra il modello e i dati finora raccolti (divisi per provincia), usando l'algoritmo [Levenberg–Marquardt](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm). 

Esistono diverse parametrizzazioni della Logistica Generalizzata. Quella usata è: 
![Sigmoid]({{ site.baseurl }}/images/sigmoid.gif)

dove `t` è il tempo, `y(t)` il numero di contagiati e `A, K, C, Q, B, M e ν` i parametri da stimare. 

Il risultato è il seguente.

[![Bergamo]({{ site.baseurl }}/images/Bergamo_sigmoid.png)]({{ site.baseurl }}/images/Bergamo_sigmoid.png)
[![Brescia]({{ site.baseurl }}/images/Brescia_sigmoid.png)]({{ site.baseurl }}/images/Brescia_sigmoid.png)

Come si può notare, sia nel caso di Bergamo che di Brescia, dovremmo trovarci all'incirca nel momento in cui il totale dei contagiati inizia a crescere più lentamente. Questo non vuol dire che il numero di nuovi contagiati crollerà drasticamente nei prossimi giorni, ma che, progressivamente, si dovrebbe assistere a un rallentamento della crescita, fino a un suo arrestarsi.

[![Lodi]({{ site.baseurl }}/images/Lodi_sigmoid.png)]({{ site.baseurl }}/images/Lodi_sigmoid.png)

Il caso di Lodi è diverso. Fin da subito sono state prese delle drastiche misure per isolare i focolai di COVID-19. Per questo motivo il numero di contagiati è cresciuto linearmente anziché esponenzialmente. Nella figura viene mostrata una retta, ma, ovviamente, anche nel caso di Lodi la crescita si arresterà. L'algoritmo di ottimizzazione, però, non lo sa e, dato che non c'è ancora segno del rallentamento nei dati, ha preferito interpolare il tutto con una retta. Purtroppo, con i dati che abbiamo, non si può prevedere quando questo rallentamento avrà luogo.

Queste previsioni vanno però prese con le dovute cautele. Diversi fattori influenzano l'accuratezza della previsione:
 - il modo in cui vengono identificati i contagiati non è uniforme nel tempo - è cambiato con l'avanzare dell'epidemia -, né nello spazio - in diverse aree si fanno tamponi con criteri diversi. Molti contagiati sono probabilmente asintomaitici e non conteggiati nelle statistiche;
 - il rispetto delle misure restrittive o la futura introduzione di misure più o meno severe possono influenzare pesantamente l'andamento dell'epidemia;
 - il modello usato è estremamente semplice ed esclusivamente fenomenologico.

I grafici sono stati generati a partire dai dati forniti dalla [Protezione Civile](https://github.com/pcm-dpc/COVID-19) sotto licenza [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.en)

[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/pcm-dpc/COVID-19/blob/master/LICENSE)
