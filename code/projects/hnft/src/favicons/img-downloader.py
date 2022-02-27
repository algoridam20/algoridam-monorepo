import urllib.request
import urllib.parse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import sched
import datetime
import os





def getNewURL(url):
    req = urllib.request.Request(url)
    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        if e.status != 307:
            raise  # not a status code that can be handled here
        redirected_url = urllib.parse.urljoin(url, e.headers['Location'])
        resp = urllib.request.urlopen(redirected_url)
        print(f"Redirected : {redirected_url} -> {resp.url}") 
    return resp.url

def generateUrl4mDomain(url):
    return f"https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=http://{url}&size=256"

def saveImage(url,domain):
    name = domain.replace(".","_")
    try:
        urllib.request.urlretrieve(url, f"{name}.png")
    except:
        try:
            newURL = getNewURL(f"https://{domain}/favicon.ico")
            urllib.request.urlretrieve(newURL, f"{name}.png")
        except:
            print(f"unable to download {name}")

allDomains = [
    'expressjs.com',
    'google.com',
    'logrocket.com',
    'plainenglish.io',
    'freecodecamp.org',
    'npmjs.com',
    'dev.to',
    'stackoverflow.com',
    'netflix.com',
    'youtube.com',
    'diagrams.net',
    'twitter.com',
    'nytimes.com',
    'cleartrip.com',
    'educative.io',
    'primevideo.com',
    'amazon.com',
    'leetcode.com',
    'quora.com',
    'outlookindia.com',
    'kiwicollection.com',
    'thomascook.in',
    'holidify.com',
    'airbnb.co.in',
    'thrillophilia.com',
    'tripadvisor.in',
    'rd.com',
    'yatra.com',
    'indianholiday.com',
    'travelandleisureindia.in',
    'travelandleisure.com',
    'mobilefirst.me',
    'github.com',
    'changelog.com',
    'nodejs.org',
    'chrome.com',
    'jsfiddle.net',
    'snyk.io',
    'cssscript.com',
    'medium.com',
    'javascripttutorial.net',
    'c-sharpcorner.com',
    'github.io',
    'com.ua',
    'gstatic.com',
    'colorhexa.com',
    'html-color-codes.info',
    'whatsapp.com',
    'mozilla.org',
    'learningdollars.com',
    'techwiser.com',
    'requirejs.org',
    'quick-adviser.com',
    'codegrepper.com',
    'extract.pics',
    'imgdownloader.com',
    'animefillerlist.com',
    'crunchyroll.com',
    'indianexpress.com',
    'reddit.com',
    'amazon.in',
    'ign.com',
    'blockchainireland.ie',
    'moneycontrol.com',
    'infoq.com',
    'veritas.com',
    'wikipedia.org',
    'top10stockbroker.com',
    'iciciprupms.com',
    'geojit.com',
    'theverge.com',
    'discord.com',
    'movr.network',
    'socket.io',
    'powerlanguage.co.uk',
    'flipkart.com',
    'wsj.com',
    'pcgamesn.com',
    'hotstar.com',
    'ithoughtria.co.in',
    'gov.in',
    'gripinvest.in',
    'hdfcbank.com',
    'indiatimes.com',
    'cleartax.in',
    'tax2win.in',
    'howtogeek.com',
    '9to5mac.com',
    'khatabook.com',
    '9anime.vc',
    'happierhuman.com',
    'oyehappy.com',
    'geeksforgeeks.org',
    'google.co.in',
    'carta.com',
    'britannica.com',
    'dzone.com',
    'clearbridgemobile.com',
    'indiatoday.in',
    'workat.tech',
    'smcinternational.in',
    'elitehubs.com',
    'pcstudio.in',
    'golchhait.com',
    'mdcomputers.in',
    'antesports.com',
    'ndtv.com',
    'jsonformatter.org',
    'wordhippo.com',
    'scrabblewordfinder.org',
    'scrapy.org',
    'analyticsvidhya.com',
    'googletagmanager.com',
    'flaticon.com',
    'shutterstock.com',
    'quip-amazon.com',
    'fast.com',
    'uxdesign.cc',
    'oracle.com',
    'microsoft.com',
    'icicidirect.com',
    'adblock-for-youtube.com',
    'getadblock.com',
    'wakefit.co',
    'mkyong.com',
    'a2z.com',
    'amazon-corp.com'
]

def main():
    getNewURL("https://leetcode.com/favicon.ico")
    # for domain in allDomains:
    #     url = generateUrl4mDomain(domain)
    #     saveImage(url,domain)


if __name__ == "__main__":
    main()