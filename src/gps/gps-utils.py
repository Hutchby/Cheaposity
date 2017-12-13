#!/usr/bin/env python3

from math import pi, atan

def coord_to_deg(coord):
    deg = coord['degrees'] + 60 * coord['minutes']
    ind = coord['indicator']
    return deg if ind == 'N' or ind == 'E' else -deg

def to_deg(rad):
    return deg * 180 / pi

def to_rad(deg):
    return deg * pi / 180


def get_infos(coord1, coord2):
    coord1_lat = to_rad(coord_to_deg(coord1[0]))
    coord1_long = to_deg(coord_to_deg(coord1[1]))
    coord2_lat = to_deg(coord_to_deg(coord2[0]))
    coord2_long = to_deg(coord_to_deg(coord2[1]))

    lat_diff = coord2_lat - coord1_lat
    long_diff = coord2_long - coord1_long
    if not long_diff:
        return (0, lat_diff, long_diff) if lat_diff > 0 else (pi, lat_diff,
                long_diff)
    azimuth = (pi * 0.5) - atan(lat_diff / long_diff)
    if long_diff > 0:
        return (azimuth, lat_diff, long_diff)
