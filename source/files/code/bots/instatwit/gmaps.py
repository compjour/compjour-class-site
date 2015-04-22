import requests
def get_location_from_address(addr):
    """

    Returns: dict, the API response from Google
    """
    baseurl = 'https://maps.googleapis.com/maps/api/geocode/json'
    resp = requests.get(baseurl, params = {'address': addr})
    return resp.json()


def get_lat_lng_from_address(addr):
    data = get_location_from_address(addr)
    # get the first result
    if len(data['results']) > 0:
        r = data['results'][0]
        return r['geometry']['location']
    else:
        return None
