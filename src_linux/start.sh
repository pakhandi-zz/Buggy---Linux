echo "Enter the round number : "
read round
echo $round > temp.txt
./ini < temp.txt
if [ ! -d "$round" ]; then
  exit
fi
chmod -R 777 $round
subl ./$round
subl $round/A/aprog.cpp
#alias xdg-open="xdg-open 2>/dev/null"
#xdg-open http://codeforces.com/contest/$round/problems