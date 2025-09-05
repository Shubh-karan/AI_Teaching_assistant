import os

count = 0
folder = "RAG_Project/Audio"
filename = os.listdir(folder)

for i,files in enumerate(filename,start=1):
    old_path = os.path.join(folder,files)
    fname = files.split(" ｜ ")[0]
    new_name = f"{i}_{fname}.mp3"
    new_path = os.path.join(folder,new_name)
    os.rename(old_path,new_path)
    print(f'Renamed {fname} -> {new_name}')