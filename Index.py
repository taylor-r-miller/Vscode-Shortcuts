import sys, os, subprocess, re 


#only supply a base dir if not on a mac 
# BASE_PATH = '/Users/taylormiller/'
BASE_PATH = None
IGNORE = ['.DS_Store']

SHORTCUTS = {
    "projects":{ 
        "path": 'Documents/Projects',
        "include_all":True 
        },
    "work":{ #example of only listing certain files
        "path": 'Documents/Work',
        "include_all": False,
        "include":[ #exact dir name
 
        ]
    }
}


def Shortcuts():

    [_,directory] = sys.argv

    directory = directory.strip()
    try: 
        info = SHORTCUTS.get(directory)
        path = info.get('path')
    except AttributeError:
        print('Attempting to access a shortcut that does not exits')
        return
    
    #handle for base dir being provided 
    if BASE_PATH:
        abs_path = f'{BASE_PATH}{path}'
    else:
        #extract the base path so we can use relative paths in the shortcut dictionary     
        osx_pattern = re.compile('^(/Users/.+?)/')
        full_path  = os.getcwd()
        base_path = f'{osx_pattern.search(full_path).group()}/'
        abs_path = f'{base_path}{path}'
        
    inlcude_all = info.get('include_all')

    if inlcude_all:
        files = [row for row in os.listdir(abs_path) if row not in IGNORE]
    else:
        files_to_include = info.get('include')
        files = [row for row in os.listdir(abs_path) if row not in IGNORE and row in files_to_include] 

    valid_choice = False
    #display a choice if we have multiple files
    if len(files) > 1:
        #print until a valid options is chosen or the user cancels program
        while not valid_choice:
            choice_dictionary ={}
            for index,row in enumerate(files,1):
                print(f'{index}.) {row}')
                choice_dictionary.update({index:row})
            try:
                num_chosen = int(input('What do you want to open?'))
            except KeyboardInterrupt:
                return
            #handle for invalide choices
            try:
                dir_choice = choice_dictionary.get(num_chosen).replace(' ','\ ')
                valid_choice = True 
                command = f'cd && code {path}/{dir_choice}'
            except AttributeError:
                print('Invalid choice. Select from list.')
 
    else:
        dir_choice = info.get('include')[0].strip().replace(' ', '\ ')
        command = f'cd && code {path}/{dir_choice}'



    subprocess.run(command,shell=True)


if __name__ == '__main__':
    Shortcuts()
