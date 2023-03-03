import utils

g_logger = utils.Logger()

def run():
    g_logger.debug("Hello debug")
    g_logger.info("Hello info")
    g_logger.warning("Hello warning")
    g_logger.error("Hello error")
    g_logger.critical("Hello critical")


if __name__ == "__main__":
    run()
