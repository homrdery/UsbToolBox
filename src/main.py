#!/bin/python

try:
    from Parser import Parser
    from device import Device

    parser = Parser()
    parser.parse_args()
    import usb
    import os
    import sig
    print("pid",os.getpid())
except Exception as e:
    print(f"Unable load modules: {e}")
    quit(5)


try:
    if parser.options.search:
        for device in Device.get_new_devices():
            print(device.info)
            print(device)
except Exception as e:
    print(f"Error: {e}")
    quit(5)
except KeyboardInterrupt as e:
    print("KeyboardInterrupt")
    quit(5)

