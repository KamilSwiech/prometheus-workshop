#!/bin/bash

yamls=$(find . | grep .yaml)
namespace=$(find . | grep namespace)

kubectl apply -f $namespace

for i in $yamls; do
	kubectl apply -f $i
done
