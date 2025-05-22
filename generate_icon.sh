# 1) Set your source and iconset directory names
ICON_SRC="icon.png"
ICONSET_DIR="MusicPlayer.iconset"

# 2) Create the .iconset folder
rm -rf "$ICONSET_DIR"
mkdir "$ICONSET_DIR"

# 3) Generate all the required sizes (PNG output)
sips -Z 16   "$ICON_SRC" --out "$ICONSET_DIR/icon_16x16.png"
sips -Z 32   "$ICON_SRC" --out "$ICONSET_DIR/icon_16x16@2x.png"
sips -Z 32   "$ICON_SRC" --out "$ICONSET_DIR/icon_32x32.png"
sips -Z 64   "$ICON_SRC" --out "$ICONSET_DIR/icon_32x32@2x.png"
sips -Z 128  "$ICON_SRC" --out "$ICONSET_DIR/icon_128x128.png"
sips -Z 256  "$ICON_SRC" --out "$ICONSET_DIR/icon_128x128@2x.png"
sips -Z 256  "$ICON_SRC" --out "$ICONSET_DIR/icon_256x256.png"
sips -Z 512  "$ICON_SRC" --out "$ICONSET_DIR/icon_256x256@2x.png"
sips -Z 512  "$ICON_SRC" --out "$ICONSET_DIR/icon_512x512.png"
sips -Z 1024 "$ICON_SRC" --out "$ICONSET_DIR/icon_512x512@2x.png"

# 4) Build the .icns from that iconset
iconutil -c icns "$ICONSET_DIR" --output "icon.icns"

# (Optional) clean up the intermediate iconset folder
rm -rf "$ICONSET_DIR"

echo "✅ Created MusicPlayer.icns"
