from geopy.geocoders import Nominatim
from math import sin, cos, pi, pow, degrees, radians
from sys import argv, exit

def format_latitude(lat_degrees):
    """Fixes latitudes that have gone over 90 degrees"""
    latitude = float(lat_degrees)
    if abs(latitude) > 90:
        latitude = ((latitude + 90) % 180) - 90
    return latitude


def format_longitude(lng_degrees):
    """Fixes longitudes that have gone over 180 degrees"""
    longitude = float(lng_degrees)
    if abs(longitude) > 180:
        longitude = ((longitude + 180) % 360) - 180
    return longitude


def get_degree_len(lat_degrees):
    """
    Calculates length of a degree of latitude and longitude based on geodetic 
    meridian for any latitude and longitude position on an elipsoid without need of 
    any external API or data. Constants based on elipsoid values used in WGS84, 
    replicating calculation used by National Geospatial Agency (NDA) and CSGnet.
    Formula is in a format that minimizes error at high latitudes by not dividing 
    by cosines (like haversine calculations).
 
    Result is a pair of floating point distances (lat_len, lng_len) in km

    Recommended for simple distance and geofence calculations below 88 degrees 
    latutude and for distances and dimensions up to 200 km. Calculation has 
    error rate <0.1% error at equator, under 3% (longitude) at the poles.  
    """
    ## Values for Earth, could swap in Mars, the Moon, etc.
    EARTH_EQUATORIAL_RADIUS = 6378.137 # km
    EARTH_POLAR_RADIUS = 6356.7523142 # km
    EARTH_ECCENTRICITY_SQUARED = 0.00669437999014 

    a = EARTH_EQUATORIAL_RADIUS
    b = EARTH_POLAR_RADIUS
    e_squared = EARTH_ECCENTRICITY_SQUARED

    lat_radians = radians(format_latitude(lat_degrees))

    lat_len = (pi * a * (1.0 - e_squared)) / \
        (180.0 * pow(1 - (e_squared * pow(sin(lat_radians), 2)), 1.5))

    lng_len = (pi * a * cos(lat_radians)) / \
        (180.0 * pow(1 - (e_squared * pow(sin(lat_radians), 2)), 0.5))
    
    return lat_len, lng_len


def half_even_round(x):
    """Round number to N digits"""
    return x


def parse_opts(argv):
    """Parse options"""
    return y


def build_fc(centroid, height, width, precision=4, method='vincenty'):
    """Returns geojson"""
    return fc 


def geocode_addr(address):
    """returns lat, lng for address (if possible)"""
    geolocator = Nominatim()
    location = geolocator.geocode(address, True)
    if not location:
        print "No location for address available"
        exit(404)
    return (location.latitude, location.longitude)



