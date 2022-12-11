"""
Input changes:
- add new line '\n' to the last line
"""

class FileSystem:
    
    def __init__(self):
        self.root_dir = Directory(None)
        self.current_dir = self.root_dir

    def back(self):
        self.current_dir = self.current_dir.parent
    
    def cd(self, dir_name):
        self.current_dir = self.current_dir.dirs[dir_name]

    def add_dir(self, dir_name):
        self.current_dir.dirs[dir_name] = Directory(self.current_dir)
    
    def add_file(self, file_name, size):
        self.current_dir.files.append(File(int(size)))

    def part1(self):
        self.root_dir.get_size()
        return self.root_dir.part1(0)

    def part2(self):
        fs_size = self.root_dir.get_size()
        treshold = 30000000 - (70000000 - fs_size)
        return self.root_dir.part2(0, treshold)


class Directory:

    def __init__(self, parent):
        self.parent = parent
        self.dirs = {}
        self.files = []
        self.size = 0

    def get_size(self):
        if self.size == 0:
            result = sum([f.size for f in self.files])
            for dir in self.dirs.values():
                result += dir.get_size()
            self.size = result
        return self.size
        

    def part1(self, result):
        if (self.size < 100000):
            result += self.size
        for dir in self.dirs.values():
            result = dir.part1(result)
        return result
    
    def part2(self,result,treshold):
        if (self.size > treshold and abs(treshold - self.size) < abs(treshold - result)):
            result = self.size
        for dir in self.dirs.values():
            result = dir.part2(result, treshold)
        return result


class File:
    def __init__(self, size):
        self.size = size


def main():
    data = open('07data.txt','r')
    fs = FileSystem()
    data.readline()  # skip first line: "$ cd /"
    # Load FileSystem into the memory
    for line in data:
        if line.startswith('$ ls'):
            content = data.readline()
            while not(content.startswith('$')) and content != '':
                param1,param2 = content.split(' ')
                param2 = param2[:-1] # remove '\n' from the name 
                if param1 == 'dir':
                    fs.add_dir(param2)
                else:
                    fs.add_file(param2,param1)
                content = data.readline()
            line = content
        if line.startswith('$ cd ..'):
            fs.back()
        elif line.startswith('$ cd'):
            _,_,dir = line.split(' ')
            fs.cd(dir[:-1])  # remove '\n' from dir name 
    # Compute values
    print(fs.part1())
    print(fs.part2())
    
    

if __name__ == '__main__':
    main()

# brak pustych dir