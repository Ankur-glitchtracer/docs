from abc import ABC, abstractmethod


# class Video(ABC):
#     @abstractmethod
#     def __init__(self) -> None:
#         pass


# class RealVideo(Video):
#     def __init__(self) -> None:
#         print("Loading video from disk...")


# class ProxyVideo:
#     def display(self) -> Video:
#         return RealVideo()

# my_proxy = ProxyVideo()

# my_proxy.display()

class Video(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class RealVideo(Video):
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self._load_on_disk()
    
    def _load_on_disk(self) -> None:
        print("Heavy Operation")
    
    def display(self) -> None:
        print(f"Displaying {self.filename}")


class ProxyVideo(Video):
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self._real_video: RealVideo | None = None
    
    def display(self) -> None:
        if self._real_video is None:
            self._real_video = RealVideo(self.filename)
        
        self._real_video.display()

# Test
proxy = ProxyVideo("Inception.mp4") # Nothing happens here
print("Proxy created...")
proxy.display() # Loading happens now
proxy.display() # Second time, it's already loaded!
