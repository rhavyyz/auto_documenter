import os
from src.file_walker.types.content import Content
from src.file_walker.types.content_types import ContentType

def walk(path : str, 
         ignore_files : list[str] = [], 
         ignore_folders : list[str] = [], 
         ignore_extensions : list[str] = [], 

         file_content : str = True):

    visited = set()

    base_depth = len(path.split(os.path.sep))

    for root, dirs, files in os.walk(path, topdown=True):
    
        if root is visited:
            continue
        visited.add(root)

        dirs[:] = [d for d in dirs if d not in ignore_folders and os.path.sep.join([root, d]) not in ignore_folders]

        # if not file_content:
        #     print(root)
        splits = root.split(os.path.sep)

        # print(len(splits))

        yield Content(
            content_type=ContentType.TITLE,
            depth=len(splits) - base_depth,
            raw_text=[splits[-1]]
        )

        for file in files:
            file_full_path = os.sep.join([root, file]) 
            visited.add(file_full_path)
            if file in ignore_files and file_full_path  in ignore_files:
                continue

            cont = False

            for extension in ignore_extensions:
                if file.endswith(extension):
                    cont=True
                    break
            # print(cont)
            if cont:
                continue

            yield Content(
                content_type=ContentType.TITLE,
                depth=len(splits) +1 - base_depth,
                raw_text=[file]
            )

            if file_content:
                with open(os.path.sep.join( [root, file]), 'r+') as f:
                    # print(os.path.sep.join([root, file]))
                    # print("abri aqui viu")
                    yield Content(
                        content_type= ContentType.CODE,
                        depth=len(splits) + 2 - base_depth,
                        raw_text=f.readlines()
                    )

