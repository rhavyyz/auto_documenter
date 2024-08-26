from src.file_walker.types.content_types import ContentType
from src.file_walker.types.content import Content
from src.render.base_render import BaseRenderer
from markdown_pdf import MarkdownPdf, Section
from uuid import uuid4
import os

class MdPdfRender(BaseRenderer):

    def __init__(self) -> None:
        
        self.___file = f"{uuid4().__str__()}.md"
        open(self.___file, 'x')
        self.___chapters = []
        super().__init__()


    def __gen_chapter(self, depth):
        while(depth > len(self.___chapters)):
            self.___chapters.append(0)
        while(depth < len(self.___chapters)):
            self.___chapters.pop()
        self.___chapters[-1]+=1

        return ".".join([str(x) for x in self.___chapters])

    def __fix_indent(self, l : list[str], d, spacer):
        
        d = min(d, 4)

        ans = []

        for line in l:
            # line = ""

            # line = line.strip() + '\n'
            if line.find('```') != -1:
                ans.append(line)
                continue
            # print(f"{line}")
            
            if line.find("## ") != -1:
                line = line.replace("## ", f"## {spacer*d*2}")
                ans.append(line)
                continue

            line = spacer*int(d/2)+line
            ans.append(line)

        return ans

    def __convert_content(self, content : Content):

        if content.content_type == ContentType.TITLE:
            if content.depth == 0:
                return "# " + " ".join(content.raw_text)
            content.raw_text[0] = "## " + self.__gen_chapter(content.depth) + ' ' + content.raw_text[0]
            return self.__fix_indent(content.raw_text, content.depth, "&nbsp; ")
        elif content.content_type == ContentType.TEXT:
            return self.__fix_indent(content.raw_text, content.depth)
        elif content.content_type == ContentType.CODE:
            return self.__fix_indent(['```\n'] + content.raw_text + ['\n```\n'], content.depth, "\t ")

    def add_content(self, content : Content) -> None:
        with open(self.___file, "a+") as file:
            file.writelines(self.__convert_content(content))
            file.writelines(['\n\n'])

    def construct(self, path : str) -> str:
        # print("valha como constroi")
        pdf = MarkdownPdf(toc_level=2)
        with open(self.___file, "r") as file:
            for line in file.readlines():
                pdf.add_section(Section(line))
        pdf.save(path)

    def __del__(self):
        # os.remove(self.___file) 
        return