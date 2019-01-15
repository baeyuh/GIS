# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:41:18 2019

@author: Subea
"""

from shapely.geometry import Point, LineString, Polygon
import geopandas as gpd
import logging


def create_point_geom(x_coord, y_coord):
    
    try:
        return Point(x_coord, y_coord)
    
    except Exception as e:
        return logging.exception(e)
    

def create_line_geom(point_geoms):

    line_geoms = LineString(point_geoms)

    try:
        return line_geoms
    
    except Exception as e:
        return logging.exception(e)


def create_poly_geom(geoms):
    
    try:
        if geoms[0].geom_type == 'Point':
            return Polygon([[p.x, p.y] for p in geoms])
        else:
            return Polygon(geoms)

    except Exception as e:
        return logging.exception(e)


def get_centroid(geoms):
    
    try:
        return [g.centroid for g in geoms]
    
    except Exception as e:
        return logging.exception(e)
    

def get_rep_point(geoms):
    
    try:
        return [g.representative_point() for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def get_area(geoms):
    
    try:
        return [g.area for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def get_length(geoms):
    
    try:
        return [g.length for g in geoms]
    
    except Exception as e:
        return logging.exception(e)


def create_polygon(x_coords, y_coords):
    
    try:
        coordpairs = [(x, y) for x in x_coords for y in y_coords]            
        return Polygon(coordpairs)
    
    except Exception as e:
        return logging.exception(e)


def insert_geomtogdf(geom):
    
    try:
        df = gpd.GeoDataFrame()   
        df['geometry'] = None
        df.loc['geometry'] = geom
        return df
    
    except Exception as e:
        return logging.exception(e)


