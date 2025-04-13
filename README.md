# Pelikirjasto
HY:n Tietokannat ja web-ohjelmointi -kurssin harjoitustyö

## Sovelluksen kuvaus
Sovelluksen tarkoituksena on mahdollistaa käyttäjälle lista hänen omistamistaan (lauta)peleistä. Eri käyttäjät voivat nähdä toistensa pelikirjastot sekä arvioida pelejä (kuten haastavuus ja arvosana).

## Sovelluksen toiminnot
- [x] Käyttäjä voi luoda uuden käyttäjätunnuksen
- [x] Käyttäjä voi kirjautua sisään käyttäjätunnuksella ja salasanalla
- [x] Käyttäjä voi lisätä sovellukseen pelejä
- [x] Käyttäjä voi poistaa sovelluksesta pelejä
- [x] Käyttäjä voi lisätä ja muokata peleille tietoja, kuten pelaajamäärän ja pelin ikäsuosituksen
- Käyttäjällä on käyttäjäsivut, josta näkee käyttäjän pelikirjaston ja arvioidut pelit
  - [x] Käyttäjällä on alkeelliset käyttäjäsivut
- [x] Käyttäjä voi nähdä muiden käyttäjien lisäämät pelit
- Käyttäjä voi etsiä pelejä hakemalla peliä nimellä, pelaajamäärällä tai ikäsuosituksella
  - [x] Käyttäjä voi etsiä pelejä hakemalla peliä nimellä
- [x] Käyttäjä voi määrittää pelille vaikeustason ja arvosanan
- Pelejä voi järjestää vaikeustason tai arvosanan mukaan

## Sovelluksen nykytilanne välitavoitteiden mukaan
Välipalautus 3:n tavoitteiden mukaisesti:
- Sovelluksessa on (alkeellinen) käyttäjäsivu, joka näyttää tällä hetkellä vain sovellukseen lisättyjen pelien määrän
- Tietokohteilla eli peleillä on useampi luokittelu ja luokittelut ovat tietokannassa
- README.md-tiedosto kuvaa, mikä on sovelluksen nykyinen tilanne.

Välipalautus 2:n tavoitteiden mukaisesti:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään ja muokkaamaan tietokohteita.
- Käyttäjä näkee sovellukseen lisätyt tietokohteet.

## Sovelluksen käynnistäminen
Luo ja käynnistä virtuaaliympäristö:
`$ python3 -m venv venv`
`$ source venv/bin/activate`
Tämän jälkeen asenna flask-riippuvuus:
`$ pip install flask`
