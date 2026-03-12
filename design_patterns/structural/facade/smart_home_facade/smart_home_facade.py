class Projector:
    def __init__(self) -> None:
        self.input : str = "Netflix"

    def set_input(self, input: str) -> None:
        self.input = input

    def on(self) -> None:
        print(f"Starting the Projector for {self.input}")

    def off(self) -> None:
        print(f"Shutting the Projector for {self.input}")


class SoundSystem:
    def __init__(self) -> None:
        self.volume: int = 10
    
    def set_volume(self, volume: int) -> None:
        self.volume = volume

    def on(self) -> None:
        print(f"Starting the SoundSystem with volume level {self.volume}")

    def off(self) -> None:
        print(f"Shutting the SoundSystem with volume level {self.volume}")


class Lights:
    def __init__(self) -> None:
        self.intensity : float = 50.0
        self._default : float = 50.0
    
    def dim(self, intensity: float) -> None:
        self.intensity = intensity
        print(f"Lights have been dim to {intensity}")
    
    def reset(self) -> None:
        self.intensity = self._default
        print(f"Lights have been reset to {self.intensity}")


class HomeThreaterFacade:
    def __init__(self, projector: Projector, soundsystem: SoundSystem, lights: Lights) -> None:
        self.projector : Projector = projector
        self._input : str = "Netflix"
        self.soundsystem : SoundSystem = soundsystem
        self._volume : int = 20
        self.lights : Lights = lights
        self._dim : float = 18.5

    def watch_movie(self, movie_name: str) -> None:
        print(f"Starting Home Threater to watch {movie_name}")

        self.projector.set_input(self._input)
        self.projector.on()

        self.soundsystem.set_volume(self._volume)
        self.soundsystem.on()

        self.lights.dim(self._dim)

    def end_movie(self) -> None:
        print("Shutting down the Home Threater")
        self.projector.off()
        self.soundsystem.off()
        self.lights.reset()

my_projector = Projector()
my_soundsystem = SoundSystem()
smart_lights = Lights()

my_homethreater = HomeThreaterFacade(my_projector, my_soundsystem, smart_lights)

my_homethreater.watch_movie("Movie")

my_homethreater.end_movie()

