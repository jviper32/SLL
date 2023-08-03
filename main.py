from src.dl_files.dl_xml import dl_xml
from src.perf_work.xml_parse import xml_parse
from src.dl_files.dl_audio import dl_audio
from src.perf_work.transcript import trans

def main():
    dl_xml()
    xml_parse()
    dl_audio()
    trans()

if __name__ == '__main__':
    main()