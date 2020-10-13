import json
import urllib.request
import imshime
import os

imshime.api_create()

def makeConversionURL(convList):
    api_key = os.getenv('API_KEY_ROUTE')
    convURLList = []
    conv = {'spot':[]}
    convList_len = len(convList)
    for i in range(convList_len):
        convName = convList[i][1]
        conv['spot'].append({'address':convName})
        convAdress = urllib.parse.quote_plus(convName, encoding='utf-8')
        request_url = r"https://maps.googleapis.com/maps/api/geocode/json?address="+convAdress+"&components=country:JP&key="+str(api_key)
        convURLList.append(request_url)
    return (convURLList, conv)

def printConversionLog(convURLList, conv, timeout=10):
    convURLList_len = len(convURLList)
    for i in range(convURLList_len):
        convURL = convURLList[i]
        try:
            with urllib.request.urlopen(convURL) as result:
                html = result.read().decode('utf-8')
                json_result = json.loads(html)
                lat = json_result["results"][0]["geometry"]["location"]["lat"]
                lng = json_result["results"][0]["geometry"]["location"]["lng"]
                conv['spot'][i]['lat'] = lat
                conv['spot'][i]['lng'] = lng
        except:
            print("ERROR!")
            import traceback
            traceback.print_exc()
    return(conv)
