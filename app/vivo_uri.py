#import hashlib
import random
import requests
import sys

#Prefixes
PREFIX_AWARD = "n"
PREFIX_AWARDED_DEGREE = "n"
PREFIX_DEGREE = "n"
PREFIX_DOCUMENT = "pub"
PREFIX_GRANT = "awd"
PREFIX_JOURNAL = "n"
PREFIX_ORGANIZATION = "org"
PREFIX_PERSON = "per"

#API info
email='vivo_root@yourdomain.edu'
password='password'
api_url='http://vivo.yourdomain.edu/vivo/api/sparqlQuery'
aboxgraph='http://vitro.mannlib.cornell.edu/default/vitro-kb-2' #this is the default
namespace='http://vivo.yourdomain.edu/individual/'

def to_hash_identifier(prefix, parts):
    while True:
        vivouri = prefix + str(random.randint(100000,999999))
        payload = {'email': email, 'password': password, 'query': 'ASK WHERE {GRAPH <'+aboxgraph+'> { <'+namespace+vivouri+'> ?p ?o . }  }' }
        r = requests.post(api_url,params=payload)
        exists=r.text
        if exists=='false':
            return vivouri
            break

        if exists not in ('true','false'):
            sys.exit("VIVO API error! Script is aborting.\nVerify your API info in vivo_uri.py file.")

'''
def to_hash_identifier(prefix, parts):
    """
    Return an identifier composed of the prefix and hash of the parts.
    """
    hash_parts = hashlib.md5("".join([unicode(part) for part in parts if part]).encode("utf-8"))
    return "%s-%s" % (prefix, hash_parts.hexdigest())
'''
