import os
from src.file_walker.types.content import Content
from src.file_walker.types.content_types import ContentType

def walk(path : str, 
         ignore_files : list[str] = [], 
         ignore_folders : list[str] = [], 
         ignore_extensions : list[str] = [], 

         file_content : str = True):


    base_depth = len(os.path.split(path))
    for root, dirs, files in os.walk(path, topdown=True):
    
        dirs[:] = [d for d in dirs if d not in ignore_folders and os.path.sep.join([root, d])]

        splits = os.path.split(root)

        yield Content(
            content_type=ContentType.TITLE,
            depth=len(splits) - base_depth,
            raw_text=[splits[-1]]
        )

        for file in files:
            if file in ignore_files and os.path.sep.join([root, file])  in ignore_files:
                continue

            cont = False

            for extension in ignore_extensions:
                if file.endswith(extension):
                    cont=True
                    break
            if cont:
                continue

            yield Content(
                content_type=ContentType.TITLE,
                depth=len(splits) - base_depth,
                raw_text=[file]
            )

            if file_content:
                with open(os.path.sep.join( [root, file]), 'r+') as f:

                    # print("abri aqui viu")
                    yield Content(
                        content_type= ContentType.CODE,
                        depth=len(splits) + 1 - base_depth,
                        raw_text=f.readlines()
                    )

