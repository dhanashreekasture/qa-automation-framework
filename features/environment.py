from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory


def before_all(context):
    env = context.config.userdata.get("env", "qa")
    context.env = env

    config = ConfigManager(env)
    context.base_url = config.get_base_url()
    context.ui_url = config.get_ui_url()
    context.db_config = config.get_db_config()


def before_scenario(context, scenario):
    if "ui" in scenario.tags:
        context.driver = DriverFactory.get_driver()
        context.driver.get(context.ui_url)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        if scenario.status == "failed":
            context.driver.save_screenshot("reports/failure.png")
        context.driver.quit()