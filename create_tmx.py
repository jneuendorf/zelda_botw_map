def tmx(tileset_images, tiles):
    return '''<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0" orientation="orthogonal" renderorder="right-down" width="94" height="79" tilewidth="256" tileheight="256" nextobjectid="1">
  <tileset firstgid="1" name="all" tilewidth="256" tileheight="256" tilecount="7426" columns="0">
{}
  </tileset>
  <layer name="Tile Layer 1" width="94" height="79">
    <data>
{}
    </data>
  </layer>
</map>
'''.format('\n'.join(tileset_images), '\n'.join(tiles))

tileset_images = []
tileset_image_id = 0
for x in range(17,110 + 1):
    for y in range(24,102 + 1):
        tileset_images.append('''    <tile id="{}">
      <image width="256" height="256" source="./7_{}_{}.png"/>
    </tile>'''.format(tileset_image_id, x, y))
        tileset_image_id += 1

tiles = []
for y in range(0,102-24+1):
    gid = y + 1
    for x in range(0,110-17+1):
        tiles.append('      <tile gid="{}"/>'.format(gid))
        gid += 79

with open('./botw.tmx', 'w') as f:
    f.write(tmx(tileset_images, tiles))
