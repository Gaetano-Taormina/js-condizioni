# Esercizio

* Chiedi l'età e il genere ("M" o "F"). Se è uomo e ha >= 67 anni o donna e ha >= 62 anni, stampa "Puoi andare in pensione", altrimenti "Devi ancora lavorare".

## Ragionamento

* leggi Genere dell' utente ;
* dichiarazione di due array per M e F ;
  * ottenimento del genere tramite includes dentro un if;
  * se array M include;
    * g ottiene M come valore
  * altrimenti se array F include;
    * g ottiene F come Valore;

* do while per correggere l'utente in caso di termini incorretti per il genere;

* leggi eta utente ;
  * se genere === M && eta >= 67 || genere === F && eta >= 62
    * stampa puoi andare in pensione ;
  * else
    * stampa Devi ancora lavorare.
