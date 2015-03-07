console.log("Boot Anti Rape");

var noble = require('noble');

noble.on('discover', function(peripheral) {
  peripheral.connect(function(error) {
    console.log('connected to peripheral: ' + peripheral.uuid);
  });
});

console.log("End Anti Rape");