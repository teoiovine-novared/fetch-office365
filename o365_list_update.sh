#!/bin/bash
# V1

echo "a b c d e f" | IFS=  read a
echo $a
python3.8 dataGroupManager.py $a $b $c $d $e $f

echo ""