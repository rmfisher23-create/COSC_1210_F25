# config_c4.py

# Grid and Room Settings
ROOM_WIDTH = 200
ROOM_HEIGHT = 200
GRID_ROWS = 3
GRID_COLS = 3

# Player Settings
PLAYER_RADIUS = 10


# Screen Size
WIDTH = ROOM_WIDTH * GRID_ROWS
HEIGHT = ROOM_HEIGHT * GRID_COLS

# Colors (R, G, B)
BG_COLOR = (200, 200, 200)
WALL_COLOR = (0, 0, 0)
PLAYER_COLOR1 = (220,20,60) # crimson
PLAYER_COLOR2 = (230,230,250) # (230,230,250) lavender

# Frames Per Second
FPS = 60

# --- Player appearance ---
PLAYER_IMAGE_SIZE1 = (60, 60)
PLAYER_IMAGE_SIZE2 = (60, 60)             # w, h in pixels
PLAYER_RADIUS = 24                       # half of width; used by your collision