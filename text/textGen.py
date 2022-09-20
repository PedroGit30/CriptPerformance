import os

sizes = [
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    512,
    4096,
    32768,
    262144,
    2047152
]

def createFiles() :    

    for s in sizes :
        os.system(f'head -c {s} big.txt > {s}b.txt')
        
createFiles()