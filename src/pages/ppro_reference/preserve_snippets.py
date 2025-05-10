'''

! WORK IN PROGRESS !

'''

import os
import pathlib
import shutil
from typing import List
import datetime
import difflib


# GLOBALS # 

g_current_datetime = datetime.datetime.now()

# CLASSES #

class documentation_library:
    '''
    Describe an entire cluster of documentation .md files
    The documentatation library is composed of documentation_md_file() items

    Organizational folders are not described in the documentation library.
    Organizational hierarchy must be extracted documentation_md_file() file paths
    '''

    def __init__(self):
        self.documentation_files = [] # files that will be processed
        self.supplemental_files = [] # files that will be copied without processing
        self._library_relative_path_root = ''

    # METHODS #

    def add_file(self, path: str, relative_root: str = '', enforce_extension = []): # -> documentation_file: #TODO add type hinting for class back in
        '''
        Create a new documentation library file object
        :str path:              path to the file             
        :str relative_root:     common relative path to root of library files
        :str enforce_extension: only allow files of specified extension to be processed
                                '.ext' and 'ext' string formats are both supported
        
        :return bool:           True if file path existed and file object created 
        
        '''
        if check_file_exists(path):
            newFile = documentation_file(path, relative_root)

            if (enforce_extension == [] or check_file_type(path, enforce_extension)):    
                self.documentation_files.append(newFile)
            else:
                self.supplemental_files.append(newFile)

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

        # Find common root directory across all files
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
                
        self._library_relative_path_root = common_root

        # Prune common root out of all document file paths to establish
        # relative paths

        # TODO why does this break with .DS_Store files?
        for docs in [self.documentation_files, self.supplemental_files]:
            for doc_path in docs:
                doc_path.filepath_relative = doc_path.filepath_absolute.replace(common_root, "")

        return True
    
    def block_type_report(  self, block_type_str: str, 
                            report_all = False, 
                            include_context: bool = False,
                            print_report = False,
                            dump_to_file = False
                            ) -> dict:
        # TODO include_context currently provides no functionality
        # TODO allow user to set dump file target location
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
            datetime_now = g_current_datetime

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
                datetime_string = g_current_datetime.strftime("_%Y-%m-%d_at_%H-%M-%S")
                writeFile_name = f"documentation_{block_type_str}_block_report{datetime_string}.blockreport"
                writeFile = open(writeFile_name, mode = "w")
                
                writeFile.write(report_to_print)
                
                writeFile.close()
            
        return found_blocks
    

    def detect_and_inherit_documentation_revisions(self, edited_docs) -> bool: # TODO typehinting for documentation object arguments
        '''
        Given a second documentation_library object which differs from the current
        documentation_library object (presumably with documentation and snipppet edits),
        detect where these differences exist and absorb any documentation additions into
        the current documentation_library object.

        In other words...
        merge changes (additions) in edited_docs into the existing documentation_library

        AKA...
        Merge all human-added stuff into the scraped documentation
        '''

        # Find matches based on filename
        filepairs = []
        target_orphans = [] # files in this documentation that appear to have no edited partner
        
        ### TODO very much incomplete
        current_pair = []
        for afile in edited_docs.documentation_files:
            for bfile in self.documentation_files:
                if afile.filepath_relative == bfile.filepath_relative:
                    pass

            if True:
                pass

    ## STATIC METHODS ##



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

    # TODO this is honestly pretty clunky with .type.type.  Change to .type_string here?
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

    :return bool:            True if filepath is of type extension.  Otherwise return False.
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
        return False

    
def determine_files_to_compare(
                            libraryA: documentation_library,
                            libraryB: documentation_library,
                            include_relpath_when_matching: bool = True
                            ):
    '''
    Considering two documentation libraries that need to be compared/merged, determine which files within each libraray
    match/correspond for comparison.  Each file should:
        • at most, have one file partner
        • any file that has more than one file partner on either side of the library cannot be compared
        • any file that has no partner identified in the other library is potentially new or omitted, and will be flagged
    
    :bool include_relpath_when_matching:    True will match files both by their filename and relative path within each library
                                            False will consider filename only when attempting to match files

    :return:    dictionary of partner/matching files between two libraries:
                {'matches': [[fileA, fileB],...], 'non_matchesA': [Afile1, Afile2,...], 'non_matchesB': [Bfile1, Bfile2,...], 'multiples': [[filepath1, filepath2,...],...]}
    '''
    matches = []
    non_matchesA = []
    non_matchesB = []
    multiples = {} # {filename: {set of documentation_file objects},..}

    file_listA = list(libraryA.documentation_files)
    file_listB = list(libraryB.documentation_files)

    # Prune out duplicates if they exist
    # Theoretically, no duplicates can exist if filepaths are considered since
    # this would break filesystem conventions
    # 
    # TODO 
    # This section may be incomplete and also totally worthless and worth removing
    # It occurrs to me after writing this that the documentation contains many
    # index.md files, which will all trigger as duplicates, which would very much
    # prevent any documenation automated management from operationg.  Thus, relative
    # paths may ALWAYS be required, and make matching on filename alone moot
    if not include_relpath_when_matching:
        indices_to_removeA = set()
        indices_to_removeB = set()


        filenamesA = [os.path.split(x.filepath_absolute)[1] for x in file_listA]
        filenamesB = [os.path.split(x.filepath_absolute)[1] for x in file_listB]

        # detect and log duplicate file objects
        for filelist in [file_listA, file_listB]:
            for file in filelist:
                filename = os.path.split(file.filepath_absolute)[1]

                if (
                    (filenamesA.count(filename) > 1 and filenamesB.count(filename) > 0) or
                    (filenamesB.count(filename) > 1 and filenamesA.count(filename) > 0)
                    ):
                    if filename in multiples.keys():
                        multiples[filename].add(file)
                    else:
                        multiples[filename] = {file}

        # log and pop indices from file lists so they are not evaluated below
        for index in range(0, len(file_listA)):
            filename = os.path.split(file_listA[index].filepath_absolute)[1]
            if filename in multiples.keys():
                indices_to_removeA.add(index)

        for index in range(0, len(file_listB)):
            filename = os.path.split(file_listB[index].filepath_absolute)[1]
            if filename in multiples.keys():
                indices_to_removeB.add(index)

        indices_to_removeA = list(indices_to_removeA)
        indices_to_removeA.sort(reverse=True)
        for index in indices_to_removeA:
            file_listA.pop(index)

        indices_to_removeB = list(indices_to_removeB)
        indices_to_removeB.sort(reverse=True)
        for index in indices_to_removeB:
            file_listB.pop(index)

    # find matching files between A and B
    for pointerA in range(0, len(file_listA)):
        for pointerB in range(0, len(file_listB)):
            pathA = file_listA[pointerA].filepath_relative
            pathB = file_listB[pointerB].filepath_relative

            if pathA == pathB:
                matches.append([file_listA[pointerA], file_listB[pointerB]])
                file_listB.pop(pointerB)
                break

            # If no B match after all B paths have been examined, log A path as non-matched
            if pointerB == len(file_listB) - 1:
                non_matchesA.append(file_listA[pointerA])
    
    non_matchesB = file_listB

    return {
        'matches': matches,
        'non_matchesA': non_matchesA,
        'non_matchesB': non_matchesB,
        'multiples': multiples
    }




def determine_docfile_alignment(
                            docfileA: documentation_file, 
                            docfileB: documentation_file, 
                            confidence_threshold: float = 1.0,
                            assume_newline_follows_additions: bool = True
                            ) -> List:
    '''
    Compare two documentation_file objects and determine their alignment:  Where they are the same, where they are
    different, and where they match back up when differences are encounterd.

    :documentation_file docfileA:           representation of text file, likely edited by user, to read new edits from
    :documentation_file docfileB:           representation of text file, likely unedited, to merge user edits into
    :float confidence_threshold:            confidence threshold beyond which two compared lines of text should be considered as matching
                                            this is a float from 0.0 - 1.0 representing a percentage of confidence
    
    :return:            List demonstrating line alighment, formatted as:
                            [{
                            'fileorder': [documentation_file_1, documentation_file_2],
                            'line_index_aligmnent: [[documentation_file_1_line_index, documentation_file_2_line_index],..]
                            }]

                        Details:
                            fileorder: contains full documentation_file objects that can be referenced
                            line_index_alignment: A list of sublists, where each sublist indicates two indices that represent
                                a matching line string across two files.  Index order of each list item corresponds to the 
                                order of the items in fileorder, i.e. the first index in the sublist matches to a line number
                                index of the first file object in fileorder; the second index in the sublist matches to the
                                line number index of the second file object in fileorder.

                                An index of -1 indicates that there was no line match found.  For example, an index pair
                                of [10, -1] indicates that line 10 from documentation_file_1 had no match in documentation_file_2

    '''
    line_alignment = {
                'fileorder': [docfileA, docfileB], 
                'line_index_alignment': []
                }
    line_orphansA = [] # lines found only in Doc A, not in Doc B
    line_orphansB = [] # lines found only in Doc B, not in Doc A
    
    numlinesA = len(docfileA.text_blocks)
    numlinesB = len(docfileB.text_blocks)

    currentlineA_index = 0 # current comparison line in Doc A
    currentlineB_index = 0 # current comparison line in Doc B

    pointerA_index = 0 # traverse pointer in Doc A
    pointerB_index = 0 # traverse pointer in Doc B

    while currentlineA_index < numlinesA and currentlineB_index < numlinesB:
        # Traverse all lines in A and B, looping through all unmatched B lines for each A line,
        # until matches are found or all A lines are exhausted

        currentlineA = docfileA.text_blocks[pointerA_index]
        currentlineB = docfileB.text_blocks[pointerB_index]

        currentlineA_string = docfileA.text_blocks[pointerA_index].text #TODO remove
        currentlineB_string = docfileB.text_blocks[pointerB_index].text #TODO remove

        if pointerB_index == 203:
            abc = 10 # DEBUG_DELETE

        # start with the first line in A and B
        if (
            # If current lines match, log matching lines, and all A/B lines that were skipped while finding a match

            # TODO Put more robust line equality evaluator function call here, and build line comparitor function!
            do_text_blocks_match(currentlineA, currentlineB) >= confidence_threshold
            # currentlineA_string.strip() == currentlineB_string.strip()
        ):
            
            # log the matching A == B line
            line_alignment['line_index_alignment'].append([
                [pointerA_index, pointerB_index], 
                [docfileA.text_blocks[pointerA_index].text, docfileB.text_blocks[pointerB_index].text]
                ])
            
            # if we've been skipped a bunch of lines in A or B, and now found a match, log the skipped lines lines
            while pointerA_index > currentlineA_index:
                line_alignment['line_index_alignment'].append([
                    [currentlineA_index, -1],
                    [docfileA.text_blocks[currentlineA_index].text, ""]
                ])
                currentlineA_index += 1

            while pointerB_index > currentlineB_index:
                line_alignment['line_index_alignment'].append([
                    [-1, currentlineB_index], 
                    ["", docfileB.text_blocks[currentlineB_index].text]
                    ])
                currentlineB_index += 1
            
            # Increment the pointers and update the current line index to match
            pointerA_index += 1
            pointerB_index += 1

            currentlineA_index = pointerA_index
            currentlineB_index = pointerB_index
        else:
            # If lines don't match, move to B pointer
            pointerB_index += 1

        if pointerB_index >= numlinesB and currentlineA_index < numlinesA:
            # if all B lines have been checked against the current A line with no match, log the A line as unmatched
            line_alignment['line_index_alignment'].append([
                [currentlineA_index, -1],
                [docfileA.text_blocks[currentlineA_index].text,""]
            ])

            pointerA_index += 1
            currentlineA_index = pointerA_index

            # If the current A line is unmatched and we assume all additions are followed by newlines,
            # log the newline right away if it follows the logged A line
            if (
                assume_newline_follows_additions
                ): 
                # If the current A line is an addition, and not simply a blank newline,
                # we check to see if corresponding newlines already exist to follow the added line.
                # Consideration is added here for A and B pointers being the last line of the file, in which case
                # checking for existing corresponding newlines will cause an INDEX OUT OF RANGE error.

                # If B lines still remain, we want to check if it's a newline.  If no lines remain, we have nothing to check
                b_line_not_newline = True
                if (currentlineB_index < numlinesB and docfileB.text_blocks[currentlineB_index].text == "\n"):
                    b_line_not_newline = False

                # Validate that a corresponding A newline exists that is not matched on the B side
                if (
                    docfileA.text_blocks[currentlineA_index-1].text != "\n" and # line addition found was not a newline
                    currentlineA_index < numlinesA and # line after found addition exists
                    docfileA.text_blocks[currentlineA_index].text == "\n" and # line after found line is a newline
                    b_line_not_newline # next line on B side is not a newline 
                    ):

                    line_alignment['line_index_alignment'].append([
                        [currentlineA_index, -1],
                        [docfileA.text_blocks[currentlineA_index].text,""]
                    ])

                    pointerA_index += 1
                    currentlineA_index = pointerA_index
                
            pointerB_index = currentlineB_index

        # if pointerA_index >= numlinesA and currentlineA_index < numlinesA:
        #     # If a given A line returns no B line match during an entire traverse pass, log it as no parther
        #     line_alignment['line_index_alignment'].append([
        #         [currentlineA_index, -1],
        #         [docfile_to_read.text_blocks[currentlineA_index].text,""]
        #         ])
            
        #     # line_orphansA.append(currentlineA)
        #     # line_orphansB.append(currentlineB)

        #     currentlineA_index += 1
        #     pointerA_index = currentlineA_index

        #     pointerB_index = currentlineB_index + 1

        if currentlineA_index >= numlinesA and currentlineB_index < numlinesB:
            # If all A lines have been traversed and B lines remain, log them at the end of the list
            while currentlineB_index < numlinesB:
                line_alignment['line_index_alignment'].append([
                        [-1, currentlineB_index], 
                        ["", docfileB.text_blocks[currentlineB_index].text]
                        ])
                # line_orphansB.append(currentlineB)

                currentlineB_index += 1
                pointerB_index = currentlineB_index # TODO likely not necessary

    return line_alignment

def do_text_blocks_match(
        blockA: text_block, 
        blockB: text_block, 
        require_block_type_match: bool = False) -> float:
    '''
    Determine if two text blocks (lines) match based off of a series of factors 

    :text_block blockA:  string to compare
    :text_block blockB:  string to compare
    :bool check_block_type: True will validate block type between two text_block object arguments
                            False will ignore the text block type of two block arguments

    :return:    float value representing percentage of matching confidence
    '''

    confidence = None
    confidences_to_average = []

    if require_block_type_match and (blockA.type.type != blockB.type.type):
        confidence = 0
    elif blockA.text.strip() == blockB.text.strip():
        confidence = 1.0
    else:
        # setup for diff between two lines # number of words in A vs B, expressed as a ration min/max
        blockA_words = blockA.text.split()
        blockB_words = blockB.text.split()
        
        blockA_words_stripped = [i.strip() for i in blockA_words]
        blockB_words_stripped = [i.strip() for i in blockB_words]

        D = difflib.Differ()
        lines_diff = D.compare(blockA_words_stripped, blockB_words_stripped)
        stripped_lines_diff = D.compare(blockA_words_stripped, blockB_words_stripped)

        lines_diff_result = [i for i in lines_diff]
        stripped_lines_diff_result = [i for i in stripped_lines_diff]

        # Multiple diff-related checks - setup
        words_unchanged = []
        words_added = 0
        words_removed = 0

        unchanged_sections = 0
        changed_sections = 0

        len_changed_chars_for_ratio = 0
        len_unchanged_chars_for_ratio = 0

        lastline_prefix = ""
        for word in lines_diff_result:
            if word[0:2] == "  ":
                words_unchanged.append(word)
                len_unchanged_chars_for_ratio += len(word) - 2
            elif word[0:2] == "+ ":
                words_added += 1
                len_changed_chars_for_ratio += len(word) - 2
            elif word[0:2] == "- ":
                words_removed += 1
                len_changed_chars_for_ratio += len(word) - 2

            if lastline_prefix != " " and word[0] == " ":
                unchanged_sections += 1
            elif lastline_prefix not in ("+", "-") and word[0] in ("+", "-"):
                changed_sections += 1
            
            if word[0] != "?":
                lastline_prefix = word[0]


        #   is diff ONLY additions?  If so, assume no conflicts and do not evaluate confidence
        if require_block_type_match and blockA.type.type != blockB.type.type:
            confidence = 0
        else:            
            if (
                words_added > 0 and words_removed == 0 and
                len(blockA_words) > 0 and len(blockB_words) > 0
                ):
                confidence = 1
            else:
                #   number of words in A vs B, expressed as a ration min/max
                if len(blockA_words) == 0 or len(blockB_words) == 0:
                    confidences_to_average.append(0)
                else:
                    words_ratio = min(len(blockA_words), len(blockB_words))/max(len(blockA_words), len(blockB_words))
                    confidences_to_average.append(words_ratio)

                #   percentage of the line that has changed
                if len_changed_chars_for_ratio == 0:
                # if len(blockA_words) == 0:
                    confidences_to_average.append(0)
                else:
                    # unchanged_ratio = len(words_unchanged)/len(blockA_words)
                    unchanged_ratio = len_unchanged_chars_for_ratio/len_changed_chars_for_ratio
                    confidences_to_average.append(unchanged_ratio)              

                # if block types don't match, this contributes to lower confidence
                # matching block type does not contibute to higher confidence
                if blockA.type.type != blockB.type.type:
                    confidences_to_average.append(0)

                # Calculate evenly weighted confidence average
                if len(confidences_to_average) > 0:
                    confidence = sum(confidences_to_average)/len(confidences_to_average)
                else:
                    confidence = 0

                # TODO not sure exactly how to unevenly weight confidence
                #   Is this a user defined thing?
                #   Is that even necessary?

    '''
    Items to check for determining confidence:

    - [√] number of words in A vs number of words in B
    - [√] percentage of the line that has been diffed
    - [x] number of diff sections vs non-diff sections (more sections = higher variablilty) - not sure this actually suggest anything valuable
    - [x] are one of the adjacent diff sections inside the other (singular plural correction) - this is kinda caught by num words in A vs B.  If ONLY singular/plural changes, num words is the same
    - [√] is diff only additions? (seems like a merge)
    - [ ] are there significant words in common between A and B suggesting line similarity (other than common words like "the")
    - [√] is line type the same
    - [ ] is the line before and after the same in both A and B (suggest line replacement)
    '''

    return confidence

def write_merged_library(
                    aligned_library_list: list, 
                    destination: str,
                    original_libraryA: documentation_library,
                    original_libraryB: documentation_library,
                    ) -> bool:
    '''
    TODO comments
    '''

    # Build new root folder to inject into destination for current write pass
    datetime_tag = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    foldername = "exported_docs_library"
    combined_foldername = f"{foldername}_{datetime_tag}"

    # Build the folders and write the files
    for item in aligned_library_list:
        if not os.path.exists(destination):
            raise FileNotFoundError(f"Target destination {destination} does not exist.")
        else:
            # FIXME this is the part where the filepath is extracted from the alignment array
            # This will likely be more functional as a class instead of an array
            relpath = item['fileorder'][0].filepath_relative.strip(os.sep)

            file_writepath = os.path.join(destination, combined_foldername, relpath)
            if os.path.exists(destination):
                makedirs_for_file(file_writepath)

                # FIXME This is the part where the file is re-written from the alignment array
                # This will liekly be more functinoal as a class instead of an array
                writefile = open(file_writepath, mode = "w")
                for line in item['line_index_alignment']:
                    if line[0][0] == -1:
                        writefile.write(line[1][1])
                    elif line[0][1] == -1:
                        writefile.write(line[1][0])
                    else:
                        writefile.write(line[1][1])
            else:
                raise FileNotFoundError(f"Target root path does not exist: {destination}")

    # copy over supplemental files

    for library in [original_libraryA, original_libraryB]:
        for file in library.supplemental_files:
            src_filepath = file.filepath_absolute
            src_relpath = file.filepath_relative.strip(os.sep)

            if os.path.exists(src_filepath):
                shutil.copy(src_filepath, os.path.join(destination, combined_foldername, src_relpath))
            else:
                raise FileNotFoundError(f"File to copy does not exist: {src_filepath}.")
        
        # TODO add logging and reporting for which supplemental files were copied/skipped

    # TODO add handling for file non-matches, multiples

    return True

def makedirs_for_file(filepath: str):
    '''
    Make all directories in path leading to file, if they don't exist

    Tries to detect if a filename is included at the end of a filepath, or if the provided path
    is a parent path with no file.

    
    :str filepath:  Path to validate exists, and creaet if it does not.  May or may not contain \
                    a file at the end of the path.
    '''

    split_path = os.path.split(filepath)
    last_item_ext_split = os.path.splitext(split_path[-1])
    
    try:
        if last_item_ext_split[1] != "" and last_item_ext_split[1][0] == ".":
            filepath = os.path.split(filepath)[0]
    except Exception as e:
        raise TypeError(f"List components did not match expected split path item: {last_item_ext_split}.  Error: {e}")
    # TODO would be helpful to have skip or error reporting logic rather than raising an exception

    pathlib.Path(filepath).mkdir(parents=True, exist_ok=True)

    return True


# TESTING BLOCK #

def testing():
    pass

# MAIN # 

if __name__ == '__main__':

    # TODO Add CLI

    '''
    TODO If run from the root folder of the documentation, the below path variable will traverse the documentation
    correctly. This should be a CLI option so that users can define their own "source" documentation library, or
    use the existing one here.  May need checks in place so that, if this .py file is moved to a new location, it does
    not traverse non-documentation files 
    '''

    '''
    TODO Read in documentation library should be a method, not main body functionality.
    '''

    # edited_docs_root_dir = os.path.split(os.path.abspath(__file__))[0]
    # edited_docs_root_dir = '/Users/binsler/Desktop/250428_Dan McS Documentation Edits_MINI/ppro_reference'
    edited_docs_root_dir = '/Users/binsler/Desktop/20250508_debugging_trim_docs/Existing_Public_Docs/ppro_reference'

    # new_scrape_root_dir = '/Users/binsler/Desktop/250428_Raw_Scrape_MINI/ppro_reference'
    new_scrape_root_dir = '/Users/binsler/Desktop/20250508_debugging_trim_docs/Scrape_from_Cathy/ppro_reference'

    library_write_root = '/Users/binsler/Desktop/20250508_debugging_trim_docs/_New_Combined_Docs'

    edited_docs = documentation_library()

    for item in os.walk(edited_docs_root_dir):
        for file in item[2]:
            newfile = edited_docs.add_file(
                                    path = os.path.join(item[0], file),
                                    enforce_extension = ['.md']
                                    )
            if os.path.splitext(file)[1].lower() == '.md':
                newfile.parse_blocks_md()

    edited_docs.set_relative_path_for_library()


    scraped_docs = documentation_library()

    for item in os.walk(new_scrape_root_dir):
        for file in item[2]:
            newfile = scraped_docs.add_file(
                                path = os.path.join(item[0], file),
                                enforce_extension = ['.md']
                                )
            if os.path.splitext(file)[1].lower() == '.md':
                newfile.parse_blocks_md()

    scraped_docs.set_relative_path_for_library()

    compare_list = determine_files_to_compare(edited_docs, scraped_docs)

    aligned_list = []
    for file in compare_list['matches']:
        aligned = determine_docfile_alignment(
                                file[0],
                                file[1], 
                                confidence_threshold=.7
                                )
    
        aligned_list.append(aligned)

        '''
        stop here
        '''

    write_merged_library(aligned_list, library_write_root, edited_docs, scraped_docs)
    

    # for item in scraped_docs.documentation_files:
    #     newpath = os.path.join(library_write_root, item.filepath_relative.strip(os.sep))
    #     if os.path.exists(library_write_root):
    #         makedirs_for_file(newpath)
    #     else:
    #         raise FileNotFoundError(f"Target root path does not exist: {library_write_root}")

    # aligned = determine_docfile_alignment(
    #                         edited_docs.documentation_files[0],
    #                         scraped_docs.documentation_files[0], 
    #                         confidence_threshold=.7
    #                         )

    
    snippet_report = edited_docs.block_type_report(block_type_str = 'snippet', print_report = True, dump_to_file = False)

    print(os.path.abspath(__file__))