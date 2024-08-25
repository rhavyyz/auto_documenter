from src.file_walker.types.content import Content
from src.render.base_render import BaseRenderer
from uuid import uuid4
import os

class MdPdfRender(BaseRenderer):

    def __init__(self) -> None:
        
        self.___file = f"{uuid4().__str__()}.md"

        open(self.___file, 'x')


        super().__init__()

    def add_content(self, content : Content) -> None:
        with open(self.___file, "a+") as file:
            file.writelines(content.raw_text)
            file.writelines(['\n', '\n'])

    def construct(self, path : str) -> str:
        # print("valha como constroi")
        return

    def __del__(self):
        os.remove(self.___file) 
        return