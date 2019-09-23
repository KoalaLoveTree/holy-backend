from aiohttp import web
from dotenv import load_dotenv
import config
import aiopg.sa


class Bootstrapper:
    def create_application(self):
        app = web.Application()

        load_dotenv()
        app['db_engine'] = self.__create_engine()

        return app

    def __create_engine(self):
        conf = config.CONNECTION

        engine = aiopg.sa.create_engine(
            database=conf['database'],
            user=conf['user'],
            password=conf['password'],
            host=conf['host'],
            port=conf['port'],
        )

        return engine
