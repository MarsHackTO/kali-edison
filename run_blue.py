# file: inquiry.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: performs a simple device inquiry followed by a remote name request of
#       each discovered device
# $Id: inquiry.py 401 2006-05-05 19:07:48Z albert $
#

import bluetooth

# set socket
print ("bluetooth.BluetoothSocket()")
ble = bluetooth.BluetoothSocket()
# listen god damnit
ble.listen(10)

# advertise
print ("advertise_service()")
bluetooth.advertise_service(ble, "EdisonKali")

# find service
print("finding nearby devices")
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

# debug
print("ble.getsockname()")
print ble.getsockname()

print("blue.fileno()")
print ble.fileno()

print("find_service()")
bluetooth.find_service("OnePlus One")
print find_service("OnePlus One")

#print("ble.bind((\"C0:EE:FB:28:59:87\"))")
#ble.bind(("C0:EE:FB:28:59:87", 0))

print("ble.connect")
ble.connect(("C0:EE:FB:28:59:87", 0))

print("ble.send")
ble.send("test_send_ble")

print("end run_blue.py")
ble.close()
