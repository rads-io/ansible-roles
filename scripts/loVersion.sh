#!/bin/bash

curl -o list.html "http://download.documentfoundation.org/libreoffice/stable/" 2> log
grep "a href=" -rni ./list.html | grep -v Size | grep -v "Parent Directory" > list1.html
head -n1 list1.html | cut -d">" -f5 | cut -d'=' -f2 | sed 's:"::g' | sed 's:/::g' > version.txt

if [ "5.0.5" = "$(cat version.txt)" ]; then 
    echo "LibreOffice version is 5.0.5, you have nothing to do.";
else
    echo "Please edit the following files:";
    for i in debian ubuntu; do 
	echo " * " $i/dependencies/vars/main.yml
    done
    echo "to define the LibreOffice version (lo_version) as $(cat version.txt)";
fi
