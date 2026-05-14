from os_utils.utils import init_public_dir, generate_pages
import sys


def main():
    base_path = None
    if len(sys.argv) > 1:
        assert len(sys.argv) == 2
        base_path = sys.argv[1]

    # python_static_file_generator
    base_path = 'python_static_file_generator/'
    # t = 'docs', 'public'
    init_public_dir(destination='docs')
    generate_pages(base_path=base_path, destination='docs')

if __name__ == '__main__':
    main()
