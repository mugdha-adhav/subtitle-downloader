import logging
import requests
import constants

def getSubs(HASH,LANG):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Searching subs in subsDB...")
    ACTION = "download"
    URL = constants.SUBDB_URL + "/?action=" + ACTION + "&hash=" + HASH + "&language=" + LANG
    HEADERS={
        'User-Agent': constants.USER_AGENT_SUBSDB
    }
    response = requests.get(url = URL, headers=HEADERS)
    if not response:
        logging.warning("Subsdb no response received.") 
    elif response.status_code == 200:
        logging.info("Subtitles found in subsdb for hash "+HASH)
        return response.text
    elif response.status_code == 400:
        logging.warning("Subsdb request malformed. Returned status code: ", response.status_code) 
    elif response.status_code == 404:
        logging.info("Subtitles for hash "+HASH+" not found in subsdb")
    else: 
        logging.info("Error retrieving subtitles. Response status code is %d",response.status_code)
        logging.info("Response message is: "+response.text)
    return None