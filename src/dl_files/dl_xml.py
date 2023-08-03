import requests
import os
from dotenv import load_dotenv

load_dotenv()
XML_SRC = os.getenv('XML_SRC')
XML_FILE = os.getenv('XML_FILE')

def dl_xml():
    xml_src = requests.get(XML_SRC)

    with open(XML_FILE, "wb") as xml:
        xml.write(xml_src.content)