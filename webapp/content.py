bando = """
> Il progetto è parte del Operativo Regionale del Fondo Europeo di Sviluppo Regionale (POR FESR 2014 - 2020) del Veneto, nell'ambito del bando dell'azione 231 volto alla "costituzione di Innovation Lab diretti al consolidamento/sviluppo del network Centri P3@-Palestre Digitali e alla diffusione della cultura degli Open Data."
"""

body = dict(

viirs=dict(

meta_description="""
La web app che stima, sulla base di immagini satellitari notturne, l'inquinamento luminoso nei comuni italiani.
""",

title="Inquinamento luminoso",

filler="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",

intro1="""
L'inquinamento luminoso è l'alterazione dei livelli di illuminazione naturale notturna causata da fonti di luce antropiche. I livelli di illuminazione naturale sono regolati da fonti naturali celesti, principalmente la luna, le emissioni atmosferiche naturali (Airglow), le stelle e la Via Lattea, la luce zodiacale. La luce artificiale sparsa nell'atmosfera rilancia la luminanza del cielo notturno e colpisce anche i siti incontaminati: è facilmente osservata durante la notte centinaia di chilometri dalla sua fonte in paesaggi che sembrano intatti dagli umani durante il giorno, danneggiando i paesaggi notturni anche in aree protette, come i parchi nazionali. Oltre a ostacolare le osservazioni astronomiche ottiche al terreno, la luminosità artificiale del cielo notturno rappresenta una profonda alterazione di un'esperienza umana fondamentale - l'opportunità per ogni persona di vedere e riflettere il cielo notturno. Inoltre, l'inquinamento luminoso causa conseguenze ecologiche globali, pone problemi di salute pubblica e spreca energia e denaro. (1)
""",

intro2="""
I satelliti di osservazione della Terra consentono il monitoraggio del pianeta di notte. Stime dell'Associazione Internazionale Dark-Sky, basata sul lavoro da immagini satellitari, mostrano che le città brillano inutilmente miliardi di dollari direttamente nel cielo ogni anno. (2) I satelliti sono in grado di dimostrare il crescente inquinamento luminoso artificiale, lo sviluppo di nuove fonti di illuminazione, come LED, e la continua crescita in estensione e radianza delle aree artificialmente illuminate. (3) I grafici qui sotto sono basati sull'analisi delle immagini satellitari americane Suimi-NPP (4) e ci aiutano a capire, in modo quantitativo, come il problema dell'inquinamento luminoso tocca il territorio vicentino e oltre. Mettono diversi comuni in confronto, mostrando la quantità di luce irradiata nel cielo.
""",

interp="""
- Ogni grafico mostra i singoli comuni come "bolle". Le loro dimensioni dipendono proportizialmente dalla popolazione. Ad esempio, una bolla di Vicenza è più grande di quella di Creazzo.
- Sull'asse X, ci sono i valori mediani (MEDIANA) di quanta luce è emessa nel cielo sopra il territorio di un singolo comune, come misurato dal satellite.Sono espressi in Nanowatt Diviso per centimetro quadrato per steradiante. Più il valore, più inquinamento luminoso è, in generale. I valori più grandi di 10 corrispondono all'alto livello di inquinamento del cielo, dove le persone non sperimentano mai condizioni simile a una vera notte perché è mascherata da un crepuscolo artificiale.
- Sull'asse Y, c'è una deviazione standard (STD), che mostra la dispersione della quantità di luce all'interno di un comune. Una bassa STD indica che i valori tendono ad essere vicini alla media (non mediana), mentre una STD elevata indica che i valori sono distribuiti su un range più ampio.
- Ad esempio, rispetto ad altri comuni della provincia di Vicenza, Rossano Veneto ha la mediana elevata ma la bassa STD, il che significa che l'intero territorio del comune è illuminato in un modo uniformemente alto. Al contrario il comune di Vicenza ha sia l'elevata mediana sia l'alta std, che corrispondono alla parte centrale brillante e alle aree periferiche più scure.
- Su ogni grafico, i comuni di interesse sono provvisti dell'etichetta e evidenziati nel colore giallo. Per vedere i nomi e vari valori di comuni, basta porre il punto del mouse su una "bolla".
""",

workflow="""
Per creare questi grafici abbiamo usato il seguente flusso di lavoro:

1. Il territorio di ogni comune e definito dal dataset dei limiti amministrativi pubblicato dall'Istat (5).
2. Le immagini satellitari notturne **VIIRS** (4) sono ottenute e elaborate nella piattaforma Big Data che si chiama [Google Earth Engine](https://earthengine.google.com/).
3. Incrociando le immagini notturne con i limiti amministrativi usando, per ogni territorio comunale vengono calcolate cosidette *statistiche zonali*, in software libero [QGIS](https://www.qgis.org/). Cioè i caratteri come media, mediana, deviazione standard, min e max che descrivono i valori estratti dalle immagini e rilevanti solo per questo comune.
4. Avendo le statistiche possiamo tracciare i grafici. Per la rappresentanza del fenomeno dell'inquinamento luminoso in un modo semplice e allo stesso modo efficace, come la descrizione dei comuni abbiamo scelto i caratteri *mediana* e *deviazione standard*.
""",

refs="""
1. Falchi, Fabio, Pierantonio Cinzano, Dan Duriscoe, Christopher C.M. Kyba, Christopher D. Elvidge, Kimberly Baugh, Boris A. Portnov, Nataliya A. Rybnikova, and Riccardo Furgoni. 2016. “The New World Atlas of Artificial Night Sky Brightness.” Science Advances 2 (6): 1–26. [doi:10.1126/sciadv.1600377](https://doi.org/10.1126/sciadv.1600377).
2. Smith, Malcolm. 2009. “Time to Turn off the Lights.” Nature 457 (7225): 27–27. [doi:10.1038/457027a](https://doi.org/10.1038/457027a).
3. Levin, Noam, Christopher C.M. Kyba, Qingling Zhang, Alejandro Sánchez de Miguel, Miguel O. Román, Xi Li, Boris A. Portnov, et al. 2020. “Remote  Sensing of Night Lights: A Review and an Outlook for the Future.” Remote Sensing of Environment 237 (September 2019). [doi:10.1016/j.rse.2019.111443](https://doi.org/10.1016/j.rse.2019.111443).
4. Le immagini notturni della Terra "VIIRS Stray Light Corrected Nighttime Day/Night Band Composites Version 1", di pubblico dominio, ottenute e elaborati tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG).
5. Istat. Limiti amministrativi di tutti i comuni italiani: https://www.istat.it/it/archivio/222527
""",

credits="""
- La web app è sviluppata con Python Dash è un quadro produttivo Python per la creazione di applicazioni analitiche Web.
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
- Foto dell'inquinamento luminoso: [Yan Yu Chen](https://www.flickr.com/photos/darkyanyu/5505836856/), licenza [CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)
"""

),

pvout={
                "meta_description": "Una web app che stima, sulla base di immagini satellitari notturne, l'inquinamento luminoso nei comuni italiani.",
                "title": "Potenziale fotovoltaico",
                "filler": """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",
                "intro": """
![NASA - Immagine notturna dell'Italia](assets/italy-night-200px.jpg)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",
                "icons": """
## Credits
- Le immagini notturni della Terra "VIIRS Stray Light Corrected Nighttime Day/Night Band Composites Version 1", di pubblico dominio, ottenuti e elaborati tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG).
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
"""
        },

ghm={
                "meta_description": "Una web app che stima, sulla base di immagini satellitari notturne, l'inquinamento luminoso nei comuni italiani.",
                "title": "Pressione Antropica",
                "filler": """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",
                "intro": """
![NASA - Immagine notturna dell'Italia](assets/italy-night-200px.jpg)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas ac erat in varius. Mauris blandit neque metus, nec mattis justo dapibus ut. Curabitur in nulla felis. Nam posuere fermentum mattis. Sed ut turpis sapien. Etiam sapien justo, feugiat at enim ut, venenatis elementum mauris. In hac habitasse platea dictumst. Duis vel tristique justo. Morbi erat nunc, viverra eget maximus eget, mollis sed felis. Nullam nibh lorem, porta at tellus vitae, condimentum convallis mauris. Maecenas nec neque vitae arcu blandit aliquet. Duis sodales ut turpis non aliquet. Mauris vitae tellus nulla. Vivamus malesuada aliquam tortor.
""",
                "icons": """
## Credits
- Le immagini notturni della Terra "VIIRS Stray Light Corrected Nighttime Day/Night Band Composites Version 1", di pubblico dominio, ottenuti e elaborati tramite [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG).
- Icone realizzate da [Freepik](https://www.freepik.com) da [www.flaticon.com](https://www.flaticon.com/).
"""
        }

)
