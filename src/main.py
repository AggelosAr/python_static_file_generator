from os_utils.utils import init_public_dir, generate_page



def main():
    init_public_dir()
    generate_page()

    generate_page(from_path='content/blog/glorfindel/index.md',
                  dest_path='public/glorfindel.html')
    
    generate_page(from_path='content/blog/tom/index.md',
                  dest_path='public/tom.html')

    generate_page(from_path='content/blog/majesty/index.md',
                  dest_path='public/majesty.html')
    
    generate_page(from_path='content/contact/index.md',
                  dest_path='public/contact.html')

if __name__ == '__main__':
    main()
