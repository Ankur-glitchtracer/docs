class Device:
    def __init__(self) -> None:
        self.volume : int = 10
        self.status : bool = False

    def is_enabled(self) -> bool:
        return self.status

    def enable(self) -> None:
        self.status = True

    def disable(self) -> None:
        self.status = False

    def set_volume(self, volume: int) -> None:
        self.volume = volume
        print(f"The Volume is set to {self.volume}")

    def get_volume(self) -> int:
        return self.volume


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device : Device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            print("The Power was ON. Toggling it!")
            self.device.disable()
        else:
            print("The Power was OFF. Togging it!")
            self.device.enable()

    def volume_up(self) -> None:
        current = self.device.get_volume()
        self.device.set_volume(current + 1)


class AdvanceRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print("The Volume is now Mute")


my_device = Device()

my_remote = AdvanceRemoteControl(my_device)

my_remote.toggle_power()

my_remote.volume_up()
my_remote.volume_up()
my_remote.volume_up()

my_remote.mute()

my_remote.volume_up()
my_remote.volume_up()

