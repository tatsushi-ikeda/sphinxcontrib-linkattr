from lxml import html, etree
from glob import glob
parser = etree.HTMLParser(remove_blank_text=True)
embedded = etree.fromstring(open('embedded.xml').read(), parser).xpath('/html/head/script')
for filename in glob('**/*.html', recursive=True):
    tree   = etree.parse(open(filename), parser)
    head   = tree.xpath('/html/head')[0]
    for e in embedded:
        head.append(e)
    tree.write(filename, pretty_print=True, method='html', encoding='utf-8')
