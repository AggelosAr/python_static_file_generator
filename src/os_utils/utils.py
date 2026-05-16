from typing import Optional

from blocks.block_utils import markdown_to_html_node, MarkDownBlock

import os 
import shutil


def init_public_dir(source='static', destination='public'):
    
    current_dir = os.getcwd()

    source_dir, destination_dir = os.path.join(*[current_dir, source]), os.path.join(*[current_dir, destination])
    print(f'Deleting <{destination_dir}> dir')
    # Clean public dir
    if os.path.exists(path=destination_dir):
        shutil.rmtree(path=destination_dir)

    os.mkdir(path=destination_dir)

    # Add updated contents from static dir
    copy_tree(source=source_dir, destination=destination_dir)


def copy_tree(source: str, destination:str):

    for content in os.listdir(path=source):

        content_path = os.path.join(*[source, content])
        destination_path = os.path.join(*[destination, content])
        
        if os.path.isfile(content_path):
            # if it is a file copy it.
            shutil.copy(src=content_path, dst=destination_path)
        else:
            # else create the dir and copy it's contents recursively
            if not os.path.exists(path=destination_path):
                os.mkdir(path=destination_path)
            copy_tree(source=content_path, destination=destination_path)
    

def generate_page(from_path: str='content/index.md', 
                  template_path: str='template.html', 
                  dest_path: str='public/index.html',
                  base_path: Optional[str]=None):

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as file:
        markdown_data = file.read()
    
    with open(template_path, 'r') as file:
        template_data = file.read()

    title = MarkDownBlock(markdown_data).extract_title()
    html_string = markdown_to_html_node(markdown=markdown_data).to_html()

    template_data = template_data.replace('{{ Title }}', title)
    template_data = template_data.replace('{{ Content }}', html_string)

    if base_path:
        template_data = template_data.replace('href="/', f'href="{base_path}')
        template_data = template_data.replace('src="/', f'src="{base_path}')

    with open(dest_path, 'w') as file:
        file.write(template_data)


def generate_pages(base_path: str='/', search_path: str='content', destination: str='public'):
    print(f'Initializing using base path <{base_path}>')

    for content in os.listdir(path=search_path):
        content_path = os.path.join(*[search_path, content])

        path_parts = os.path.splitext(content_path)
        path = path_parts[0].replace('content', destination)
        ext = path_parts[1]
        
        if os.path.isfile(content_path):

            if ext == '.md':
                generate_page(base_path=base_path, from_path=content_path, dest_path=f'{path}.html')
        else:
            if not os.path.exists(path):
                os.mkdir(path=path)
            generate_pages(base_path=base_path, search_path=content_path, destination=destination)
