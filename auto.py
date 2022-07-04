import os
from shutil import move

source_dir = "C:/Users/portu/Downloads/TESTE"
dest_doc = "C:/Users/portu/Downloads/DOCUMENTOS"

# Lista todos os arquivos em determinado diretório
for entry in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, entry)):
        print(entry)
        name = entry

    if name.endswith('.pdf'):
