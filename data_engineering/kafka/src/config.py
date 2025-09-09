import configparser
import os


# Define the path to the properties file
properties_path = os.path.expanduser(
    "data_engineering/kafka/.confluent/python.properties"
)

# Initialize the parser and read the properties file
parser = configparser.ConfigParser()
parser.read(properties_path)

# Convert the properties to a dictionary
config = {key: value for key, value in parser.items("learn-kafka")}
