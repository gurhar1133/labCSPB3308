#!/bin/bash
echo $1
cat $1 | while read line; do
	echo $line
done
