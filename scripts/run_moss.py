import os
from mosspy import Moss
from argparse import ArgumentParser
from os.path import join, expanduser
from configparser import ConfigParser
from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER


def get_downloads_path():
    if os.name != "nt": return join(expanduser('~'), 'downloads')
    sub_key = "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" \
        "\Shell Folders"
    downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
    with OpenKey(HKEY_CURRENT_USER, sub_key) as key:
        return QueryValueEx(key, downloads_guid)[0]


def get_configuration():
    configurationParser = ConfigParser()
    configurationParser.read("config.ini")
    return configurationParser


def configure_arguments():
    argumentParser = ArgumentParser(
        description="Simple script that uploads a collection of \
            \"Aulas\"-structured student solutions to the Moss service \
            for plagiarism checking purposes.")
    argumentParser.add_argument("--language", help="The programming \
        language used in the assignment.", choices=Moss.languages,
                                default="haskell")
    argumentParser.add_argument("--path", help="The path to the \
        solutions to be processed.", required=True)
    argumentParser.add_argument("--base_path", help="Path to the base \
        file(s) handed to students as part of the assignment.")
    return argumentParser


userId = get_configuration()["Moss"]["userId"]
arguments = configure_arguments().parse_args()
moss = Moss(userId, arguments.language)
