#!/bin/bash
# Send JSON POST request display body of the response
curl -sd @"$2" -X POST "$1" -H "Content-Type: application/json"
