echo "Enter the round number : "
read round
echo $round > temp.txt
./ini < temp.txt
subl ./$round
subl $round/A/prog.cpp
xdg-open http://codeforces.com/contest/$round/problems