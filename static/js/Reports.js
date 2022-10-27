//https://stackoverflow.com/questions/41161889/display-multiple-markers-on-google-map-from-data-in-html-table-using-javascript

var table = $("table tbody");

var tableLocs = [];
table.find('tr').each(function(i) {
var $tds = $(this).find('td'),
siteName = $tds.eq(0).text(),
Lat = $tds.eq(2.split(", ")[0]).text();
Lon = $tds.eq(2.split(", ")[0]).text();
var obj = {'sitename': siteName,'lat': Lat,'lon': Lon}

var marker = new google.maps.Marker({position: myCenter});
marker.setMap(map);

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}

window.initMap = initMap;