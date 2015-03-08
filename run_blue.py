# file: inquiry.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: performs a simple device inquiry followed by a remote name request of
#       each discovered device
# $Id: inquiry.py 401 2006-05-05 19:07:48Z albert $
#

import bluetooth

print("finding nearby devices")
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))


print ("bluetooth.BluetoothSocket()")
ble = bluetooth.BluetoothSocket()

print("ble.getsockname()")
print ble.getsockname()

print("blue.fileno()")
print ble.fileno()

#print("ble.bind((\"C0:EE:FB:28:59:87\"))")
#ble.bind(("C0:EE:FB:28:59:87", 0))

print("ble.connect((\"C0:EE:FB:28:59:87\"))")
ble.connect(("C0:EE:FB:28:59:87", 0))

print("ble.send()")
ble.send("test_send_ble")

print("end run_blue.py")
ble.close()
