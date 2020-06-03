import requests
import sys

from lxml import html

# read a share as a google url get parameter 
# search for a given xpath
# if smth is found then return otherwise None

def getShareValue(share):
    url = "http://www.google.de/search?q=" + share + "+Aktie"
    r = requests.get(url)
    tree = html.fromstring(r.content)
    
    xpath = "/html/body/div/div[4]/div/div[3]/div/div/div/div/div[1]/div/div/div/div"
    share = tree.xpath(xpath)
    r.close()
    
    if(len(share) > 0):   
        return share[0].text
    
    return None
 
if __name__ == "__main__":
    
    # check if enough args are given
    if len(sys.argv) < 2:
        print("[-] Missing argument, please enter a share name")
        sys.exit()
    
    # var assign
    for i in range(1, len(sys.argv)):
        share = sys.argv[i]
        value = getShareValue(share)

        # output
        if value == None:
            print("[-] " + share + " was not found")

        else:
            print("[*] " + str(share) + ": " + str(value) + "€")

    
    
