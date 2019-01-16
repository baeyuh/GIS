# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:41:18 2019

@author: Subea
"""

from shapely.geometry import Point, LineString, Polygon
import geopandas as gpd
import pyproj
import logging


def create_point_geom(x_coord, y_coord):
    """
    A function that takes in a pair of x and y coordinate values to create a shapely point.
    
    Parameters
    ----------------------------------------------------
    x_coord : float x-coordinate value
    y_coord : float y-coordinate value
    
    Returns
    ----------------------------------------------------
    A shapely point
    """
    
    try:
        return Point(x_coord, y_coord)
    
    except Exception as e:
        return logging.exception(e)
    

def create_line_geom(point_geoms):
    """
    A function that takes in a list of shapely point geoms or coordinate pairs to create a line geometries.
    
    Parameters
    ----------------------------------------------------
    point_geoms: list of shapely.Points or tuple pairs of coordinates
    
    Returns
    ----------------------------------------------------
    Line geometries
    """

    line_geoms = LineString(point_geoms)

    try:
        return line_geoms
    
    except Exception as e:
        return logging.exception(e)


def create_poly_geom(geoms):
    """
    A function that takes in a list of shapely point geoms or line geoms to create a polygon.
    
    Parameters
    ----------------------------------------------------
    geoms: list of shapely.Points, tuple pairs of coordinates or line geometries
    
    Returns
    ----------------------------------------------------
    A polygon
    """
    
    try:
        if geoms[0].geom_type == 'Point':
            return Polygon([[p.x, p.y] for p in geoms])
        else:
            return Polygon(geoms)

    except Exception as e:
        return logging.exception(e)


def get_centroid(geoms):
    """
    A function that takes in a list of geometries and gets the centroid.
    
    Parameters
    ----------------------------------------------------
    geoms: list of any geometries
    
    Returns
    ----------------------------------------------------
    A list of centroid point geometries
    """
    
    try:
        return [g.centroid for g in geoms]
    
    except Exception as e:
        return logging.exception(e)
    

def get_rep_point(geoms):
    """
    A function that takes in a list of geometries and gets the centroid-like points within them.
    
    Parameters
    ----------------------------------------------------
    geoms: list of any geometries
    
    Returns
    ----------------------------------------------------
    A list of centroid-like point geometries within
    """
    
    try:
        return [g.representative_point() for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def get_area(geoms):
    """
    A function that takes in a list of geometries and gets the areas.
    
    Parameters
    ----------------------------------------------------
    geoms: list of any geometries
    
    Returns
    ----------------------------------------------------
    A list of area values
    """
    
    try:
        return [g.representative_point() for g in geoms]
    
    except Exception as e:
        return logging.exception(e)
    try:
        return [g.area for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def get_length(geoms):
    """
    A function that takes in a list of geometries and gets the lengths.
    
    Parameters
    ----------------------------------------------------
    geoms: list of any geometries
    
    Returns
    ----------------------------------------------------
    A list of length values
    """
    
    try:
        return [g.length for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def create_polygon(x_coords, y_coords):
    """
    A function that takes in lists of corresponding x and y coordinates and creates a polygon.
    
    Parameters
    ----------------------------------------------------
    x_coords: list of x-coordinate float values
    y_coords: list of y-coordinate float values
    
    Returns
    ----------------------------------------------------
    A polygon
    """
    
    try:
        coordpairs = [(x, y) for x in x_coords for y in y_coords]            
        return Polygon(coordpairs)
    
    except Exception as e:
        return logging.exception(e)


def insert_geomtogdf(geom):
    """
    A function that takes in a geometry and inserts it to a new GeoDataFrame.
    
    Parameters
    ----------------------------------------------------
    geom: any shapely geometry
    
    Returns
    ----------------------------------------------------
    A GeoDataFrame with the geometry data
    """
    
    try:
        df = gpd.GeoDataFrame()   
        df['geometry'] = None
        df.loc['geometry'] = geom
        return df
    
    except Exception as e:
        return logging.exception(e)


def get_m_dist_latlong(lat1, long1, lat2, long2, ellps="WGS84"):
    """
    A function that takes in two pairs of latitude and longitude values and gets their distance in meters.
    
    Parameters
    ----------------------------------------------------
    lat1: float latitude coordinate of first point
    long1: float longitude coordinate of first point
    lat2: float latitude coordinate of second point
    long2: float longitude coordinate of second point
    
    Returns
    ----------------------------------------------------
    Distance between two points in meters.
    """
    
    try:
        geod = pyproj.Geod(ellps=ellps)
        angle1,angle2,distance = geod.inv(long1, lat1, long2, lat2)
        return distance      
    
    except Exception as e:
        return logging.exception(e)
    
