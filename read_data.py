import pprint
import glob
import os
import xml.etree.ElementTree
from dateutil import parser
import pandas as pd
import numpy as np


def parse(filename):
    e = xml.etree.ElementTree.parse(filename).getroot()
    total = {}
    total["totalPresent"] = e.find("totalPresent").text
    total["totalLibre"] = e.find("totalLibre").text

    parcs = {}
    # XPATH notation
    # https://fr.wikipedia.org/wiki/XPath
    for parc in e.findall("Quartier/Parc"):
        nom = parc.find("libelleParc").text
        try:
            libre = int(parc.find("placesLibresParc").text)
        except ValueError:
            # certaines cases ont écrit obsolete...
            libre = np.nan
        parcs[nom] = libre

    date = parser.parse(parc.find("placesLibresUpdate").text)

    return date, total, parcs


def _get_dataframe():
    path = "./data/**/*.xml"
    res = pd.DataFrame()
    for fname in glob.glob(path, recursive=True):
        print("processing", fname)
        date, total, parcs = parse(fname)
        parcs["date"] = date
        df = pd.DataFrame(parcs, index=[res.shape[0]])
        res = res.append(df)
    return res


def get_dataframe():
    FILENAME = "./data/janvier.feather"
    if os.path.exists(FILENAME):
        print("using {} stored dataframe".format(FILENAME))
        df = pd.read_feather(FILENAME)
    else:
        print("loading dataframe for XML files")
        df = _get_dataframe()
        df.to_feather(FILENAME)

    # on ne peut pas stocker d'index temporel dans le feather
    # on met la colonne date comme un index et on la supprime du dataframe
    df.index = df.date
    df = df.drop("date", 1)
    return df.sort_index()


if __name__ == "__main__":
    main()

