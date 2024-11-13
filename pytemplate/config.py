import logging

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.FileHandler("pytemplate.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class EnvFileLoader(BaseSettings):
    """
    Configuration class that inherits from BaseSettings.
    Designed only as a LOADER for a .env file. Not to store the values.
    This way, we can have multiple configuration classes that STORE different environment variables.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Config(EnvFileLoader):
    DUMMY_STR: str


config = Config()
