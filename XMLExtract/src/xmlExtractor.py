if __name__ == '__main__':
    from test.sampleExtractor import Extractor
    e = Extractor()
    e.LoadPage('http://www.mvideo.ru')
    
    e.PrintPreparedXML()
