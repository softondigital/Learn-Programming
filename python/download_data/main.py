#!/usr/bin/env python
'''The main module'''
from pathlib import Path
import requests


def download_file(
        file_url: str,
        path: str,
) -> str:
    '''Downloads a file

    :param file_url: The URL of the resource to download
    :param filename: The filename of the file
    :param path: The path where the file will be saved
    :return: The local path to the downloaded file
    '''
    req = requests.get(file_url, stream=True)

    with open(path, 'wb') as file_object:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                file_object.write(chunk)

    return path


def main():
    '''Main function'''
    csv_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
    file_name = csv_url.split('/')[-1:][0]
    file_path = Path.cwd() / 'instance' / file_name
    download_file(csv_url, file_path)

if __name__ == '__main__':
    main()
