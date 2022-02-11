def string_splosion(str):
    strParts = ''
    rString = ''
    for i in range(len(str)):
        strParts+=str[i]
        rString+=strParts
    return rString

if __name__ == '__main__':
    inString = input()
    print(string_splosion(inString))
