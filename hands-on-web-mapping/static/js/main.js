$(document).ready(function() {

var osm_mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
})

var open_topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});

var flood = new L.GeoJSON.AJAX("data/flood.geojson", {
    style: function(feature) {
        switch (feature.properties.FloodSusc) {
            case 'HF':   return {color: "#0000fe", fillOpacity: 0.7, weight: 1};
            case 'LF':   return {color: "#75cff0", fillOpacity: 0.7, weight: 1};
            case 'MF':   return {color: "#c896ff", fillOpacity: 0.7, weight: 1};
            case 'VHF':  return {color: "#00064d", fillOpacity: 0.7, weight: 1};
        }
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup('<b>Flood Susceptibility:</b> ' +feature.properties.FloodSusc);
    }
});

var storm_surge = new L.GeoJSON.AJAX("data/storm-surge.geojson", {
    style: function(feature) {
       switch (feature.properties.HAZ) {
           case 3:   return {color: "#e31a1c", fillOpacity: 0.7, weight: 1};
           case 2:   return {color: "#ff7f00", fillOpacity: 0.7, weight: 1};
           case 1:   return {color: "#effb08", fillOpacity: 0.7, weight: 1};
           default:  return {color: "#cf4320", fillOpacity: 0.7, weight: 1};
       }
   },
   onEachFeature: function (feature, layer) {
       layer.bindPopup('<b>Storm-Surge Susceptibility:</b> ' +feature.properties.HAZ);
   }
});

var basemaps = {
    "OSM Mapnik": osm_mapnik,
    "OpenTopoMap": open_topo,

}

var overlays = {
    "Flood": flood,
    "Storm Surge": storm_surge,
}

var map = L.map('map', {
    center: [9.830, 118.745],
    zoom: 10,
    layers: [osm_mapnik, flood]
});

L.control.layers(basemaps, overlays).addTo(map);



map.invalidateSize();
})
