from os_utils.utils import init_public_dir, generate_page



def main():
    init_public_dir()
    generate_page()

    generate_page(from_path='content/blog/glorfindel/index.md',
                  dest_path='public/glorfindel.html')

if __name__ == '__main__':
    main()
