import usb
import time


class Device:
    def __init__(self, device: usb.core.Device):
        """
        :param device:usb девайс который подключен к пк
        """
        self.device = device

    @staticmethod
    def get_devices():
        """
        :return:возрат количество подключённых usb девайсов и список этих девайсов
        """
        devices = []
        for dev in usb.core.find(find_all=True):
            # info = dev.get_info(dev)
            devices.append(dev)
        count = len(devices)
        return count, devices

    def usb_get_string(self, code):
        """
        :param code:
        :return:
        """
        try:
            value = usb.util.get_string(self.device, code)
        except Exception as e:
            value = str(e)

    @property
    def Product(self):
        """
        :return:
        """
        key = self.device.bDeviceClass
        table = usb._lookup.device_classes
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
        """
        :return: возращает проинформированнный список девайсов
        """
        retval = {}
        for key in "idVendor", "idProduct", "bDeviceClass", "iProduct", "speed", "bus", "port_number", "address":
            try:
                retval[key] = getattr(self.device, key)
            except Exception as e:
                print(e)
        retval["Product"] = self.Product
        return retval
    @staticmethod
    def get_new_devices():
        """
        :return:возращает информацию о новом устройстве
        """
        result = []
        count, devices = Device.get_devices()
        while True:
            tmp_count, tmp_devices = Device.get_devices()
            if tmp_count > count:
                break
            else:
                count, devices = tmp_count, tmp_devices
            time.sleep(2)
            print(tmp_count)

        for dev in tmp_devices:
            if dev not in devices:
                result.append(Device(dev))

        return result
    def __str__(self):
        info = self.info
        return f"""
        {hex(info["idVendor"])}:{hex(info["idProduct"])}
        """
