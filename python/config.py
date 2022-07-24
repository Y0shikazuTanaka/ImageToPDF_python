import configparser
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("../resources"), relative_path)


class Config:

    CONF_FILE = resource_path("config.ini")
    CONF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONF_FILE)

    if not os.path.exists(CONF_PATH):
        raise FileNotFoundError

    cnf = configparser.ConfigParser()
    cnf.read(CONF_PATH, "UTF-8")

    # app_base_setting
    baseSettings = cnf["app_base_setting"]

    version = baseSettings["version"]
    appName = baseSettings["name"]

    imgFormats = baseSettings["img_formats"]

    # app_window_setting
    windowSettings = cnf["app_window_setting"]

    windowSizeWidth = windowSettings["window_size_width"]
    windowSizeHeight = windowSettings["window_size_height"]
    labelFilename = windowSettings["label_filename"]
    labelTitle = windowSettings["label_title"]
    labelAutor = windowSettings["label_autor"]
    labelSoft = windowSettings["label_soft"]
    labelOwnerPass = windowSettings["label_owner_pass"]
    labelReadPass = windowSettings["label_read_pass"]
    labelPrint = windowSettings["label_print"]
    labelCopy = windowSettings["label_copy"]
    labelRemove = windowSettings["label_remove"]


