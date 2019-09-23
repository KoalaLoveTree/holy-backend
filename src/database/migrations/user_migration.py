from .migration import AbstractMigration
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)


class UserMigration(AbstractMigration):
    meta = MetaData()

    def up(self, db_engine):
        self.meta.create_all(bind=db_engine, tables=[self.__get_table()])

    def down(self, db_engine):
        self.meta.drop_all(bind=db_engine, tables=[self.__get_table()])

    def __get_table(self):
        return Table(
            'users', self.meta,

            Column('id', Integer, primary_key=True),
            Column('username', String(200), nullable=False),
            Column('password', String(200), nullable=False),
            Column('role', String(200), nullable=False),
            Column('created_at', Date, nullable=False),
            Column('updated_at', Date, nullable=False),
        )
