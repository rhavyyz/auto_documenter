from abc import ABC
from abc import abstractmethod
from src.file_walker.types.content import Content

class BaseRenderer(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add_content(self, content : Content) -> None:
        pass

    @abstractmethod
    def construct(self, path : str) -> str:
        pass