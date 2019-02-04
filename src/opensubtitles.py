import logging
import constants
from xmlrpc.client import ServerProxy, Transport

def login():
    transport = Transport()
    transport.user_agent = constants.USER_AGENT
    xmlrpc = ServerProxy(constants.OPENSUBTITLES_URL, allow_none=True, transport=transport)
    data = xmlrpc.LogIn(constants.USERNAME, constants.PASSWORD, constants.LANGUAGE, constants.USER_AGENT)
    token = data.get('token') if '200' == data.get('status').split()[0] else None
    return token

def getSubs(hash,lang):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Searching subs in opensubtitles...")

    token = login()

    #return "your subs",True
    return None