import click

from pathlib import Path

import fnmatch


import shutil


def organize_by_keyword(current_path,keyword):

    Path(current_path/keyword).mkdir(exist_ok=True)
    
    for file in Path(current_path).iterdir():
        if file.is_file():
            if fnmatch.fnmatch(file,"*"+keyword+"*"): 
                click.secho(f'{file} found')
                shutil.move(current_path/file,current_path/keyword)
           
def organize_by_extention(current_path,extention):
    Path(current_path/extention).mkdir(exist_ok=True)
    
    for file in Path(current_path).iterdir():
        if file.is_file():
            if fnmatch.fnmatch(file,"*."+extention): 
                click.secho(f'{file} found')
                shutil.move(current_path/file,current_path/extention)

@click.group()
@click.version_option(version="0.0.1",prog_name="File_Orginazer")
def main():
    """
    File Organizer :cli tool to organize your files into folder
    """
    pass

@main.command()
@click.argument('current_path')
@click.option('--keyword','-k',help="Specify the keyword to sort by")
def organize(current_path,keyword):
    """
    Organize by keyword
    eg. python3 file_organie organize . --keyword test
    """
    click.secho(f"Organize files in {current_path} by {keyword}",fg ='green')
    organize_by_keyword(Path(current_path),keyword)

    click.secho(f'Matched file stored in {Path(current_path)/keyword}',fg='green')

@main.command()
@click.argument('current_path')
@click.option('--extention','-e',help="Specify the file extention to sort by")
def organize_by_ext(current_path,extention):
    """
    Organize by extention
    eg. python3 file_organie organize-by-ext . --extention txt
    """
    click.secho(f"Organize files in {current_path} by {extention}",fg ='green')
    organize_by_extention(Path(current_path),extention)

    click.secho(f'Matched file stored in {Path(current_path)/extention}',fg='green')






if __name__ == '__main__':
    main()