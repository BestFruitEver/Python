#!/bin/bash


function gitacp("$@"){
git add .

git commit -m "$@"
git push -u origin master
}
