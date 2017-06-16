import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from colorama import Fore

home = os.path.expanduser('~')

def parse(target, problemChr, mode):
    for i, element in enumerate(target):
        In = str(element)
        In=In.replace('Input', '')
        In=In.replace('Output', '')
        In=In.replace('<div class="input">', '')
        In=In.replace('<div class="output">', '')
        In=In.replace('<div class="title">', '')
        In=In.replace('</div>', '')
        In=In.replace('<pre>', '').replace('</pre>', '')
        In=In.replace('&gt;', '>')
        In=In.replace('&lt;', '<')
        In=In.replace('&quot;', '"')
        In=In.replace('&amp;', '&')
        In=In.replace('<br />', '\n')
        In=In.replace('<br/>', '\n')
        In=In.replace('</ br>', '\n')
        In=In.replace('</br>', '\n')
        In=In.replace('<br>', '\n')
        In=In.replace('< br>', '\n')
        In=In.split('\n')

        path = os.path.join(home + '/Github/tester/' + problemChr \
                            + str(i + 1) + mode)

        outputFile = open(path, 'w')
        for data in In:
            if data != '' and data != ' ':
                outputFile.write(data + '\n')
        outputFile.close()

def main():
    codeforcesURL = 'http://www.codeforces.com/contest/'
    print(Fore.RED + "\n      Parser" + Fore.WHITE)
    contestCode = int(input("Contest Code: " ))

    mainPageURL = codeforcesURL + str(contestCode)
    page = urlopen(mainPageURL)
    soup = BeautifulSoup(page.read(), "html.parser")
    problemSetSize = len(soup.findAll(title="Submit"))

    ch = []
    chtest = []
    for i in range(26):
        ch.append(chr(ord('A') + i))
        chtest.append(0)

    for i in range(problemSetSize):
        url = codeforcesURL + str(contestCode) + "/problem/" + str(ch[i])
        page = urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")

        numOfTestCase = len(soup.findAll('div', {'class': 'input'}))
        parse(soup.findAll('div', {'class': 'input'}), ch[i], '.in')
        parse(soup.findAll('div', {'class': 'output'}), ch[i], '.out')

        chtest[i] = numOfTestCase
        print(Fore.WHITE + "parsing " + ch[i] + \
              Fore.GREEN + "  [Success]  " + Fore.WHITE + "")

    resultPath = os.path.join(home + '/Github/tester/result.txt')
    resultFile = open(resultPath, 'w')
    resultFile.write(str(contestCode) + '\n')
    for i in range(problemSetSize):
        resultFile.write(ch[i] + ' ' + str(chtest[i]) + '\n')
    resultFile.close()

if __name__ == "__main__":
    main()
