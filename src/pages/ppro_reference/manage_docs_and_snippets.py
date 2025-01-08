'''

! WORK IN PROGRESS !

'''

import os
from typing import List
import datetime

# CLASSES #

class documentation_library:
    '''
    Describe an entire cluster of documentation .md files
    The documentatation library is composed of documentation_md_file() items

    Organizational folders are not described in the documentation library.
    Organizational hierarchy must be extracted documentation_md_file() file paths
    '''

    def __init__(self):
        self.documentation_files = []

    # METHODS #

    def add_file(self, path: str, relative_root: str = '', enforce_extension = ''): # -> documentation_file: #TODO add type hinting for class back in
        '''
        Create a new documentation library file object
        :str path:              path to the file             
        :str relative_root:     common relative path to root of library files
        :str enforce_extension: only allow files of specified extension to be processed
                                '.ext' and 'ext' string formats are both supported
        
        :return bool:           True if file path existed and file object created 
        
        '''
        if check_file_exists(path):
            if (enforce_extension == '' or check_file_type(path, enforce_extension)):
                newFile = documentation_file(path, relative_root)
                self.documentation_files.append(newFile)              

        return newFile
    
    def add_folder(self):
        # TODO build in a structure (possibly a dictionary) that can represent folders and subfolders
        pass

    def get_on_disk_structure_tree(self) -> str:
        '''
        
        '''
        # TODO LATER
        # !!! This function is incomplete
        class treeItem():
            def __init__(self):
                depth = 0
                self.isDir = None
                self.name = None
                self.parent = None
                self.children = []

        for file in self.documentation_files:
            pass
        # !!! This function is incomplete

    def set_relative_path_for_library(self) -> bool:
        '''
        Look at all the documentation_file objects in the library, determine
        the common root path for all files, and then set the relative path
        for each file in the library by pruning out the common root


        :return:    True if proccess completes
        '''

        common_root = ''

        # Find coommon root directory across all files
        for doc in self.documentation_files:
            doc_path = doc.filepath_absolute
            current_branch = os.path.split(doc_path)[0]
            if common_root == '':
                common_root = current_branch
            else:
                # TODO there a much more dynamic method needed for determine
                # when this traverse arrives at the root/volume of the tree
                while doc_path.find(common_root) != 0:
                    common_root = os.path.split(common_root)[0]
                
        # Prune common root out of all document file paths to establish
        # relative paths
        for doc_path in self.documentation_files:
            doc_path.filepath_relative = doc_path.filepath_absolute.replace(common_root, "")

        return True
    
    def block_type_report(  self, block_type_str: str, 
                            report_all = False, 
                            include_context: bool = False,
                            print_report = False,
                            dump_to_file = False
                            ) -> dict:
        # TODO include_context currently provides no functionality
        '''
        Report all instances of a specific block type across the entire document
        library, organized per document file

        :str block_type_str:    block type to collect and report
        :bool report_all:       report all block types (ignore block_type_str)
        :bool include_context:  include text lines before and after block type
        
        :return:        dictionary of all blocks found per file
                        structure:
                            {
                            'count': total number of snippets
                            'files': all files found in library
                                [
                                    {
                                    'filepath': path to file
                                    'blocks': [list of block strings]
                                    }
                                ]
                            }
        
        '''
        found_blocks = {
                        'count': 0,
                        'files': []
                        }

        for doc in self.documentation_files:
            doc_filepath = doc.filepath_absolute
            doc_snippets = []
            
            for block in doc.text_blocks:
                if block.type.type == block_type_str.lower() or report_all:
                    found_blocks['count'] += 1
                    doc_snippets.append(block.text)

            found_blocks['files'].append({
                                        'filepath': doc_filepath,
                                        'blocks': list(doc_snippets)
                                        })
        
        # Generate report to print or dump to file
        if print_report or dump_to_file:
            datetime_now = datetime.datetime.now()

            indent = 5
            files_with_no_found_blocks = []

            if report_all:
                block_type_str = "All"

            report_to_print = f"REPORT FOR '{block_type_str.upper()}' BLOCKS FOUND"
            report_to_print += f"\nReport Generated: {datetime_now.strftime('%d %b %Y at %H:%M:%S')}"
            report_to_print += f"\n\nTotal Found Across All Files: {found_blocks['count']}\n"

            for report_item in found_blocks['files']:
                if len(report_item['blocks']) == 0:
                    files_with_no_found_blocks.append(report_item['filepath'])
                else:
                    snippet_count = 1

                    report_to_print += "\n" + "-"*20 + "\n"
                    report_to_print += f"File: {report_item['filepath']}\n"
                    report_to_print += f"Blocks: {len(report_item['blocks'])}\n"                    

                    for block in report_item['blocks']:
                        report_to_print += "\n"
                        report_to_print += " "*indent
                        report_to_print += f"{snippet_count}/{len(report_item['blocks'])}\n"

                        report_to_print += " "*indent
                        report_to_print += f"{block.replace('\n', ('\n' + ' '*indent))}"

                        snippet_count += 1
            
            if len(files_with_no_found_blocks) > 0:
                report_to_print += f"\nThe following files had no {block_type_str} blocks detected:"
                for zeroFile in files_with_no_found_blocks:
                    report_to_print += "\n" + " "*indent + zeroFile

            report_to_print += "\n\n--- END OF REPORT ---\n"

            if print_report:
                print(f"\n\n{report_to_print}")

            if dump_to_file:
                datetime_string = datetime_now.strftime("_%Y-%m-%d_at_%H-%M-%S")
                writeFile_name = f"documentation_{block_type_str}_block_report{datetime_string}.blockreport"
                writeFile = open(writeFile_name, mode = "w")
                
                writeFile.write(report_to_print)
                
                writeFile.close()
            
        return found_blocks


class documentation_file:
    '''
    Describe an entire single documentation .md file.
    The documentation file is composed of sequential documentation_block() blocks.
    
    :str path:              path to the file             
    :str relative_root:     common relative path to root of library files

    '''

    def __init__(self, path: str, relative_root: str = ''):
        self._filepath_absolute = None
        self._filepath_relative = None
        self.text_blocks = []

        if check_file_exists(path):
            self._filepath_absolute = path

            if relative_root != '':
                path = path.replace(relative_root, '')
            self._filepath_relative = path


    # PROPERTIES #

    @property
    def filepath_absolute(self):
        return self._filepath_absolute
    
    @filepath_absolute.setter
    def filepath_absolute(self, pathstring):
        if type(pathstring) == str:
            self._filepath_absolute = pathstring
        else:
            raise ValueError(f"{pathstring} is type {type(pathstring)}. Expected type str or None.")

    @property
    def filepath_relative(self):
        return self._filepath_relative
    
    @filepath_relative.setter
    def filepath_relative(self, pathstring):
        if type(pathstring) == str:
            self._filepath_relative = pathstring
        else:
            raise ValueError(f"{pathstring} is type {type(pathstring)}. Expected type str or None.")
    
    # METHODS #

    def parse_blocks_md(self) -> bool:
        '''
        parse a .md file into component blocks       
        '''
        md_file_types = [
                        '.md',
                        ]
        
        inside_markdown_block = '' # flag indicating inside a markdown block; value will be the string name of the block type

        if check_file_exists(self._filepath_absolute):
            if check_file_type(self._filepath_absolute, md_file_types):
                f = open(self._filepath_absolute, mode = 'r')
                collected_text = ''
                for line in f.readlines():
                    current_line_type = text_block_type.determine_type(line)
                    collected_text += line
                    
                    if current_line_type in list(text_block_type.markdown_block_types.keys()):
                        if inside_markdown_block == '':
                            # if we're entering a block, build the entire block before committing
                            inside_markdown_block = current_line_type
                        elif inside_markdown_block == current_line_type:
                            # if we're exiting a block, reset the markdown block to trigger it to be committed
                            inside_markdown_block = ''
                            
                    # commit text only when text block flag is closed
                    if inside_markdown_block == '':
                        new_text_block = text_block(collected_text)
                        new_text_block._type.set_type(collected_text)
                        self.text_blocks.append(new_text_block)

                        collected_text = ''

                # add any remaing text at end of file as text block
                if collected_text != '':
                    new_text_block = text_block(collected_text)
                    self.text_blocks.append(new_text_block)

                f.close()

        return True
    
    def get_file_type(self) -> str:
        '''
        return file type extension of file object
        '''

        return os.path.splitext(self._filepath_absolute)


class text_block:
    '''
    Describe a block of text in a text file.
    The text blocks are made up of text that represents paragraphs, headings, documentation or snippets
    Text blocks are assigned a text_block_type() type upon construction.
    '''
    def __init__(self, textStr: str):
        self._type = text_block_type()
        self._text = ''

        self.text = (textStr)
    
    # PROPERTIES #

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, textString: str) -> None:
        if type(textString) == str:
            self._text = textString
            self._type.set_type(textString)

        else:
            raise TypeError(f"Expected type 'str'. Received type '{type(textString)}'")

    @property
    def type(self):
        return self._type


class text_block_type:
    '''
    Establish the type of text_block based on the content of the text block
    '''

    # TODO there should probably be a more dynamic line-type detection algorithm in place than simply
    #  looking at the first letter of the first line of a text block.
    # TODO There's probably a more dynamic way to cover both allowed types, and the subset of multi line block types...
    allowed_types = {
                    # 'text' is the default type if no other type applies
                    # it is not designated in the allowed type list
                    '#': 'heading',
                    '_': 'separator',
                    '`': 'snippet',
                    }
    
    markdown_block_types = {
                            'snippet': '```',
                            }
    
    def __init__(self):
        self._type = None

    # PROPERTIES #

    @property
    def type(self) -> str:
        return self._type

    # METHODS #

    def set_type(self, string_to_type: str) -> bool:
        self._type = text_block_type.determine_type(string_to_type)
        return True

    def force_set_type(self, textString: str) -> bool:
        '''
        Force the type using a string type name value
        Should be used only when a starting text-block character is not available or qualified
            to indicate and set the text block type 
        '''
        if textString.lower() in list(text_block_type.allowed_types.values()):
            self.type = textString.lower()
        else:
            raise ValueError(f"'{textString}' is not a valid block type.  Expected: {text_block_type.allowed_types}")
        
        return True

    # STATIC METHODS #

    def determine_type(string_to_type: str) -> str:
        '''
        Determine and the type for a specific text block based on the
        starting character of the block

        :str string_to_type:    full string of the block to determine type for
        :return:                String indicating type
        '''

        typeString = None

        if type(string_to_type) == str:
            if len(string_to_type) == 0:
                typeString = 'text'
            elif string_to_type[0] in list(text_block_type.allowed_types.keys()):
                typeString = text_block_type.allowed_types[string_to_type[0]]
            else:
                # Anything not caught above will become flagged as text
                typeString = 'text'
        else:
            raise TypeError(f"'{string_to_type[0]}' is not a string. A single character string is required to match text block type.")
            
        return typeString

    def get_type_names() -> list:
        return list(text_block_type.allowed_types.values())
    
    def get_types_leading_characters() -> list:
        return list(text_block_type.allowed_types.keys())

    def get_non_text_types_leading_characters() -> list:
        types = list(text_block_type.allowed_types.keys())
        if '' in types:
            types.remove('')

        return types
        

# FUNCTIONS #

def check_file_exists(filepath: str) -> bool:
    '''
    replaces os.path.exists() to provide consistent Exception message when os.path.exists() is needed
    '''

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"'{filepath}' does not exist.")
    
    return True
    
def check_file_type(filepath: str, extension: List[str]) -> bool:
    '''
    validate that a file is of the desired type/extension

    :str filepath:      path to file
    :[str] extension:   list of representative extensions to validate in filepath
                        '.ext' and 'ext' are both acceptable formats for this string

    :return:            True if filepath is of type extension.  Otherwise raises Error.
    '''

    processed_extension_set = set()

    for ext in extension:
        if type(ext) != str:
            raise TypeError(f"Value '{ext}' is type {type(ext)}. Expected str.")
        else:
            processed_extension_set.add(ext.strip('.').lower())

    if os.path.splitext(filepath)[1].strip('.').lower() in processed_extension_set:
        return True
    else:
        raise TypeError(f"'{os.path.split(filepath)[1].lower()}' is not type: '{processed_extension_set}'")

# TESTING BLOCK #

def testing():
    pass

# MAIN # 

if __name__ == '__main__':

    file_directory = os.path.split(os.path.abspath(__file__))[0]

    docs = documentation_library()

    for item in os.walk(file_directory):
        for file in item[2]:
            if os.path.splitext(file)[1].lower() == '.md':
                newfile = docs.add_file(os.path.join(item[0], file))
                newfile.parse_blocks_md()

    docs.set_relative_path_for_library()
    
    snippet_report = docs.block_type_report(block_type_str = 'snippet', print_report = True, dump_to_file = True)

    print(os.path.abspath(__file__))