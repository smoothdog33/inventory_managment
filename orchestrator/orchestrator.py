
import logging
from shlex import quote

from pandas.core.common import not_none

# Configure logging
logging.basicConfig(
    level=logging.INFO,              # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler('batch_application.log'),    # Log to a file
        logging.StreamHandler()                          # Log to console
    ]
)
from generators.supplier_profile import supplier_profile_class
from generators.product import product_class
from generators.supplier_questions import supplier_questions_class
from generators.warehouse_profile import warehouse_profile_class
from integrators.supplier_updater import supplier_updater_class
from integrators.supplier_products_questions_xref import supplier_conv_class
from integrators.create_supplier_file_for_quote import quote_class
from integrators.load_responses_from_supplier import responses_class
from connections.properties import product_property_func,profile_property_func,questions_property_func,warehouse_property_func,supplier_products_questions_xref,create_supplier_for_quote

from connections.connection import get_connection

import pandas
import argparse
from faker import Faker
fake = Faker()
#instance = product_class()
#instance1 = supplier_profile_class()
#instance2 = supplier_questions_class()
#instance3 = warehouse_profile_class()
#instance4 = supplier_updater_class()
#instance5 = supplier_conv_class()
product_file = product_property_func()
profile_file = profile_property_func()
questions_file = questions_property_func()
warehouse_file = warehouse_property_func()
supplier_products_questions_xref_file = supplier_products_questions_xref()
create_supplier_for_quote_file = create_supplier_for_quote()
print("hi")
try:
    logging.info("product task started.")
    instance = product_class()
    instance.product_func()
    instance.product_inserter(product_file, 'products')
except Exception as err:
    logging.info("product task error.")
logging.info("product task ended.")
try:
    logging.info("profile task started.")
    instance1 = supplier_profile_class()
    instance1.supplier_profile()
    instance1.supplier_profile_inserter(profile_file, 'profile_')

except Exception as err:
    logging.info("profile task error.")
logging.info("profile task ended.")
try:
    logging.info("questions task started.")
    instance2 = supplier_questions_class()
    instance2.supplier_questions()
    instance2.question_inserter(questions_file, 'questions')
except Exception as err:
    logging.info("questions task ended.")
logging.info("questions task ended.")
try:
   logging.info("warehouse task started.")
   instance3 = warehouse_profile_class()
   instance3.warehouse_profile()
   instance3.warehouse_inserter(warehouse_file,'warehouse_profile')
except Exception as err:
    print(f"4Unexpected {err=}, {type(err)=}")
    logging.info("warehouse task error.")
logging.info("warehouse task ended.")
try:
    logging.info("supplier_conv task started.")
    instance5 = supplier_conv_class()
    instance5.supplier_products_questions_xref_func()
    instance5.supplier_products_questions_xref_inserter(supplier_products_questions_xref(),'supplier_products_questions_xref_table')
except Exception as err:
    logging.info("supplier_conv task error.")
logging.info("supplier_conv task ended.")
try:
    logging.info("supplier quote task started.")
    instance6 = quote_class()
    instance6.json_inserter()
except Exception as err:
    print(f" 5Unexpected {err=}, {type(err)=}")
    logging.info("supplier quote task error.")
logging.info("supplier quote task ended.")

try:
    logging.info("responses task started.")
    instance7= responses_class()
    instance7.load_responses(create_supplier_for_quote_file)
except Exception as err:
    print(f"6Unexpected {err=}, {type(err)=}")
    logging.info("responses task error.")
logging.info("responses task ended.")

try:
    logging.info("supplier_updater task started.")
    instance8 = supplier_updater_class()
    instance8.supplier_updater_func()
except Exception as err:
    print(f"7Unexpected {err=}, {type(err)=}")
    logging.info("supplier_updater task error.")
logging.info("supplier_updater task ended.")





