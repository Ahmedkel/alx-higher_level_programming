#!/bin/bash
# Send a POST request to a URL passed as an argument,
# and displays the body of the response

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
