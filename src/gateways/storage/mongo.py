
from typing import Iterable
from src.entities.person import Person
from src.usecases.interfaces import IStorage



class Mongo(IStorage):
    def get_persons_all(self) -> Iterable[Person]:
        query = """
            main.public.persons{}
        """
        rows: list[dict] = self.execute(query)
        
