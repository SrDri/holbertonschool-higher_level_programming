#!/bin/bash
# send POST request and display body of the response
curl -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
