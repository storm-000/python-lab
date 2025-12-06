file = str(input("\n Enter the file name : \n"))

with open(file, "r") as src:
    content = src.read()
    
    words = content.split()
    no_of_words = len(words)
    print(f"No of words : {no_of_words}")
    
    lines = content.splitlines()
    line_count = len(lines)
    print(f"No of lines : {line_count}")