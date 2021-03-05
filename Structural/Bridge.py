from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self, percent):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass


def volume_wrapper(func):
    def magic(self):
        print(f'volume now on {self.device_name}: {self.device.get_volume()}')
        func(self)
        print(f'volume now on {self.device_name}: {self.device.get_volume()}')

    return magic


class RemoteControl:
    device: Device

    def __init__(self, device: Device):
        self.device = device
        self.device_name = device.__class__.__name__

    def toggle_power(self):
        if self.device.is_enabled():
            print(f"disabling {self.device_name}")
            self.device.disable()
        else:
            print(f"enabling {self.device_name}")
            self.device.enable()

    @volume_wrapper
    def volume_down(self):
        print(f'decreasing volume of {self.device_name}')
        self.device.set_volume(self.device.get_volume() - 10)

    @volume_wrapper
    def volume_up(self):
        print(f'increasing volume of {self.device_name}')
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        print(f'switching to 1 channel back on {self.device_name}')
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        print(f'switching to 1 channel forward on {self.device_name}')
        self.device.set_channel(self.device.get_channel() + 1)


class Radio(Device):
    enabled = False
    volume = 20
    max_volume = 50
    min_volume = 0
    channel = 1
    min_channel = 1
    max_channel = 12

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        if percent > self.max_volume:
            self.volume = self.max_volume
        elif percent < self.min_volume:
            self.volume = self.min_volume
        else:
            self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if channel > self.max_channel:
            self.channel = self.min_channel
        elif channel < self.min_channel:
            self.channel = self.max_channel
        else:
            self.channel = channel


class TV(Device):
    enabled = False
    volume = 20
    max_volume = 100
    min_volume = 0
    channel = 1
    min_channel = 1
    max_channel = 100

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        if percent > self.max_volume:
            self.volume = self.max_volume
        elif percent < self.min_volume:
            self.volume = self.min_volume
        else:
            self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if channel > self.max_channel:
            self.channel = self.min_channel
        elif channel < self.min_channel:
            self.channel = self.max_channel
        else:
            self.channel = channel


if __name__ == '__main__':
    tv = TV()
    radio = Radio()
    tv_remote = RemoteControl(tv)
    radio_remote = RemoteControl(radio)
    tv_remote.volume_down()
    tv_remote.volume_down()
    tv_remote.volume_down()
    tv_remote.volume_up()
