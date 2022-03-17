#!/bin/bash

echo "starting scrapping"

python3 scrap.py

echo "finished scrapping now map!"

python3 main.py

echo "done!"
