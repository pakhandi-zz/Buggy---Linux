echo "Enter the round number : "
read round
echo $round > temp.txt
./ini $round
if [ ! -d "$round" ]; then
  exit
fi
chmod -R 777 $round
subl ./$round
subl $round/A/aprog.cpp

#Uncomment the comments below to open the problemset in your default browser
#Make sure you have xdg-open installed on your system...

#alias xdg-open="xdg-open 2>/dev/null"
#xdg-open http://codeforces.com/contest/$round/problems