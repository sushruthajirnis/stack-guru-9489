#!/bin/bash

heroku login

inp=$1
app=$2
echo $inp
echo $app
inp_val="heroku config:get $inp -a $app"
var_val=$(eval $inp_val)

if [ ! -f .env ] ; then
    # if not create the file
      touch .env
fi

echo "$inp=$var_val" >> .env
