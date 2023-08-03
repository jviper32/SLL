import lxml.etree as ET
import json
import os
from dotenv import load_dotenv

load_dotenv()
XML_FILE = os.getenv('XML_FILE')
TITLE_URL_JSON = os.getenv("TITLE_URL_JSON")

def xml_parse():
    tree = ET.parse(XML_FILE)
    elements = tree.xpath("//item//enclosure[@url]")

    title_url_dict = {
        element.getparent().findtext("title").encode("utf-8").decode("utf-8"): 
        element.get("url") for element in elements
        }

    with open(TITLE_URL_JSON, "r") as f:
        existing_data = json.load(f)

    for key, value in title_url_dict.items():
        if key not in existing_data:
            existing_data[key] = value

    with open(TITLE_URL_JSON, "w") as f:
        json.dump(existing_data, f, indent=4)