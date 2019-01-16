# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:44:19 2019

@author: Subea
"""

import osgeo.ogr


def shp_analysis(fpath, fieldname):    
    """
    A function that takes in a shapefile and analyze its basic properties - no. of layers, spatial reference, no. of features and field attribute.
    
    Parameters
    ----------------------------------------------------
    fpath : filepath in string format of shapefile, use double backslashes (\\) for directory separator
    fieldname : string format of column/field name of attribute to be checked
    
    Returns
    ----------------------------------------------------
    No. of layers, spatial reference, no. of features and field attribute of each feature
    """

    shapefile = osgeo.ogr.Open(fpath)
    numLayers = shapefile.GetLayerCount()
    print("Shapefile contains {} layers".format(numLayers))
    print()
    for layerNum in range(numLayers):
        layer = shapefile.GetLayer(layerNum)
        spatialRef = layer.GetSpatialRef().ExportToProj4()
        numFeatures = layer.GetFeatureCount()
        print("Layer {} has spatial reference {}".format(layerNum, spatialRef))
        print("Layer {} has {} features:".format(layerNum, numFeatures))
        print()
        for featureNum in range(numFeatures):
            feature = layer.GetFeature(featureNum)
            featureAttr = feature.GetField(fieldname)
            print("Feature {} : {}".format(featureNum, featureAttr))
            
            
