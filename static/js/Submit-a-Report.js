// https://stackoverflow.com/questions/50213683/capture-image-from-a-webcam-and-upload-it-to-flask-server
//navigator.geolocation.getCurrentPosition(function(position) {
//function showPosition(position) {
//  document.getElementById("location").value = "Latitude: " + position.coords.latitude +
//  "<br>Longitude: " + position.coords.longitude;}
//});
//if (navigator.geolocation) {
//function getlocation() {
//      navigator.geolocation.getCurrentPosition(showLoc);
//    }
//    function showLoc(pos) {
//      document.getElementById("latitude").value =
//       "Latitude: " +
//        pos.coords.latitude +
//        "<br>Longitude: " +
//        pos.coords.longitude;
//    }
//    }

//navigator.geolocation.getCurrentPosition((position) => {
//  loc(position.coords.latitude, position.coords.longitude);
//});



if (navigator.geolocation) {
var geolocation = {};
geolocation.latitude = 0;
geolocation.longitude = 0;
navigator.geolocation.getCurrentPosition(function (p) {
geolocation.latitude = p.coords.latitude;
geolocation.longitude = p.coords.longitude;
document.getElementById("longitude").value = geolocation.latitude;
document.getElementById("latitude").value = geolocation.longitude;
}, function (error) {
alert("Failed to get GPS location");
});
} else {
alert("Failed to get GPS working");
};

//function loc() {
//document.getElementById("longitude").value = geolocation.latitude;
//document.getElementById("latitude").value = geolocation.longitude;
//};
//loc()


if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
    // ok, browser supports it
// Set constraints for the video stream
var constraints = { video: { facingMode: "default" }, audio: false };

// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
    cameraTrigger = document.querySelector("#camera--trigger")

// Access the device camera and stream to cameraView
function cameraStart()
{
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function()
{
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL("image/webp");
    cameraOutput.classList.add("taken");
};

// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
};
