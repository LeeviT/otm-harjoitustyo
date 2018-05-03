# N-kappaleen ongelma -simulaatio

Sovellus simuloi usean kappaleen välistä gravitaatiovuorovaikutusta.

**Käytän harjoitustyössä kielenä Pythonia.**

## Dokumentaatio

[vaatimusmäärittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[työaikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuridokkari](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[sekvenssikaavio](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio.md)

## Releaset
[viikon 5 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.1-alpha)
[viikon 6 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.2-alpha)

## Komentorivitoiminnot
### Virtuaaliympäristö
Sovellusta ajetaan (mieluiten) virtuaaliympäristössä _virtualenv_ illä. Sen voit käynnistää projektin juuressa _otm-harjoitustyo/_ komennolla
```
source venv/bin/activate
```

### Vaatimukset
Projektin buildaamiseen vaaditaan _pipin_ versiota 10.0.0 alempi versio sekä _PyBuilder_. _PyBuilderin_ saat asennettua aktivoimalla ensin virtuaaliympäristö (ks. yllä) ja suorittamalla komennon
```
pip install pybuilder
``` 
sekä _numpy_:
```
pip install numpy
```

### Testaus
Koodia testataan PyBuilderin avulla. Checkstylen tekeminen _flake8_:lla, sekä yksikkö testien että testauskattavuuden generoiminen tapahtuu komennolla
```
pyb analyze
```
Ensin PyBuilder tulostaa outputissa checkstyle-virheiden määrän. Sitten _unittest_ ajaa yksikkötestit ja _coverage.py_ vielä generoi testauskattavuusraportin. Testauskattavuusraportin voi avata esim. Chromiumilla komennolla 
```
chromium target/reports/coverage_html/index.html 
```
Ja mikäli checkstyle-virheitä on, on checkstyle-raportin polku _target/reports/flake8_.

### Suoritettavan whl:n generointi ja ohjelman suorittaminen
Projektin juuressa eli _otm-harjoitustyo/_ suorita komento 
```
pyb publish
```
jolloin _.whl_-tiedosto generoituu _target_-kansion alakansioon. Voit suorittaa _wheelin_ kommennolla
```
python3.6 target/dist/nbodysim-1.0.dev0/dist/nbodysim-1.0.dev0-py3-none-any.whl 
```

