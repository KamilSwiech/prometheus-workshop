#!/bin/bash

url_list=$(cat url_file)
for url in $url_list; do
	for i in {1..100}; do
		curl -s $url > /dev/null
	done
done
