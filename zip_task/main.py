import os, zipfile, random

def get_packed(in_dir, output_directory: str):
    files_list = [os.path.join(in_dir, i) for i in os.listdir(in_dir)]
    output = os.path.join(output_directory, os.path.splitext(random.choice(files_list))[0])+'.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in files_list:
            zipf.write(os.path.join(f))


a = input('Введите путь: ')
a = a if a else os.getcwd()
get_packed(a, a)

