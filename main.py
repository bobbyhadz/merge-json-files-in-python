# How to merge multiple JSON files in Python

import json


def merge_json_files(file_paths):
    merged_contents = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file_in:
            merged_contents.extend(json.load(file_in))

    with open('employees_final.json', 'w', encoding='utf-8') as file_out:
        json.dump(merged_contents, file_out)


paths = [
    'employees_1.json',
    'employees_2.json'
]

merge_json_files(paths)