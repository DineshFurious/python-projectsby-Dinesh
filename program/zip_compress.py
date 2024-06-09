import zipfile
import pathlib


def make_archive(filepath, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressedddd.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for files in filepath:
            archive.write(files)



# if __name__ == "__main__":
#     make_archive(filepath=["text1", "text2"], dest_dir="Bonus")