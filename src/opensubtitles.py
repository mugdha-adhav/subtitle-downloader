import logging
import constants
from xmlrpc.client import ServerProxy, Transport
import zlib
import base64

def login():
    transport = Transport()
    transport.user_agent = constants.USER_AGENT_OPENSUBS
    xmlrpc = ServerProxy(constants.OPENSUBTITLES_URL, allow_none=True, transport=transport)
    try:
        data = xmlrpc.LogIn(constants.USERNAME, constants.PASSWORD, constants.LANGUAGE, constants.USER_AGENT_OPENSUBS)
    except:
        logging.warning("Error occured while establishing connection to opensubtitles...")
        return None,None
    if '200' == data.get('status').split()[0]:
        logging.info("Got token from opensubtitles")
        return data.get('token'),xmlrpc  
    else: 
        logging.warning("Error occured while getting opensubtitles token. Returned status as "+data.get('status').split()[0])
        return None

def getSubs(hash,size,lang):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Searching subs in opensubtitles...")

    token,xmlrpc = login()
    if token:
        data=xmlrpc.SearchSubtitles(token, [{'sublanguageid': 'eng', 'moviehash': hash, 'moviebytesize': size}])
        if '200' == data.get('status').split()[0]:
            logging.info("Searching subtitles ended successfully...")
            data=data.get('data')  
            data=xmlrpc.DownloadSubtitles(token, [data[0].get('IDSubtitleFile')])
            if '200' == data.get('status').split()[0]:
                logging.info("Downloading subtitles ended successfully...")
                encoded_data=data.get('data')  
                if not encoded_data:
                    logging.warning("Downloaded data is empty...")
                    return None
                try:
                    decoded_data = base64.b64decode(encoded_data[0].get('data'))
                    decoded_data = zlib.decompress(decoded_data, 16+zlib.MAX_WBITS)
                    decoded_data = decoded_data.decode('utf-8')
                except:
                    logging.warning("Error occured while decoding data...")
                    return None
                if not decoded_data:
                    logging.warning("Decoded data is empty...")
                    return None
                return decoded_data
            else:
                logging.warning("Error occured while downloading subtitles. Error code is: "+data.get('status').split()[0])
                return None          
        else:
            logging.warning("Error occured while searching subtitles. Error code is: "+data.get('status').split()[0])
            return None  
    return None