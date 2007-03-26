#!/bin/bash

cd ~/dev/tRack
git add -A
git commit -m '"$@"'
git push origin master
