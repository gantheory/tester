""" Add Test """

import os
from colorama import Fore

HOME = os.path.expanduser('~') + '/Github/tester/'

def main():
    """ Main Function to Add Test """

    print(Fore.RED + "\n      ADD TEST" + Fore.WHITE)
    contestCode = 0
    problemCode = ord(input("Problem Code: ")) - ord('A')

    path = os.path.join(HOME + 'contest_information.txt')
    data = []
    contest_information_file = open(path, 'r')
    for line in contest_information_file:
        nowInput = line.strip().split(' ')
        if len(nowInput) == 1:
            contestCode = nowInput[0]
            continue
        nowInput[1] = int(nowInput[1])
        data.append(nowInput)
    contest_information_file.close()
    data[problemCode][1] += 1

    # Input File
    print(Fore.RED + "\n      Input" + Fore.WHITE)
    print('--------------------')
    path = os.path.join(HOME + '/testcases/' +
                        data[problemCode][0] + str(data[problemCode][1]) + '.in')
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
    path = os.path.join(HOME + '/testcases/' +
                        data[problemCode][0] + str(data[problemCode][1]) + '.out')
    outputFile = open(path, 'w')
    while 1:
        nowInput = input()
        nowInput = nowInput.strip()
        if nowInput == 'end':
            print('--------------------')
            break
        outputFile.write(nowInput + '\n')
    outputFile.close()

    # Contest Information File
    path = os.path.join(HOME + 'contest_information.txt')
    contest_information_file = open(path, 'w')
    contest_information_file.write(contestCode + '\n')
    for line in data:
        contest_information_file.write(line[0] + ' ' + str(line[1]) + '\n')
    contest_information_file.close()

if __name__ == "__main__":
    main()
