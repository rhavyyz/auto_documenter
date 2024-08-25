from src.cli import gen_parser
from src.ignore_parser.parser import parse as ig_parse
from src.render.factory import Factory
from src.file_walker.walk import walk


def main():
    # output_file
    # ignore_file
    # render_type
    # has_summary

    args = gen_parser().parse_args()
    # print("resenha")
    ignore_props= ig_parse(args.ignore_file)
    
    renderer = Factory.generate_renderer(args.render_type)

    if args.has_summary:
        for content in walk(path=args.path, **ignore_props, file_content=False):
            renderer.add_content(content)
    
    for content in walk(path=args.path, **ignore_props, file_content=True):
        renderer.add_content(content)

    renderer.construct(args.output_file)


if __name__ == "__main__":
    main()