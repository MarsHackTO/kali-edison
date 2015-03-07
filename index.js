console.log("Boot Anti Rape");

noble.on('discover', function(peripheral) {
  peripheral.connect(function(error) {
    console.log('connected to peripheral: ' + peripheral.uuid);
  });
});

console.log("End Anti Rape");