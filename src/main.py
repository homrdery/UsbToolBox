#!/bin/python
import sys
import time
import Parser
parser=Parser()
try:
    import usb
    from usb import _lookup as _lu
except Exception as e:
    print(f"Unable load modules: {e}")
    quit(5)


def usb_get_string(device, code):
    try:
        value = usb.util.get_string(device, code)
    except Exception as e:
        value = str(e)


class Device:
    def __init__(self, device: usb.core.Device):
        self.device = device

    @property
    def Product(self):
        key = self.device.bDeviceClass
        table = _lu.device_classes
        default = "---"
        try:
            value = usb.util.get_string(self.device, self.device.iProduct)
        except ValueError:
            value = table[key]
        if value is None:
            value = default
        return value

    @property
    def info(self):
        retval = {}
        for key in "idVendor", "idProduct", "bDeviceClass", "iProduct", "speed", "bus", "port_number", "address":
            try:
                retval[key] = getattr(self.device, key)
            except Exception as e:
                print(e)
        retval["Product"] = self.Product
        return retval

    def __str__(self):
        info = self.info
        return  f"""
        {hex(info["idVendor"])}:{hex(info["idProduct"])}
        """

def prosmotr():
    devices = []
    for dev in usb.core.find(find_all=True):
        # info = dev.get_info(dev)
        devices.append(dev)
    count = len(devices)
    print (count)
    while True:

        tmp_count = 0
        tmp_devices = []
        for dev in usb.core.find(find_all=True):
            tmp_count+=1
            tmp_devices.append(dev)
        if tmp_count > count:
            break
        time.sleep(2)
        print (tmp_count)

    for dev in tmp_devices:
        if dev not in devices:
            device = Device(dev)
            print (device.info)
            print (device)
if parser.options.search():
    prosmotr()




