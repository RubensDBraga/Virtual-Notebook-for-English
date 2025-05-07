from pathlib import Path
from time import sleep


def createfile(file):
    path = Path(file)
    if not path.exists():
        path.touch()
        print('File created')
    else:
        print('Loading...')


def read(archive):
    sleep(0.5)
    with open('Evolution_in_English.txt', 'r') as archive:
        content = archive.readlines()
        for line in content:
            print(line.strip())


def create(english='Indeterminate', portuguese='Indeterminate'):
    with open('Evolution_in_English.txt', 'a') as file:
        file.write(f'{english} - {portuguese}\n')
