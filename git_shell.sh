#!/bin/bash

git add . -A
git pull
git commit -m $1
git push origin master:master 
