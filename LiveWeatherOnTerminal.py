# Below code is to generate live Weather when on Terminal

import urllib3
import json
http = urllib3.PoolManager()

# below function is will generate zip code of the current location besed on the current ip address
def get_my_zip():
    
    zip_code = http.request('GET','http://ip-api.com/json')
    zip_data = json.loads(zip_code.data)
    #print(zip_data)
    return zip_data['zip']+','+zip_data['countryCode'].lower()
        
# Below function will generte all pull all the necessary weather readings based on the zip code given
def get_waether_update(zip_country):
    
    weather_url = "https://samples.openweathermap.org/data/2.5/weather?zip="
    app_id = "&appid=b6907d289e10d714a6e88b30761fae22"
    url = weather_url + zip_country + app_id
    weather_json = http.request('GET', url)
    weather = json.loads(weather_json.data)
    
    # here we are extracting all individual readings 
    condition = weather["weather"][0]["main"]
    temp = json.dumps(weather["main"]["temp"])
    hitemp = json.dumps(weather["main"]["temp_max"])
    lotemp = json.dumps(weather["main"]["temp_min"])
    humidity = json.dumps(weather["main"]["humidity"])
    pressure = json.dumps(weather["main"]["pressure"])
    
    # here we are printing out the the reading that we parsed above
    print("CONDITION                    %s    " % condition)
    print("TEMPERATURE                  %sF  " % temp)
    print("HIGH                         %sF  " % hitemp)
    print("LOW                          %sF  " % lotemp)
    print("HUMIDITY                     %s%%    " % humidity)
    print("PRESSURE                     %smbar" % pressure)

# Now we are going to print the result out
get_waether_update(get_my_zip())
