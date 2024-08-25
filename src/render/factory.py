from abc import ABC

from src.render.enum import RenderesEnum
from src.render.base_render import BaseRenderer
from src.render.renders.MdPdfRender import MdPdfRender


class Factory(ABC):
    ___factory : dict[RenderesEnum,BaseRenderer] = {
        RenderesEnum.MARKDOW_PDF: MdPdfRender
    }

    @classmethod
    def generate_renderer(cls, renderer : RenderesEnum) -> BaseRenderer:
        return cls.___factory[renderer]()