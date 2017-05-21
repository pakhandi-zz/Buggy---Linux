#! /bin/bash
echo "Enter the round number : "
read round

echo $round > temp
./ini $1 $round

while read line           
do            
    echo $line
    break         
done <temp

echo "Press any key to continue"
read r

if [ ! -d "$line$round" ]; then
  exit
fi

chmod -R 777 $line$round
subl $line$round
subl $line$round/A/sol.cpp