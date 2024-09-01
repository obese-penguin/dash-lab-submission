#!/usr/bin/env bash

echo -n "Enter AUTH_TOKEN: "
read -r auth

while :
do 
    echo -n "Enter query: "
    read -r query
    declare data="{inputs: $query, auth: $auth}"
    declare cmd=$(curl http://localhost:8000 -X POST -d "{'inputs': '${query}', 'auth': '${auth}'}" >> output.json)
    echo '\\n' >> output.json
    echo $cmd
done
