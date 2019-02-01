import src.subsdb
import src.opensubtitles
import logging

def provision(hash, lang):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Received request for hash "+hash)
    subData = subsdb.getSubs(hash,lang)
    if subData:
        return subData
    
    subData=opensubtitles.getSubs(hash, lang)
    if subData:
        return subData

    logging.info("Subtitles for "+hash+" not found")
    return None