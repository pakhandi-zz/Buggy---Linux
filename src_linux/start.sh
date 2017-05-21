echo "Enter the round number : "
read round

echo $round > temp
./ini $1 $round

while read line           
do            
    echo $line
    break         
done <temp

read -n 1 -s -p "Press any key to continue"

if [ ! -d "$line$round" ]; then
  exit
fi

chmod -R 777 $line$round
subl $line$round
subl $line$round/A/sol.cpp