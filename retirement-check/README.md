# Esercizio

* Chiedi l'età e il genere ("M" o "F"). Se è uomo e ha >= 67 anni o donna e ha >= 62 anni, stampa "Puoi andare in pensione", altrimenti "Devi ancora lavorare".

## Ragionamento

* inizializzazione di genere
* do
  * leggi genere da utente;
  * dichiarazione di due array per M e F ;
  * se array M include;
    * g ottiene M come valore
  * altrimenti se array F include;
    * g ottiene F come Valore;
* while per correggere l'utente in caso di termini incorretti per il genere;

* leggi eta utente ;
* se genere === M && eta >= 67 || genere === F && eta >= 62
  * stampa puoi andare in pensione ;
* else
  * stampa Devi ancora lavorare.

---

## Exercise

* Ask the age and gender ("M" or "F"). If it is a man and has >= 67 years or a woman and has >= 62 years, print "You can retire", otherwise "You still have to work".

## Reasoning

* gender initialization
* do
  * read gender from user;
  * declaration of two arrays for M and F;
  * if array M includes;
    * g gets M as value
  * otherwise if array F includes;
    * g gets F as value;
* while to correct the user in case of incorrect terms for gender;

* read user age;
* if gender === M && age >= 67 || gender === F && age >= 62
  * print you can retire;
* else
  * print you still have to work.
