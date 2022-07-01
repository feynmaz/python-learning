from abc import ABC, abstractmethod
from typing import Iterable

from src.entities.person import Person


class IStorage(ABC):
    @abstractmethod
    def get_persons_all(self) -> Iterable[Person]:
        ...
