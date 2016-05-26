echo "Enter the round number : "
read round

echo $round > temp
./ini $round

while read line           
do            
    echo $line
    break         
done <temp

if [ ! -d "$line$round" ]; then
  exit
fi

chmod -R 777 $line$round
subl $line$round
subl $line$round/A/aprog.cpp

#Uncomment the comments below to open the problemset in your default browser
#Make sure you have xdg-open installed on your system...

#alias xdg-open="xdg-open 2>/dev/null"
#xdg-open http://codeforces.com/contest/$round/problems