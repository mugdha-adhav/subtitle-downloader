import logging
import requests
import constants

def getSubs(HASH,LANG):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Searching subs in subsDB...")
    ACTION = "download"
    URL = constants.SUBDB_URL + "/?action=" + ACTION + "&hash=" + HASH + "&language=" + LANG
    HEADERS={
        'User-Agent': 'SubDB/1.0 (subsworld/1.0; http://github.com/mugdhaadhav/subtitle-downloader)'
    }
    response = requests.get(url = URL, headers=HEADERS)
    if response.status_code == 400:
        logging.warning("Subsdb request malformed. Returned status code: ", response.status_code) 
    elif response.status_code == 404:
        logging.info("Subtitles for hash "+HASH+" not found in subsdb")
    elif response.status_code == 200:
        logging.info("Subtitles found in subsdb for hash "+HASH)
        return response.text
    return None