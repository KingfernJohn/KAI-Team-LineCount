import sys, os, time

while True:
    time.sleep(1)
    os.system('cls')
    every_line = int(0)
    print()

    for path, subdirs, files in os.walk("C:/Users/Kingfern/Desktop/KAI-Cryp"):
        for name in files:
            if path.endswith('__pycache__'):
                break
            elif name == '.gitignore' or name == 'LICENSE' or name == 'CHANGELOG.txt' or name == 'manifest.in' or name == 'README.md' or name == 'README.txt':
                break
            elif name.endswith('.py') == False:  # 2 Lines Filter PYTHON only
                break                            #
            else:
                path = path.replace("\\", "/")
                path = path[path.find('KAI-Cryp'):]
                insges = path+'/'+name
                insges = str(insges)
                lines = sum(1 for line in open(insges, 'r'))
                print(f"{name}     \t->\t{lines}")
                lines = int(lines)
                every_line += lines

    print(f"\n{every_line}\n")
