from dataclasses import dataclass
from src.file_walker.types.content_types import ContentType 

@dataclass
class Content:
    content_type : ContentType
    raw_text : list[str]
    depth : int