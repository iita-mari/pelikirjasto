# Pelikirjasto
HY:n Tietokannat ja web-ohjelmointi -kurssin harjoitustyö

## Sovelluksen kuvaus
Sovelluksen tarkoituksena on mahdollistaa käyttäjälle lista hänen omistamistaan (lauta)peleistä. Eri käyttäjät voivat nähdä toistensa pelikirjastot.

## Sovelluksen toiminnot
- [x] Käyttäjä voi luoda uuden käyttäjätunnuksen
- [x] Käyttäjä voi kirjautua sisään käyttäjätunnuksella ja salasanalla
- [x] Käyttäjä voi lisätä sovellukseen pelejä
- [x] Käyttäjä voi poistaa sovelluksesta pelejä
- [x] Käyttäjä voi lisätä ja muokata pelien tietoja
- [x] Käyttäjä voi määrittää pelille vaikeustason ja arvosanan
- [x] Käyttäjällä on käyttäjäsivut, josta näkee käyttäjän lisäämät pelit, pelien määrän ja pääsee katsomaan käyttäjän antamia tietoja peleille
- [x] Käyttäjä voi lisätä profiiliinsa kuvan ja vaihtaa sen
- [x] Käyttäjä voi nähdä muiden käyttäjien lisäämät pelit ja niille annetut tiedot
- [x] Käyttäjä voi etsiä pelejä hakemalla peliä nimellä
- [x] Pelejä voi kommentoida

## Sovelluksen asennus ja käynnistäminen
1. Luo ja käynnistä virtuaaliympäristö:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Asenna flask-riippuvuus:
```
$ pip install flask
```

3. Alusta tietokanta ja lisää alkutiedot:
```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

4. Käynnistä sovellus:
```
$ flask run
```

## Suuren tietomäärän käsittely
Sovelluksen toimivuutta suuren tietomäärän käsittelyssä on testattu `seed.py` tiedoston avulla. `seed.py` on toteutettu kurssin materiaalin mukaisesti ja se luo tuhat käyttäjää, miljoona peliä ja kymmenen miljoonaa kommenttia.

Sivuston lataamiseen kuluva aika:
- Ilman sivutusta ja indeksöintiä: 8.57s
- Sivutus, ei indeksöintiä: 0.2s
- Sivutus ja indeksöinti: 0.02s