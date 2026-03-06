from abc import ABC, abstractmethod


class Computer:
    def __init__(self) -> None:
        self.cpu : str | None = None
        self.memory : str | None = None
        self.gpu : str | None = None
        self.psu : str | None = None


class Builder(ABC):
    def __init__(self):
        self.computer : Computer = Computer()

    @abstractmethod
    def add_cpu(self, cpu: str) -> Builder:
        pass

    @abstractmethod
    def add_memory(self, memory: str) -> Builder:
        pass

    @abstractmethod
    def add_gpu(self, gpu: str) -> Builder:
        pass

    @abstractmethod
    def add_psu(self, psu: str) -> Builder:
        pass

    @abstractmethod
    def build(self) -> Computer:
        pass


class GamingPCMenu(Builder):
    def add_cpu(self, cpu: str) -> Builder:
        self.computer.cpu = cpu
        return self

    def add_memory(self, memory: str) -> Builder:
        self.computer.memory = memory
        return self

    def add_gpu(self, gpu: str) -> Builder:
        self.computer.gpu = gpu
        return self

    def add_psu(self, psu: str) -> Builder:
        self.computer.psu = psu
        return self

    def build(self) -> Computer:
        print(f"Gaming PC has cpu: {self.computer.cpu}, memory: {self.computer.memory}, gpu: {self.computer.gpu}, psu: {self.computer.psu}")
        computer = self.computer
        self.computer = Computer()
        return computer

# Goal usage:
my_builder = GamingPCMenu()
pc = my_builder.add_cpu("Intel i9").add_gpu("RTX 4090").build()

