echo "Enter the round number : "
read round
echo $round > temp.txt
./ini < temp.txt
subl ./$round
subl $round/A/prog.cpp
alias xdg-open="xdg-open 2>/dev/null"
xdg-open http://codeforces.com/contest/$round/problems