#!/usr/bin/env bash


# 7_17_24
#
# 7_99_102
# https://zeldamaps.com/tiles/botw/hyrule/7_17_24.png

url='https://zeldamaps.com/tiles/botw/hyrule'
zoom_level="7"

# NOTE: This can probably be made faster: https://stackoverflow.com/a/24276040/6928824
for x in $(seq 17 1 110)
do
    for y in $(seq 24 1 102)
    do
        filename=$(printf "%d_%d_%d.png" $zoom_level $x $y)
        # echo "would download $url/$filename"
        curl -O "$url/$filename"
    done
done
