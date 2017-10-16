""" implementation of several parse functions """

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from colorama import Fore

HOME = os.path.expanduser('~') + '/Github/tester/'

__all__ = ["parse_codeforces", "parse_atcoder"]

def parse_codeforces_single_task(target, task_id, mode):
    """ parse specific task in Codeforces """

    for i, element in enumerate(target):
        html_string = str(element)
        html_string = html_string.replace('html_stringput', '')
        html_string = html_string.replace('Input', '')
        html_string = html_string.replace('Output', '')
        html_string = html_string.replace('<div class="input">', '')
        html_string = html_string.replace('<div class="output">', '')
        html_string = html_string.replace('<div class="title">', '')
        html_string = html_string.replace('</div>', '')
        html_string = html_string.replace('<pre>', '').replace('</pre>', '')
        html_string = html_string.replace('&gt;', '>')
        html_string = html_string.replace('&lt;', '<')
        html_string = html_string.replace('&quot;', '"')
        html_string = html_string.replace('&amp;', '&')
        html_string = html_string.replace('<br />', '\n')
        html_string = html_string.replace('<br/>', '\n')
        html_string = html_string.replace('</ br>', '\n')
        html_string = html_string.replace('</br>', '\n')
        html_string = html_string.replace('<br>', '\n')
        html_string = html_string.replace('< br>', '\n')
        html_string = html_string.split('\n')

        path = os.path.join(HOME + 'testcases/' + task_id + str(i + 1) + mode)

        test_cases_file = open(path, 'w')
        for data in html_string:
            if data != '' and data != ' ':
                test_cases_file.write(data + '\n')
        test_cases_file.close()

def parse_atcoder(config):
    """ parse testcases of AtCoder """

    def get_single_task_url(config, task_id):
        """ get single task url """

        contest_id = config.contest_id
        return "http://" + contest_id + '.contest.atcoder.jp/tasks/' + contest_id + '_' + task_id

    task_id = []
    test_num = []
    for i in range(26):
        task_id.append(chr(ord('a') + i))
        test_num.append(0)

    total_task_num = 0
    for i in range(26):
        now_task_url = get_single_task_url(config, task_id[i])
        page = urlopen(now_task_url)
        soup = BeautifulSoup(page.read(), "html.parser")
        test_cases = soup.findAll('pre')
        if len(test_cases) == 0:
            break
        test_cases = [test_cases[i].text for i in range(1, int(len(test_cases) / 2))]
        test_num[i] = int(len(test_cases) / 2)
        total_task_num += 1
        if len(test_cases) % 2 != 0:
            raise ValueError("Parsing Error: Input/Output Should be paris")
        for j, test_case in enumerate(test_cases):
            uppercase_task_id = chr(ord('A') + i)
            if j % 2 == 0:
                with open(HOME + '/testcases/' +
                    uppercase_task_id + str(int(j / 2 + 1)) + '.in', 'w') as input_file:
                    input_file.write(test_case)
            else:
                with open(HOME + '/testcases/' +
                    uppercase_task_id + str(int(j / 2 + 1)) + '.out', 'w') as input_file:
                    input_file.write(test_case)
        print(Fore.WHITE + "    parsing " + task_id[i] + \
              Fore.GREEN + "  [Success]  " + Fore.WHITE + "")

    result_path = os.path.join(HOME + 'contest_information.txt')
    contest_information_file = open(result_path, 'w')
    contest_information_file.write(str(config.contest_id) + '\n')
    for i in range(total_task_num):
        contest_information_file.write(chr(ord('A') + i) + ' ' + str(test_num[i]) + '\n')
    contest_information_file.close()

def parse_codeforces(config):
    """ parse testcases of CodeForces """

    codeforces_url = 'http://www.codeforces.com/contest/'
    contest_id = str(int(config.contest_id))

    main_page_url = codeforces_url + str(contest_id)
    print("    from {}".format(main_page_url))
    page = urlopen(main_page_url)
    soup = BeautifulSoup(page.read(), "html.parser")
    problem_set_size = len(soup.findAll(title="Submit"))

    task_id = []
    test_num = []
    for i in range(26):
        task_id.append(chr(ord('A') + i))
        test_num.append(0)

    for i in range(problem_set_size):
        url = codeforces_url + str(contest_id) + "/problem/" + str(task_id[i])
        page = urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")

        num_of_test_case = len(soup.findAll('div', {'class': 'input'}))
        parse_codeforces_single_task(soup.findAll('div', {'class': 'input'}), task_id[i], '.in')
        parse_codeforces_single_task(soup.findAll('div', {'class': 'output'}), task_id[i], '.out')

        test_num[i] = num_of_test_case
        print(Fore.WHITE + "    parsing " + task_id[i] + \
              Fore.GREEN + "  [Success]  " + Fore.WHITE + "")

    result_path = os.path.join(HOME + 'contest_information.txt')
    contest_information_file = open(result_path, 'w')
    contest_information_file.write(str(contest_id) + '\n')
    for i in range(problem_set_size):
        contest_information_file.write(task_id[i] + ' ' + str(test_num[i]) + '\n')
    contest_information_file.close()
