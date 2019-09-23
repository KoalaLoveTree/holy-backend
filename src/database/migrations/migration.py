from abc import ABC, abstractmethod


class AbstractMigration(ABC):
    @abstractmethod
    def up(self, db_engine):
        pass

    @abstractmethod
    def down(self, db_engine):
        pass

    def __get_table(self):
        pass
