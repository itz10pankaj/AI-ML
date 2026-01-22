import logging

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("Aithmatic")

def addition(a,b):
    result=a+b
    logger.debug(f"{a} + {b} = {result}")
    return result
addition(2,3)