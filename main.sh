#!/usr/bin/env bash

./download_tiles.sh
python3 ./create_tmx.py
