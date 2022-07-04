import os

source_dir = "C:/Users/portu/Downloads"

# Lista todos os arquivos em determinado diretório
for entry in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, entry)):
        print(entry)
