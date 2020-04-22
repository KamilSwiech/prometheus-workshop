#!/bin/sh
items=$(ls | grep -e config-.*.yaml)
for i in $items; do
	kubectl create secret generic alertmanager-config --from-file=alertmanager.yaml=$i --dry-run -oyaml > am-secret-$(echo $i | awk 'BEGIN{FS="-"} {print $2}')
done
