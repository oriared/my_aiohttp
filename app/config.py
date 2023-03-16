import typing
import yaml
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from app import Application


@dataclass
class Config:
    username: str
    password: str


def setup_config(app: 'Application'):
    with open('config/config.yaml') as f:
        raw_config = yaml.safe_load(f)
    app.config = Config(
        username=raw_config['credentials']['username'],
        password=raw_config['credentials']['password']
    )
