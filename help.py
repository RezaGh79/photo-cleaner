import os
import time

import imagehash
from PIL import Image


def create_folder(address):
    if not os.path.exists(address):
        os.makedirs(address)


def get_create_time(address):
    return time.strftime('%Y%m%d', time.gmtime(os.path.getmtime(address)))
    # return time.ctime(os.path.getctime(address))


def get_modify_date(address):
    return time.ctime(os.path.getmtime(address))


def printDictionary(dict):
    print("\n", "final dictionary: ")
    for i in dict:
        print(i, " = ", dict[i])


def similar_or_not(hash0, hash1):
    # true means similar
    # maximum bits that could be different between the hashes.
    cutoff = 5

    if hash0 - hash1 < cutoff:
        return True
    else:
        return False


def to_hash(address):
    return imagehash.average_hash(Image.open(address)).__str__()


def add_needed_folders_to_destination(folder_list):
    for address in folder_list:
        if not address.endswith("processed"):
            create_folder(address)