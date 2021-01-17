import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import {Tile as TileLayer, Image as ImageLayer} from 'ol/layer';
import {OSM, ImageArcGISRest} from 'ol/source';

var url = 'https://sampleserver1.arcgisonline.com/ArcGIS/rest/services/' +
    'Specialty/ESRI_StateCityHighway_USA/MapServer';

var layers = [
    new ol.layer.Tile({
        source: new ol.source.OSM()
    }),
    new ol.ol.layer.Image({
        source: new ol.source.ImageArcGISRest({
            ratio: 1,
            params: {},
            url: url
        })
    })
];
var map = new ol.Map({
    layers: layers,
    target: 'map',
    view: new ol.View({
        center: [-10997148, 4569099],
        zoom: 4
    })
});
