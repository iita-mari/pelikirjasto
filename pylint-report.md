# Pylint-raportti

Pylint suoritettiin komennolla `pylint *.py` ha se antoi seuraavan raportin:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:103:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:112:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:118:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:146:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:188:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:222:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:236:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:222:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:243:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:270:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:280:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:270:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:290:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:297:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:301:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:96:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "item_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:26:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.33/10 (previous run: 8.33/10, +0.00)
```
## Raportin tulokset

### Docstring
Ilmoitukset, kuten
```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
```
kertovat, että sovelluksen moduuleista, funktioista tai metodeista puuttuvat docstring-kommentit. Näitä ei vaadittu kurssilla ja niiden poisjättäminen on tietoinen päätös.

## Puuttuva palautusarvo
Ilmoitukset, kuten
```
app.py:58:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
koskevat tilanteita, jossa palautetaan koodissa `GET` tai `POST`, mutta on teoreettinen (ei käytännön) mahdollisuus, että olisi tilanne, jossa palautettaisiin jotain muuta. Funktiot on kuitenkin kirjoitettu niin, että niissä vaaditaan `GET` tai `POST` joten muita palautusarvoja ei tarvita ja virheilmoitusta ei tarvitse huomioida.

### Tarpeeton else
Ilmoitukset, kuten
```
app.py:236:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```
kertovat, että koodin olisi voinut kirjoittaa tiiviimmin ilman `else`haaraa. On kuitenkin tietoinen (ja selkeämpi) päätös toteuttaa koodi kirjoittamalla molemmat, sekä `if`- että `else`-vaihtoehdot auki eikä varsinainen virhe.

### Vakion nimi
Ilmoitukset, kuten
```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "item_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
```
liittyvät vakion kirjoittamistyyliin. Pythonin (ja kurssin) käytäntöjen mukaisesti nimet on kirjoitettu kokonaan pienillä kirjaimilla ja sanojen välissä on alaviiva.

### Vaarallinen oletusarvo
Ilmoitukset, kuten
```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
liittyvät vaaralliseen oletusarvoon. Parametrin oletusarvo on tyhjä lista `[]`, jota ei tässä sovelluksessa haittaa, sillä koodissa ei ole asioita, jotka muuttaisivat kyseistä listaoliota.
