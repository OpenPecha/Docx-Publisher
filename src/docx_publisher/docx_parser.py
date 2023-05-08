import docx
from pathlib import Path
from time import sleep



def split_docx(doc):
    texts = []
    in_language1 = True
    last_font_size = 0
    language1 = []
    language2 = []
    for cur_para in doc.paragraphs:
        print(cur_para.text)
        print(len(cur_para.text))
        
        if cur_para.style.name == 'Heading 1':
            if cur_para.style.font.size != last_font_size:
                in_language1 = not in_language1
        if in_language1:
            language1.append(cur_para.text)
        else:
            language2.append(cur_para.text)
        last_font_size = cur_para.style.font.size if len(cur_para.text)!=0 else last_font_size

    texts = ['\n'.join(language1),'\n'.join(language2)]
    return texts

def create_repo(text,title):
    repo_name = "XYZ"
    text_path = f"{repo_name}/{title}.txt"
    Path(repo_name).mkdir()
    Path(text_path).write_text(text)
    return repo_name

def create_repos(texts,title):
    repos = []
    for text in texts:
        repos.append(create_repo(text,title))
        sleep(2)
    
    return repos

def main(docx_path):
    doc = docx.Document(docx_path)
    title = doc.core_properties.title
    texts = split_docx(doc)
    repos = create_repos(texts,title)

if __name__ == "__main__":
    docx_path = "'EN_BO_WEB/article_docx/01.བོད་འགྱུར་དྲ་རྩོམ།.docx'"
    main(docx_path)



