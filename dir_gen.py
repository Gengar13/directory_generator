#dir_gen module
"""
module takes a path to a text file as argument and creates a folder structure
that corresponds to it
Copyright (C) 2021  Hanoune El Mehdi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
import os

def count_nb_of_tabs(foldername : str) -> int:
    nb=len(foldername) - len(foldername.lstrip())
    return nb//2

def make_element(element : str) -> None:
    if ":" in element:
        element = element.replace(":","")
        os.system(f"mkdir {element}")
    else:
        os.system(f"touch {element}")

def make_dir_struct(struct_file : str) ->None:
    with open(struct_file) as f:
        data = f.readlines()
    folder_list=[]
    for line in data:
        if ":" in line:
            folder_list.append(line)
    folder_origin=[]
    for line in data:
        folder_origin.append(count_nb_of_tabs(line))
    clear_data =[]
    for el in data:
        clear_data.append(el.replace(" ","").replace("\n",""))
    r = zip(clear_data,folder_origin)
    levels = list(r)
    cursor = 0
    for (i,jo) in levels:
        if cursor==jo:
            make_element(i)
            if ":" in i:
                prev_folder = i.replace(":","").replace("\n","")
        elif cursor<jo:
            os.chdir(prev_folder)
            cursor+=1
            make_element(i)
            if ":" in i:
                prev_folder = i.replace(":","").replace("\n","")
        elif cursor>jo:
            while cursor!=jo:
                os.chdir("../")
                cursor-=1
            make_element(i)
            if ":" in i:
                prev_folder = i.replace(":","").replace("\n","")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',"--file",action="store",required=True,
        help="structure file path")
    make_dir_struct(parser.parse_args().file)
   

if __name__=="__main__":
    main()
