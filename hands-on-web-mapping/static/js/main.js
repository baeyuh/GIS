$(document).ready(function() {

var map = L.map('map', {
    center: [12.8797, 121.7740],
    zoom: 6,
});

var osm_mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

})
