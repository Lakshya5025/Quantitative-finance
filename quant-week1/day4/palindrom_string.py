strings = [
    "madam",
    "racecar",
    "hello",
    "python",
    "level",
    "world",
    "radar",
    "kayak",
    "reviver",
    "openai",
    "noon",
    "civic",
    "rotor",
    "refer",
    "chatgpt",
    "banana",
    "malayalam",
    "aibohphobia",
    "programming",
    "stats",
    "tenet",
    "mom",
    "dad",
    "pop",
    "wow",
    "deified",
    "algorithm",
    "developer",
    "college",
    "engineer",
    "solos",
    "data",
    "science",
    "repaper",
    "abcdcba",
    "abccba",
    "computer",
    "keyboard",
    "mouse",
    "india",
    "neveroddoreven",
    "javascript",
    "django",
    "react",
    "swift",
    "hannah",
    "anna",
    "cplus",
    "909",
    "121",
    "12321",
    "12345",
    "1001",
    "999",
    "abcba",
    "abcd",
    "notapalindrome",
    "palindrome",
    "rotator",
    "bob",
    "eve",
    "civiccar",
    "palindrometest",
    "stack",
    "queue",
    "linkedlist",
    "binarytree",
    "machinelearning",
    "datastructure",
    "networking",
    "computergraphics"
]



for str in strings:
    start = 0
    end = len(str) - 1
    flag = True
    while(start < end):
        if(str[start] != str[end]):
            flag = False
            break
        start += 1
        end -= 1
    print(f"{str}: {flag}")
    
        