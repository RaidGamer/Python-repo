#Application Programming Interface
# är ett program som hämtar information från andras web databaser 
# som tex från google, och den informationen kan då senare bli implementerad i ens egna program i python eller vilket annat språk som helst.

import sys, requests, json

if len(sys.argv) != 2:
    sys.exit()

#http request till itunes om results baserat på din input (vilken artist du valde)
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

obj = response.json() #lagrar json results i en var

print(json.dumps(response.json(), indent = 2)) #printas som en lista med alla resultat i json format

for result in obj["results"]: #filtrerar genom result key value pair som innehåller alla resultat
    print(result["trackName"]) #söker specifikt för trackName i results och printar ut en sång från specifierade artist