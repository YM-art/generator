import time
from pathlib import Path
import configparser


def get_ini_config_object(config_ini_path: Path):
    config = configparser.ConfigParser()
    config.read(config_ini_path, encoding="utf-8")
    return config


config_path = Path.cwd() / "config-sample.ini"
config_object = get_ini_config_object(config_path)

Editions = {
        "start_time_str": str,
        "end_time_str": str,

        "root_dir": Path(config_object["package"]["root_dir"]),
        "SHORT_ARCH": config_object["package"]["SHORT_ARCH"],
        "version": config_object["package"]["version"],
        "build": time.strftime("%Y.%m.%d.%H%M")
        }
