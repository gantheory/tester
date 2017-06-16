import os
from colorama import Fore

home = os.path.expanduser('~')

def main():
    print(Fore.RED + "\n      ADD TEST" + Fore.WHITE)
    contestCode = 0
    problemCode = ord(input("Problem Code: ")) - ord('A')

    path = os.path.join(home + '/Github/tester/result.txt')
    data = []
    resultFile = open(path, 'r')
    for line in resultFile:
        nowInput = line.strip().split(' ')
        if len(nowInput) == 1:
            contestCode = nowInput[0]
            continue
        nowInput[1] = int(nowInput[1])
        data.append(nowInput)
    resultFile.close()
    data[problemCode][1] += 1

    # Input File
    print(Fore.RED + "\n      Input" + Fore.WHITE)
    print('--------------------')
    path = os.path.join(home + '/Github/tester/' + data[problemCode][0] + \
                        str(data[problemCode][1]) + '.in')
    inputFile = open(path, 'w')
    while 1:
        nowInput = input()
        nowInput = nowInput.strip()
        if nowInput == 'end':
            print('--------------------')
            break
        inputFile.write(nowInput + '\n')
    inputFile.close()

    # Output File
    print(Fore.RED + "\n      Output" + Fore.WHITE)
    print('--------------------')
    path = os.path.join(home + '/Github/tester/' + data[problemCode][0] + \
                        str(data[problemCode][1]) + '.out')
    outputFile = open(path, 'w')
    while 1:
        nowInput = input()
        nowInput = nowInput.strip()
        if nowInput == 'end':
            print('--------------------')
            break
        outputFile.write(nowInput + '\n')
    outputFile.close()

    # Result File
    path = os.path.join(home + '/Github/tester/result.txt')
    resultFile = open(path, 'w')
    resultFile.write(contestCode + '\n')
    for line in data:
        resultFile.write(line[0] + ' ' + str(line[1]) + '\n')
    resultFile.close()

if __name__ == "__main__":
    main()

