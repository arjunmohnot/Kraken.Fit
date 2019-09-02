
# origin_loc = '28.339274, 77.316538'
# #destin_loc = origin_loc
# waypoints = ['28.469248, 77.307786', '28.487120, 77.303272', '28.503869, 77.279928', '28.487120, 77.303272', '28.469248, 77.307786']


def mapsUrlGenerator(origin_loc, waypoints):
    url_ext_origin_loc = origin_loc.replace(',','%2C').replace(' ','+')
    url_ext_waypoints = (("%7C".join(waypoints)).replace(',','%2C')).replace(' ','+')

    maps_url = 'https://www.google.com/maps/dir/?api=1&origin={}&destination={}&travelmode=walking&waypoints={}'.format(url_ext_origin_loc, url_ext_origin_loc, url_ext_waypoints)

    #return(maps_url)
    print(maps_url)

mapsUrlGenerator(origin_loc, waypoints)
