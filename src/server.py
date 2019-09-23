from aiohttp import web
from bootstrap import Bootstrapper


bootstrapper = Bootstrapper()

web.run_app(bootstrapper.create_application())
