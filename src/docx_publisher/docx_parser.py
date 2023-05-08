import docx
from pathlib import Path
from time import sleep
import uuid



def split_docx(doc):
    splitted_files = []
    last_font_size = 0
    texts = []
    for i,cur_para in enumerate(doc.paragraphs):
        print(cur_para.text)
        print(len(cur_para.text))
        
        if cur_para.style.name == 'Heading 1':
            if cur_para.style.font.size != last_font_size and i != 0:
                splitted_files.append('\n'.join(texts))
                texts = []
        texts.append(cur_para.text)
        last_font_size = cur_para.style.font.size if len(cur_para.text)!=0 else last_font_size

    return splitted_files


def create_repo(text,start_index):
    repo_path = f"./data/{str(uuid.uuid4())[:4]}"
    repo_path = f"./data/{start_index}"
    Path(repo_path).mkdir(exist_ok=True, parents=True)
    text_path = f"{repo_path}/{start_index}_{str(uuid.uuid4())[:4]}.txt"
    Path(text_path).write_text(text)
    create_readme(Path(repo_path))
    return repo_path


def create_readme(path):
    result = "# EN_BO_WEB"
    readme_fn = path / "README.md"
    readme_fn.write_text(result)


def create_repos(texts):
    start_index = 7000
    repos = []
    for i,text in enumerate(texts):
        if i % 2 == 0 and i != 0:
            start_index += 1
        repos.append(create_repo(text,start_index))
    return repos

def main(docx_path):
    doc = docx.Document(docx_path)
    title = doc.core_properties.title
    texts = split_docx(doc)
    repos = create_repos(texts)

if __name__ == "__main__":
    docx_path = "EN_BO_WEB/article_docx/03.བོད་འགྱུར་དྲ་རྩོམ།.docx"
    main(docx_path)



