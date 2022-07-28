import os

# folder path
dir_path = r'.'

res = os.listdir(dir_path)
for i in res:
    if i.startswith('0'):
        os.rename(i,'22_'+i)
    elif i.startswith('1'):
        os.rename(i,'21_'+i)