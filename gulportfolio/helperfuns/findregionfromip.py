from ip2geotools.databases.noncommercial import DbIpCity

def findregionfromip(ipaddr):
    response = DbIpCity.get(ipaddr, api_key='free')
    return str(response.city+", "+response.country)