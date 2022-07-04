from os import scandir
from os import rename
from os.path import splitext, exists, join
from shutil import move
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:/Users/portu/Downloads/TESTE"
dest_dir_videos = "C:/Users/portu/Downloads/VIDEOS"
dest_dir_images = "C:/Users/portu/Downloads/IMAGENS"
dest_dir_docs = "C:/Users/portu/Downloads/DOCUMENTOS"
dest_dir_programs = "C:/Users/portu/Downloads/PROGRAMAS"
dest_dir_music = "C:/Users/portu/Downloads/MUSICAS"


def makeUnique(dest, name):
    filename, extesion = splitext(name)
    contador = 1

    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(contador)}){extesion}"
        contador += 1

    return name


def mover_arquivo(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = makeUnique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest, copy_function=2)


class manipularAlteracoes(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                # dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    mover_arquivo(dest_dir_music, entry, name)
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    mover_arquivo(dest_dir_videos, entry, name)
                elif name.endswith('.pdf') or name.endswith('.xlsx'):
                    dest = dest_dir_docs
                    mover_arquivo(dest, entry, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = manipularAlteracoes()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
