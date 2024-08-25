import os
def parse(path):
    args = {
        'ignore_files': [], 
        'ignore_folders' : [], 
        'ignore_extensions'  : []
    }
    
    try:
        with open(path, 'r+') as f:
            for line in f.readlines():
                if pos := line.find('#') != -1:
                    line = line[: pos].strip()

                if line == '' or line == '*':
                    continue

                if line[-1] ==  os.path.sep:
                    args['ignore_folders'].append(line)
                elif line[0] == '*':
                    args['ignore_extensions'].append(line[1:])
                else:
                    args['ignore_folders'].append(line)
                    args['ignore_files'].append(line)
    except Exception as e:
        print(e)

    return args