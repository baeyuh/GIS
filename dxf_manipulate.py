import geopandas as gpd

#open the DXF file
dxf_file = gpd.read_file('../folder/drawing.dxf')
#dxf_file.plot()

#scale the DXF to spatial extent 
#scale parameters (x, y, z, origin=(_))
#scale params are equal to drawing scale divided by measured extents in QGIS
geometryScaled = dxf_file.scale(x,y,1,origin=(0,0,0))
#geometryScaled.plot()

#translate the geometry to PRS92 ZONE_
#translate parameters (x-offset, y-offset, z-offset) 
#georeference and use QGIS coordinates found at the bottom of the map view
geometryTranslated = geometryScaled.translate(x-coord,y=coord,0)
#geometryTranslated.plot()

#apply the new geometry to the geopandas dataframe and apply the EPSG code
#link to PRS92 EPSG codes: https://spatialreference.org/ref/?search=prs92
dxf_file = gpd.GeoDataFrame(dxf_file, geometry=geometryTranslated)
dxf_file.crs = {'init':'epsg:code'}
#dxf_file.plot()

#export the spatial as shapefile
dxf_file.to_file('../folder/Dxf_Total.shp')

