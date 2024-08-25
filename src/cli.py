import argparse
from src.render.enum import RenderesEnum

def gen_parser():
    parser = argparse.ArgumentParser(description='Auto Documenter')

    parser.add_argument("path", action="store",type=str)
    parser.add_argument('-o', action="store",type=str, dest='output_file', default="a.pdf")
    parser.add_argument('-i', action="store",type=str , dest='ignore_file', default=".ig")
    parser.add_argument('-r', action="store",type=RenderesEnum , dest='render_type', default="MARKDOW_PDF")
    parser.add_argument('-s', action="store",type=bool , dest='has_summary', default="True")


    return parser