#!/bin/bash
URL=http://localhost:5000/form
if which xdg-open > /dev/null
then
  xdg-open $URL
elif which gnome-open > /dev/null
then
  gnome-open $URL
fi
