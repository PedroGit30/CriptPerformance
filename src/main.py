from encryption import algo
import random
import timeit
import os
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

# for private key generation
PUBLIC_EXPONENT = 65537
KEY_SIZE        = 2048

algo.rsa_generate_keys(PUBLIC_EXPONENT,KEY_SIZE)

# number of runs
N_TIMES         = 5000 


sizes_input_text = [    
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
    2047152,
]

algorithms = [
    ("aes_256_ctr_encrypt","aes_256_ctr_decrypt",lambda t,f : f(t[0],t[1],t[2]),[8,64,512,4096,32768,262144,2047152]),
    ("rsa_encrypt","rsa_decrypt",lambda x,f : f(x),[2,4,8,16,32,64,128]),
    ("sha256","","",[8,64,512,4096,32768,262144,2047152])
]

# size is the number of bytes in the string
def get_random_utf_8_bytes(size : int) -> bytes :

    # utf-8 table :
    #   https://www.utf8-chartable.de/
    include_ranges = [
        #basic latin table exept controls
        ( 0x0020, 0x0026 ), 
        ( 0x0028, 0x007E ), 
        ( 0x00A1, 0x00AC ), 
        ( 0x00AE, 0x00FF ), 
        #Latin Extended-A full table
        ( 0x0100, 0x017F ),
        #Latin Extended-B full table
        ( 0x0180, 0x024F ),
        #Latin Extended-C full table
        ( 0x2C60, 0x2C7F ),
        # Runic symbols
        ( 0x16A0, 0x16F0 ),
        # Greek and Coptic
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C )
    ]

    alphabet = []
    randomString = ""
    current_size = 0

    for (fromCode,toCode) in include_ranges :        
        for i in range(fromCode,toCode) :
            alphabet.append(i)
        #alphabet.append(0x000A) #increase probability of line breaks
    
    # add utf-8 character until current_size <= size
    while current_size < size :        
        code = random.choice(alphabet)
        new_size = current_size + len(chr(code).encode('utf-8')) 

        if new_size > size : 
            break
        else :
            randomString += chr(code)
            current_size = new_size
    
    # chose ascii characters to add to end in order to 
    # have the desired size
    while current_size < size :
        code = random.randint(32,126)
        randomString += chr(code)
        current_size += 1

    return bytes(randomString,'utf-8')

def readFile(file) :
    f = open(file,'rb')
    data = f.read()
    f.close()
    return data

def test(generateFiles=False) : 

    spaces_betwen = 10
    legend_start = 2.5
    xs = [ x for x in range(0,len(sizes_input_text)*spaces_betwen,spaces_betwen) if True ]
    counter = 0

    for (encrypt,decrypt,fun,interval) in algorithms :

        print(f'\n{ encrypt.replace("_encrypt","") + f" (number of runs = {N_TIMES})" } : \n')

        print("*" * 96)
        print(f"|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |")
        
        ys1 = [] # y axis for encryption times
        ys2 = [] # y axis for decryption times

        for size in sizes_input_text :            
            t1 = 0
            t2 = 0

            if size in interval :    

                if generateFiles : 
                    text = get_random_utf_8_bytes(size)
                else : 
                    text = readFile(f"{dir_path}/../text/{size}b.txt")

                if decrypt == "" :
                    t1 = timeit.timeit(f'algo.{encrypt}(text)',number=N_TIMES,globals= {'algo':algo ,'text' : text})

                else :                
                    output = [()]

                    for _ in range(N_TIMES) :
                        t1 += timeit.timeit(f"output[0] = algo.{encrypt}(text)",number=1,globals= {'algo':algo ,'text' : text,'output':output})                                        
                        t2 += timeit.timeit(f"fun(output[0],algo.{decrypt})",number=1,globals= {'algo':algo ,'fun' : fun,'output':output})

                    # t1 = timeit.timeit(f"output.append(algo.{encrypt}(text))",number=N_TIMES,globals= {'algo':algo ,'text' : text,'output':output})                                        
                    # t2 = timeit.timeit(f"fun(output.pop(0),algo.{decrypt})",number=N_TIMES,globals= {'algo':algo ,'fun' : fun,'output':output})               

                    # output = getattr(algo,encrypt)(text)
                    # t1 = timeit.timeit(f"algo.{encrypt}(text)",number=N_TIMES,globals= {'algo':algo ,'text' : text})                                                        
                    # t2 = timeit.timeit(f"fun(output,algo.{decrypt})",number=N_TIMES,globals= {'algo':algo ,'fun' : fun,'output':output})               

            ys1.append((t1 / N_TIMES) * 1000000) 
            ys2.append((t2 / N_TIMES) * 1000000) 
            t1 = '{:.4f}'.format( (t1 / N_TIMES) * 1000000 ) if t1 != 0 else "  --  "
            t2 = '{:.4f}'.format( (t2 / N_TIMES) * 1000000 ) if t2 != 0 else "  --  "           
            col1 = "|" + (" " * 8) + f"{size}" + (" " * ( 13 - len(str(size)) )) + "|"
            col2 = (" " * 13) + t1 + (" " * ( 23 - len( str(t1) ) ) ) + "|"
            col3 = (" " * 12) + t2 + (" " * ( 23 - len( str(t2) ) ) ) + "|"            
            print(col1 + col2 + col3)


        print("*" * 96)                             
        plt.bar([ x+counter for x in xs if True ],ys1,width=0.8,label=encrypt)
        plt.bar([ x+counter+1 for x in xs if True ],ys2,width=0.8,label=decrypt)
        counter += 2

    tick_label = ["2b","4b","8b","16b","32b","64b","128b","512b","4096b","32768b","262144b","2047152b"]

    for size in sizes_input_text :        
        plt.bar([x + legend_start for x in xs if True ],[0]*len(xs),tick_label=tick_label)
    
    plt.ylabel("avg time per run (μs)")
    plt.xlabel("size of file (bytes)")
    plt.legend()
    plt.show()


print("\n-------------STATIC TEXT FILES-------------")
plt.title(f"Static text encryption and decryption performance measures (number of runs = {N_TIMES})")
test()
print("\n-------------GENERATED TEXT FILES-------------")
plt.clf()
plt.title(f"Generated text encryption and decryption performance measures (number of runs = {N_TIMES})")
test(generateFiles=True)
