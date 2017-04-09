
function setupReader(file) {
    var name = file.name;
    var reader = new FileReader();  
    reader.onload = function() {  
        var parsed = new DOMParser().parseFromString(this.result, "text/xml");

        var l = omnivore.gpx.parse(parsed)
        l.setStyle({color : getSelectedColour(),
                    opacity: 0.5});
        l.addTo(map);
    }
    reader.readAsText(file);
}

function getSelectedColour() {
    return $('#colourPicker').val();
}

function addToMap(){
    var files = document.getElementById('myFile').files;

    for (var i = 0; i < files.length; i++) {
        setupReader(files[i]);
    }
}

function toggleElement(nav) {
    var x = document.getElementById(nav);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}
