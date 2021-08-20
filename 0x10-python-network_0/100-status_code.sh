#!/bin/bash
# Send request display status code of the response
curl -o /dev/null -sw "%{http_code}" "$1"
