import json
import urllib.request
import imshime
import os

imshime.api_create()

def makeURL(location, radius, type="convenience_store"):
    api_key = os.getenv('API_KEY_ROUTE')
    latlng = str(location[0]) + "," + str(location[1])
    requestURL = r"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+latlng+"&radius="+radius+"&types="+type+"&language=ja&key="+str(api_key)
    print(requestURL)
    return(requestURL)

def printResultLog(url, timeout=10):
    try:
        with urllib.request.urlopen(url) as result:
            html = result.read().decode('utf-8')
            json_result = json.loads(html)

            conv = []
            i = 0
            try:
                while((json_result["results"][i]["name"] is not None) and (json_result["results"][i]["vicinity"] is not None)):
                    name = json_result["results"][i]["name"]
                    vicinity = json_result["results"][i]["vicinity"]
                    conv.append([name,vicinity])
                    i += 1
            except IndexError:
                print("")
            return (conv)

    except:
        print("ERROR!")
        import traceback
        traceback.print_exc()


