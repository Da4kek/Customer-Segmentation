import zipfile 
import os

def extract_main():
    with zipfile.ZipFile("instacart-market-basket-analysis.zip") as zip_:
        zip_.extractall("Data/")

def extract_in():
    for i in os.listdir("Data/"):
        with zipfile.ZipFile(f"Data/{i}") as zip_re:
            zip_re.extractall("Data/")

extract_in()