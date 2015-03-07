console.log("Boot Anti Rape");

var noble = require('noble');

console.log("Noble included");

noble.on('discover', function(peripheral) {
  peripheral.connect(function(error) {
    console.log('connected to peripheral: ' + peripheral.uuid);
  });
});

console.log("End Anti Rape");