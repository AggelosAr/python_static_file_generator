import os 
import shutil


def init_public_dir(root='.', source='static', destination='public'):
    
    current_dir = os.getcwd()

    source_dir, destination_dir = os.path.join(*[current_dir, source]), os.path.join(*[current_dir, destination])
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
    
