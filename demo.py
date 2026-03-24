#logging
import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)
#logging.disable(logging.CRITICAL)
age = 45

if age < 18:
    print("UNDERAGE")
    logging.warning("Warning")
else:
    print("Pass")
    logging.info("info")