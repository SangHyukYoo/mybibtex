import bibtexparser
from jinja2 import Environment, FileSystemLoader

# BibTeX 파일을 파싱합니다.
with open('ref.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Jinja2 템플릿을 로드합니다.
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# 파싱된 데이터를 템플릿에 적용합니다.
html_output = template.render(entries=bib_database.entries)

# 결과를 HTML 파일로 저장합니다.
with open('index.html', 'w') as html_file:
    html_file.write(html_output)
