# -*- coding: utf8 -*-
from webdriverdownloader import GeckoDriverDownloader

def download_geckodriver():
    gdd = GeckoDriverDownloader()
    gdd.download_and_install()
