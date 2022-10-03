import sqlite3
from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

Cursor = TypeVar("Cursor")


class Driver(Generic[Cursor], metaclass=ABCMeta):
    @abstractmethod
    def execute(self, query: str) -> Cursor:
        pass


class SqliteDriver(Driver[sqlite3.Cursor]):
    def __init__(self, database: str | bytes):
        self.connection = sqlite3.connect(database)

    def execute(self, query: str):
        return self.connection.execute(query)
