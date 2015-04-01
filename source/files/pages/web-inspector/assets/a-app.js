var USGS_API_JSON_ENDPOINT = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson',
    GMAPS_ENDPOINT = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'

function get_earthquake_data(){
  console.info("get data");
  $.get(USGS_API_JSON_ENDPOINT, function(data){
    var mapmarks = GMAPS_ENDPOINT,
        tstr = "<thead><tr><th>Place</th><th>Time</th><th>Magnitude</th></tr></thead><tbody>"

    data.features.forEach(function(f){
      var p = f.properties, geo = f.geometry.coordinates
      tstr += "<tr>"
      tstr += "<td class='place'>" + p.place + "</td>"
      var dt = new Date(p.time);
      tstr += "<td class='time'>" + [ dt.getMonth() + 1, dt.getDate(), dt.getFullYear() ].join('/') + '&nbsp;' +
        [dt.getHours(), dt.getMinutes()].join(':') +
        "</td>"

      tstr += "<td class='mag'>" + p.mag + "</td>"
      tstr += "</tr>"
      mapmarks += '&markers=size:tiny%7C' + geo[1] + ',' + geo[0]
    });

    tstr += "</tbody>";
    $('#earthquakes').html(tstr);
    $('#earthquakes-map').attr('src', mapmarks)
  });

  just_shake();
}

// http://stackoverflow.com/questions/4399005/implementing-jquerys-shake-effect-with-animate
function just_shake(){
  console.info("gonna shake!")
  var $sel = $("#the-container");
  $sel.css("position","relative");
  var s = 15, d = 20, t = 3;
  for (var x=1; x<=s; x++) {
        $sel.animate({left:(d*-1)}, (((d/s)/4)))
          .animate({left:d}, ((t/s)/2))
          .animate({left:0}, (((t/s)/4)));
  }

  return $sel;
}

function just_swift(){
  $("#the-container").children().fadeOut(300, function(){
    $('#the-container').html('<iframe id="swift-video" width="560" height="315" src="https://www.youtube.com/embed/nfWlot6h_JM?start=4&autoplay=1" frameborder="0" allowfullscreen></iframe>')


    console.info("Resizing video!");
    $('#swift-video').css({ width: $(window).innerWidth() + 'px', height: $(window).innerHeight() + 'px' });

    // If you want to keep full screen on window resize
    $(window).resize(function(){
        $('#swift-video').css({ width: $(window).innerWidth() + 'px', height: $(window).innerHeight() + 'px' });
    });


  })

}



$(document).ready(function(){
  $("button#refresh-quake-data").click(function(){
    get_earthquake_data();
  })

  $("button#refresh-swift").click(function(){
    just_shake();
    just_swift();

  })



  console.info("hi there");
})

