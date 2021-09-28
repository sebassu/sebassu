from mosspy import Moss
from argparse import ArgumentParser
from configparser import ConfigParser


def get_configuration():
    configurationParser = ConfigParser()
    configurationParser.read("config.ini")
    return configurationParser


userId = get_configuration()["Moss"]["userId"]
argumentParser = ArgumentParser(
    description="Simple script that uploads a collection of \"Aulas\"-\
    structured student solutions to the Moss service for plagiarism \
    checking purposes.")
argumentParser.add_argument("--language", help="The programming \
    language used in the assignment.", choices=Moss.languages,
                            default="haskell")
argumentParser.add_argument("--path", help="The path to the solutions \
    to be processed.")
argumentParser.add_argument("--base_path", help="Path to the base file\
    (s) handed to students as part of the assignment.", default=None)

arguments = argumentParser.parse_args()
moss = Moss(userId, argumentParser.language)
