from xml.etree import ElementTree
from pip._vendor import requests

class Extractor(object):
    
    def LoadPage(self, pageURI):
        page = requests.get(pageURI)
        self.root = ElementTree.Element('RootHTML')
        ElementTree.SubElement(self.root, page.content)
        
    def PrintPreparedXML(self):
        print(ElementTree.dump(self.root))