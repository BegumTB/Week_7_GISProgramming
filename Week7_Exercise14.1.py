from __future__ import print_function, division

def sed(pattern, replace, file1, file2):
    fin = open(file1, 'r')
    fout = open(file2, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
     

def main():
    pattern = 'pattern'
    replace = 'replace'
    file1 = 'words.txt'
    file2 = file1 + '.replaced' 
    sed(pattern, replace, file1, file2)

file1 = 'words.txt'
file2 = file1 + '.replaced'


if __name__ == '__main__':
    main()
else: 
    print ("Error!")


