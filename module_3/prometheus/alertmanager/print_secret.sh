kubectl get secrets alertmanager-config -oyaml | sed -n '3 p' | cut -d ':' -f 2 | awk '{$1=$1};1'|  base64 -d 
