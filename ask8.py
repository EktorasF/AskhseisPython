import urllib.request
import json
url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
r=urllib.request.urlopen(url)
html=r.read()
html=html.decode()
d=json.loads(html)
btc = d["BTC"]["EUR"]
eth = d["ETH"]["EUR"]
ltc = d["LTC"]["EUR"]

f = open("Εισάγετε το txt αρχείο σας με το λεξικό (ολόκληρο το path)", "r")
dict = f.read()
dict = json.loads(dict)

dBTC = dict.get("BTC")
dETH = dict.get("ETH")
dLTC = dict.get("LTC")

BTCvalueEURO = dBTC*btc
ETHvalueEURO = dETH*eth
LTCvalueEURO = dLTC*ltc

print("Τα κρυπτονομίσματα BTC που έχετε, αντιστοιχούν σε ",BTCvalueEURO, "ευρώ")
print("Τα κρυπτονομίσματα ETH που έχετε, αντιστοιχούν σε ",ETHvalueEURO, "ευρώ")
print("Τα κρυπτονομίσματα LTC που έχετε, αντιστοιχούν σε ",LTCvalueEURO, "ευρώ")
