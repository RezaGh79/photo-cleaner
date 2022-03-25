import os
import re
import shutil

from help import create_folder
from help import get_create_time
from help import printDictionary
from help import to_hash
from help import add_needed_folders_to_destination
from collections import Counter


def number_generator(date):
    number_list.append(date)
    return Counter(number_list)[date]


def generate_name(key):
    date = get_create_time(key)
    name = key.split("\\")[-1]
    return date + '_' + '{:0>4}'.format(str(number_generator(date))) + '_' + re.sub('[;_(),]', '', name)


def generate_final_image_dict(dict):
    for key, value in dict.items():
        dict[key] = 'C:\\Users\\MoDerN\\Desktop\\processed\\' \
                    + "\\".join(key.split("\\")[5:-1]) + '\\' + generate_name(key)
        shutil.copyfile(key, dict[key])


def process(address):
    final_address = 'C:\\Users\\MoDerN\\Desktop\\processed'
    create_folder(final_address)

    # Error if file doesn't exist
    if not os.path.exists(address):
        print("Folder doesn't exist.")
        return

    folder_list = set()

    for dirpath, dirs, files in os.walk(address):
        for filename in files:
            fname = os.path.join(dirpath, filename)
            folder_list.add(dirpath.replace("process", "processed"))
            if fname.endswith('.png') or fname.endswith(".jpg") or fname.endswith('.jpeg'):
                dictionary[fname] = to_hash(fname)

    add_needed_folders_to_destination(folder_list)
    # delete duplicate values and save
    # final dictionary into (result)
    for key, value in dictionary.items():
        if value not in dictionary_deleted_duplicates.values():
            dictionary_deleted_duplicates[key] = value

    # number_generator(dictionary_deleted_duplicates)
    # number_generator(dictionary_deleted_duplicates)
    generate_final_image_dict(dictionary_deleted_duplicates)
    print("Number of detected input files: {},"
          " number of processed output files: {}"
          .format(len(dictionary), len(dictionary_deleted_duplicates)))

    return final_address


path = 'C:\\Users\\MoDerN\\Desktop\\process'
# dictionary of address and hash
dictionary = {}
dictionary_deleted_duplicates = {}
number_list = []

print(process(path))
# printDictionary(dictionary)
# printDictionary(dictionary_deleted_duplicates)
# printDictionary(dictionary_deleted_duplicates)
