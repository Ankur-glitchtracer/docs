from abc import ABC, abstractmethod


class Light:
    def __init__(self) -> None:
        self.intensity: int = 0
    def on(self) -> None:
        self.intensity = 100
        print("Light is ON")

    def off(self) -> None:
        self.intensity = 0
        print("Light is OFF")

    def set_intensity(self, intensity: int) -> None:
        self.intensity = intensity
        print(f"Light is set to the intensity: {intensity}")


class Stereo:
    def __init__(self) -> None:
        self.volume: int = 0
        self.hasCD: bool = False

    def increaseVolume(self) -> None:
        volume = self.volume + 1
        self.volume = volume
        print(f"Volume has been increased to {volume}")

    def setVolume(self, volume: int) -> None:
        self.volume = volume
        print(f"Volume has been set to {volume}")

    def getVolume(self) -> int:
        return self.volume

    def insertCD(self) -> None:
        self.hasCD = True
        print("CD has been inserted")

    def ejectCD(self) -> None:
        self.hasCD = False
        print("CD has been ejected")

    def playCD(self) -> None:
        if self.hasCD:
            print("Playing the CD!!")
        else:
            print("Please insert CD to play")

    def mute(self) -> None:
        self.volume = 0
        print("TV has been muted")


class Garage:
    def __init__(self) -> None:
        self.state: bool = False

    def open(self) -> None:
        if self.state:
            print("The Garage is already Opened")
        else:
            self.state = True
            print("Opening the Garage")

    def close(self) -> None:
        if self.state:
            self.state = False
            print("Closing the Garage")
        else:
            print("The Garage is already Closed")

    def toggle(self) -> None:
        if self.state:
            self.state = False
            print("Closing the Garage")
        else:
            self.state = True
            print("Opening the Garage")


class Thermostat:
    def __init__(self) -> None:
        self.temp: int = 74

    def set_temp(self, temp: int) -> None:
        self.temp = temp
        print(f"Thermostat has been set to temperature: {temp}°F")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light
        self.prev_state: Light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        light: Light = self.light
        self.light = self.prev_state
        self.prev_state = light


class LightDimCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light
        self.prev_state: Light = light

    def execute(self) -> None:
        self.light.set_intensity(intensity=30)

    def undo(self) -> None:
        light: Light = self.light
        self.light = self.prev_state
        self.prev_state = light


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light: Light = light
        self.prev_state: Light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        light: Light = self.light
        self.light = self.prev_state
        self.prev_state = light


class StereoIncreaseVolumeCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo
        self.prev_state: Stereo = stereo

    def execute(self) -> None:
        self.stereo.increaseVolume()

    def undo(self) -> None:
        stereo: Stereo = self.stereo
        self.stereo = self.prev_state
        self.prev_state = stereo


class StereoMuteCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self.stereo: Stereo = stereo
        self.prev_state: Stereo = stereo

    def execute(self) -> None:
        self.stereo.setVolume(volume=0)

    def undo(self) -> None:
        stereo: Stereo = self.stereo
        self.stereo = self.prev_state
        self.prev_state = stereo



class GarageOpenCommand(Command):
    def __init__(self, garage: Garage) -> None:
        self.garage: Garage = garage
        self.prev_state: Garage = garage

    def execute(self) -> None:
        self.garage.open()

    def undo(self) -> None:
        self.garage.toggle()


class PartyCommand(Command):
    def __init__(self, thermostat: Thermostat, light: Light, stereo: Stereo) -> None:
        self.thermostat: Thermostat = thermostat
        self.prev_thermo: Thermostat = thermostat
        self.light: Light = light
        self.prev_light: Light = light
        self.stereo: Stereo = stereo
        self.prev_stereo: Stereo = stereo

    def execute(self) -> None:
        self.thermostat.set_temp(temp=72)
        self.light.set_intensity(intensity=30)
        self.stereo.playCD()

    def undo(self) -> None:
        thermostat: Thermostat = self.thermostat
        self.thermostat = self.prev_thermo
        self.prev_thermo = thermostat

        light: Light = self.light
        self.light = self.prev_light
        self.prev_light = light

        stereo: Stereo = self.stereo
        self.stereo = self.prev_stereo
        self.prev_stereo = stereo


class Remote:
    def __init__(self, button_1: Command, button_2: Command, button_3: Command, button_4: Command, party: Command) -> None:
        self.button_1: Command = button_1
        self.button_2: Command = button_2
        self.button_3: Command = button_3
        self.button_4: Command = button_3
        self.party: Command = party
        self.undo: Command | None = None

    def firstButton(self) -> None:
        self.undo = self.button_1
        self.button_1.execute()

    def secondButton(self) -> None:
        self.undo = self.button_2
        self.button_2.execute()

    def thirdButton(self) -> None:
        self.undo = self.button_3
        self.button_3.execute()

    def fourthButton(self) -> None:
        self.undo = self.button_4
        self.button_4.execute()

    def partyButton(self) -> None:
        self.undo = self.party
        self.party.execute()

    def undoButton(self) -> None:
        if self.undo:
            self.undo.undo()

my_thermo = Thermostat()
my_light = Light()
my_stereo = Stereo()
my_garage = Garage()

light_on_command = LightOnCommand(light=my_light)
light_dim_command = LightDimCommand(light=my_light)
open_garage_command = GarageOpenCommand(garage=my_garage)
mute_command = StereoMuteCommand(stereo=my_stereo)
party_command = PartyCommand(thermostat=my_thermo, light=my_light, stereo=my_stereo)

my_remote = Remote(button_1=light_on_command, button_2=light_dim_command, button_3=open_garage_command, button_4=mute_command, party=party_command)

my_remote.firstButton()
my_remote.fourthButton()
my_remote.undoButton()

