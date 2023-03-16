from typing import Optional
from aiohttp.web import (
    Application as AiohttpApplication,
    View as AiohttpView,
    Request as AiohttpRequest,
    run_app as aiohttp_run_app
)
from aiohttp_apispec import setup_aiohttp_apispec
from app.config import Config, setup_config
from app.routes import setup_routes
from app.middlewares import setup_middlewares
from app.accessor import CrmAccessor, setup_accessors


class Application(AiohttpApplication):
    config: Optional[Config] = None
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_config(app)
    setup_routes(app)
    setup_aiohttp_apispec(app, title='CRM Application',
                          url='/docs/json',
                          swagger_path='/docs')
    setup_middlewares(app)
    setup_accessors(app)
    aiohttp_run_app(app)
