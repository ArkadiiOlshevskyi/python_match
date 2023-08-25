import os
# matching the format of file and printing it on terminal
# in repo we have all except txt file and one unknown file


def file_format_match(file_format):
    match file_format:
        case 'csv':
            print(f"this is CSV file")
        case 'json':
            print(f"this is JSON file")
        case 'xml':
            print(f"this is XML file")
        case 'txt':
            print(f"this is txt file")
        case 'yml':
            print(f"this is yml file")
        case _:
            print(f"unknown file format")       # we have for this one jpeg file in folder


def main():
    path = "R:/0_tech/git_repo/python_match/data/"     # use or local repo path for files
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            file_extension = filename.split('.')[-1]
            print(f"Checking format for file: {filename}")
            file_format_match(file_extension)
            print()


if __name__ == '__main__':
    main()
