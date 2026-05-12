from textnode import TextNode


def main():
    text_node = TextNode(text='This is some anchor text',
                         text_type='link',
                         url='https://www.boot.dev')


    print(text_node)


if __name__ == '__main__':
    main()
