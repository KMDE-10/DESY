def gather_files_regex(dir: str, regex) -> list:
    '''
    Gathers all files below a directory that match the provided regular expression
    Traverses into sub-directories

    dir -- the directory

    regex -- A regular expression to match filenames
    '''
    #
    import re
    import os
    subdir = dir
    p = re.compile(regex)
    data = []
    for dir, _, files in os.walk(subdir):
        for name in files:
            if p.match(name):
                b = (str(os.path.join(dir, name)))
                data.append(b)

    return data