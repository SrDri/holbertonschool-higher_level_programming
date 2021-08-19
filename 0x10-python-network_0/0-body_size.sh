#!/bin/bash
# request URL display size of body in bytes
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
