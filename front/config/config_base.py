from tornado.options import define, options


class ConfigBase(object):
    _DEFAULT_CONFIG_FILE = "/code/config/front.conf"

    @staticmethod
    def setup():
        # Define options
        define("back_client_api_url", type=str, help="BACK APP Api url")
        define("back_celery_config", type=dict, help="BACK APP Celery setting")

        # Load from file
        options.parse_config_file(ConfigBase._DEFAULT_CONFIG_FILE)
