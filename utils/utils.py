import os

# Custom imports
from . import constants


def get_file_name():
    filename = input("Nom du fichier à analyser : ")

    try:
        files = os.listdir(constants.DIRECTORY)
    except Exception as e:
        print("Une erreur est survenue. Vérifiez la présence du dossier " +
             f"des instances de génome dans le réportoire courant SVP. ({e})")
        exit(1)

    if filename not in files:
        print(f"Ce fichier n'existe pas dans Instances_genome/")
        exit(1)

    return filename


def parse_file(path):
    with open(path, "r") as file:
        content = file.read()

    # Remove tailing LR and potential whitespaces
    content = content.strip("\n ").split('\n')

    # Keeping only the last 2 lines without inner whitespaces
    content = [line.replace(' ', '') for line in content [-2:]]

    return content


def csub(a, b):
    return (a != b) * (3 * (a in ('A', 'T') and b in ('A', 'T') or a in ('G', 'C') and b in ('G', 'C')) or 4)
