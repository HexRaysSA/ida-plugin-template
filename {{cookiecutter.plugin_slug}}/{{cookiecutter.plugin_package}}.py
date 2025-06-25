from {{cookiecutter.plugin_package}}.utils import my_util
import logging
import ida_idaapi

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("{{cookiecutter.plugin_package}}")

class {{cookiecutter.plugin_class}}(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_FIX

    # Required attributes - must be set by subclasses
    wanted_name: str = "{{cookiecutter.plugin_name}}"
    comment: str = "{{cookiecutter.plugin_name}}"
    help: str = "{{cookiecutter.plugin_name}}"

    def init(self) -> int:
        logger.info("Plugin {{cookiecutter.plugin_name}} initializing")
        return ida_idaapi.PLUGIN_KEEP

    def run(self, arg: int) -> None:
        logger.info("Plugin {{cookiecutter.plugin_name}} running")

    def term(self) -> None:
        logger.info("Plugin {{cookiecutter.plugin_name}} terminating")

def PLUGIN_ENTRY():
    return {{cookiecutter.plugin_class}}()