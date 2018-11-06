#!/bin/sh

for module_name in python-twitter configparser; do
    pip install --target=. $module_name
done 
