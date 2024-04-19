WALKING_UP_DIR = "Images/Penguins/Walking/Up/"
WALKING_DOWN_DIR = "Images/Penguins/Walking/Down/"
WALKING_SIDE_DIR = "Images/Penguins/Walking/Side/"

UP_PATTERN = "walk_up_{}.png"
DOWN_PATTERN = "walk_down_{}.png"
SIDE_PATTERN = "walk_side_{}.png"

PENGUIN_WALK_UP_LEN = 6
PENGUIN_WALK_DOWN_LEN = 6
PENGUIN_WALK_SIDE_LEN = 7

PENGUIN_WALK_UP_IMGS = [WALKING_UP_DIR + UP_PATTERN.format(i) for i in range(1, PENGUIN_WALK_UP_LEN + 1)]
PENGUIN_WALK_DOWN_IMGS = [WALKING_DOWN_DIR + DOWN_PATTERN.format(i) for i in range(1, PENGUIN_WALK_DOWN_LEN + 1)]
PENGUIN_WALK_SIDE_IMGS = [WALKING_SIDE_DIR + SIDE_PATTERN.format(i) for i in range(1, PENGUIN_WALK_SIDE_LEN + 1)]