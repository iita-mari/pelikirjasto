# Pelikirjasto
HY:n Tietokannat ja web-ohjelmointi -kurssin harjoitustyö

## Sovelluksen kuvaus
Sovelluksen tarkoituksena on mahdollistaa käyttäjälle lista hänen omistamistaan (lauta)peleistä. Eri käyttäjät voivat nähdä toistensa pelikirjastot sekä arvioida pelejä (kuten haastavuus ja arvosana).

## Sovelluksen toiminnot
- [x] Käyttäjä voi luoda uuden käyttäjätunnuksen
- [x] Käyttäjä voi kirjautua sisään käyttäjätunnuksella ja salasanalla
- [x] Käyttäjä voi lisätä sovellukseen pelejä
- [x] Käyttäjä voi poistaa sovelluksesta pelejä
- [x] Käyttäjä voi lisätä ja muokata pelien tietoja
- [x] Käyttäjä voi määrittää pelille vaikeustason ja arvosanan
- [x] Käyttäjällä on käyttäjäsivut, josta näkee käyttäjän pelikirjaston, käyttäjän lisäämien pelien määrät ja käyttäjän antamat tiedot peleille
- [x] Käyttäjä voi nähdä muiden käyttäjien lisäämät pelit
- [x] Käyttäjä voi etsiä pelejä hakemalla peliä nimellä

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
