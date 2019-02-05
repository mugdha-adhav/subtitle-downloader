import src.subsdb
import src.opensubtitles
import logging

def provision(subrequest, lang):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Received request for subtitle download ")
    
    subData=opensubtitles.getSubs(subrequest.opensubshash, subrequest.filesize, lang)
    if subData:
        return subData
        
    subData = subsdb.getSubs(subrequest.subsdbhash,lang)
    if subData:
        return subData

    logging.info("Subtitles not found")
    return None