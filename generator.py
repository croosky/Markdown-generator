import sys

STOP_LINE = '\n[comment]: <> (Stop)\n'

class Solution:
    def __init__(self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link = link.rstrip('\n')
        self.code = code

    def get_title(self):
        return f'## {self.title}'

    def get_contents(self):
        return f'+ [{self.title}](#{self.link[30:-1]})\n{STOP_LINE}'

    def get_code(self):
        code_lines = '\n'.join(map(lambda x: x.strip('\n')[4:], self.code))
        return f'``` python\n{code_lines}\n```'

    def get_solution(self):
        return f'{self.get_contents()}\n{self.get_title()}\n\n{self.link}\n\n{self.get_code()}'

def read_all_lines(filename):
    file = open(filename)
    result = file.readlines()
    file.close()
    return result

def write_to_md(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()

def read_all_file(filename):
    file = open(filename)
    result = file.read()
    file.close()
    return result

def merge(old, new):
    old_parts = old.split(STOP_LINE)
    new_parts = new.split(STOP_LINE)
    if len(old_parts) == 1:
        return f'{new}'
    return f'{old_parts[0]}{new_parts[0]}{STOP_LINE}{old_parts[1]}{new_parts[1]}'

def main(in_file,out_file):
    in_txt = read_all_lines(in_file)
    source = Solution(in_txt[0], in_txt[1], in_txt[3:])
    new = source.get_solution()
    old = read_all_file(out_file)
    result = merge(old, new)
    write_to_md(out_file, result)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])