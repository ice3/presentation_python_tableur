# Presentation Python / Pandas

Talk sur la base de la manipulation / traitement de données en python

* présentation de pandas
* utilisation pour manipuler et nettoyer des timeseries

## Utilisation

* pour lancer le notebook : `jupyter notebook`
* pour voir la présentation statique :
    * lancer un serveur web `python -m http.server 9898`
    * ouvrir son navigateur sur l'adresse http://localhost:9898/slides.html
    * fermer le serveur en faisant `ctrl-c`

## Contexte

Présentation donnée :

* [meetup linkvalue](https://www.meetup.com/fr-FR/Linkvalue-Tech-Lille/events/258791033/) Lille
    * 20 février 2019
    * [vidéo](https://www.youtube.com/watch?v=VdOycImBylg)

## Installation

Manipulation des

Projet python classique :

    pip install -r requirements.txt

### Installation de RISE

Pour avoir les slides interactives, j'utilise l'extension [RISE](https://damianavila.github.io/RISE/) pour les `jupyter notebook`

    jupyter-nbextension install rise --py --sys-prefix
    jupyter-nbextension enable rise --py --sys-prefix


## Organisation du code

* `read_data.py` : lecture des fichiers de données présent dans le dossier `data`
* `Python tableur -- analyse données monaco parking.ipynb` : notebook de la présentation
* `slides.html` : version statique de la présentation (il faut pouvoir servir les fichiers statiques)
* images : toutes les images utilisées dans la présentation
