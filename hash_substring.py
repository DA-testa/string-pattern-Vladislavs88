# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    teksts=input().strip()
    if "F" in teksts:
        with open("tests/06") as file:
            teksts1=file.readline().rstrip()
            teksts2=file.readline().rstrip()
    if "I" in teksts:
        teksts1=input().rstrip()
        teksts2=input().rstrip()
    else:
        print("wrong command")
        return
    return teksts1,teksts2
        
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
#     return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(teksts1, teksts2):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return [i for i in range(len(teksts2)-len(teksts1)+1)if teksts2[i:i+len(teksts1)]==teksts1]


# this part launches the functions
if __name__ == '__main__':
    teksts3=get_occurrences(*read_input())
    print_occurrences(teksts3)


