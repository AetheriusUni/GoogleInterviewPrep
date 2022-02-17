# returns name and phone number
def phoneNumberLookUp(phonebook, query):
    for key in phonebook:
        if key == query:
            return f"{key}={phonebook[key]}"
    return "Not found"

if __name__ == '__main__':
    n = int(input())
    namesAndNumbers = []
    phonebook = {}
    for i in range(n):
        ele = input().split()
        namesAndNumbers.append(ele)
    for key, val in namesAndNumbers:
        phonebook[key] = val
    done = False
    while True:
        try:
            query = input()
            if query != 'done':
                print(phoneNumberLookUp(phonebook, query))
        except:
            break
