from os import environ, pardir, path
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


DATA_DIR = environ.get('DATA_DIR_NAME')
OUTPUT_DIR = environ.get('OUTPUT_DIR_NAME')

RAW_DATA_FILENAME = environ.get('RAW_DATA_FILE_NAME')
PRICES_FILENAME = environ.get('PRICES_FILE_NAME')
MIN_PRICE_FILENAME = environ.get('MIN_PRICE_FILE_NAME')
BARPLOT_PARKING = environ.get('BARPLOT_PARKING')
BARPLOT_ROOMS = environ.get('BARPLOT_ROOMS')
SCATTERPLOT_INTERIORS = environ.get('SCATTERPLOT_INTERIORS')


PROJECT_DIR = path.abspath(path.join(path.dirname(__file__), pardir))
DATA_PATH = path.join(PROJECT_DIR, DATA_DIR)
OUTPUT_PATH = path.join(PROJECT_DIR, OUTPUT_DIR)


class DataFilesConf:

    class Paths:
        data = DATA_PATH
        output = OUTPUT_PATH

    class FileNames:
        raw_data = join(DATA_PATH, RAW_DATA_FILENAME)
        prices = join(OUTPUT_PATH, PRICES_FILENAME)
        min_price = join(OUTPUT_PATH, MIN_PRICE_FILENAME)
        barplot_parking = join(OUTPUT_PATH, BARPLOT_PARKING)
        barplot_rooms = join(OUTPUT_PATH, BARPLOT_ROOMS)
        scatterplot_interiors = join(OUTPUT_PATH, SCATTERPLOT_INTERIORS)


