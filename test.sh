#!/bin/bash
name=$1
contest_code=0
problem_code=${name:0:1}
pathe=$HOME'/Github/tester/result.txt'
DONE=false
todo=0
tot=0
foo=0
until $DONE
do
  read line || DONE=true
  foo=$(($foo+1))
  # echo "${line}"
  if [ ${foo} = 1 ]; then
    contest_code=${line}
  elif [[ ${line:0:1} == $problem_code ]]; then
    tot=${line:2:1}
  fi
done < $pathe

fla=0

# clang++ -std=c++11 -stdlib=libc++ -O2 -Wall -Wshadow -I /usr/local/include $name || fla=1
g++-7 $name || fla=1
if [ $fla -eq 1 ]
then
  echo -e "\033[1;31mCompilation Error\x1b[0m"
  exit
fi

todo=0
while [[ $todo -lt $tot ]]
do
  echo '----------------------------------------'
  u=1
  todo=$((todo+1))
  pathe=$HOME'/Github/tester/'
  temppath=$pathe$problem_code$todo'.in'
  x=0
  # timeout 2 ./a.out <$temppath> $pathe$problem_code$todo'.rc' || x=1
  # brew install coreutils for gtimeout
  gtimeout 2 ./a.out <$temppath> $pathe$problem_code$todo'.rc' || x=1
  diff --brief --ignore-space-change <(sort $pathe$problem_code$todo'.out') <(sort $pathe$problem_code$todo'.rc') >/dev/null
  comp_val=$?

  if [ $x -eq 1 ]
  then
    echo -e "Running test "$todo"\x1b[0m : \033[1;34m [Time limit exceeded]\x1b[0m"
  elif [ $comp_val -eq 1 ]
  then
    echo -e "Running test "$todo"\x1b[0m : \033[91m [Wrong Answer]\x1b[0m"
    echo -e "\033[1;35mInput :\x1b[0m"
    cat < $temppath
    echo -e "\033[1;31mRecieved Ouput :\x1b[0m "
    cat < $pathe$problem_code$todo'.rc'
    echo -e "\033[1;32mExpected Output :\x1b[0m"
    cat < $pathe$problem_code$todo'.out'
  else
    echo -e "Running test "$todo" : \033[92m [Pretest Passed]\x1b[0m"
  fi
done
echo '----------------------------------------'
