class wall:
    def __init__(self, x1, y1, x2, y2, weight):
        self.color = "blue"
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.weight = weight


class upper_grass:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = (0, 180, 0)
        self.slow = 3


class down_grass:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = (0, 100, 0)
        self.slow = 3


class sand:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = (255, 255, 80)
        self.slow = 12


class barrier:
    def __init__(self, x1, y1, x2, y2, weight):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.weight = weight


class water:
    def __init__(self, x, y, size_x, size_y, move_x, move_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = (0, 0, 100)
        self.slow = 0
        self.move_x = move_x
        self.move_y = move_y


class down_sand:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = (100, 100, 0)
        self.slow = 12


class hole_1:
    def __init__(self):
        self.spawn_x = 180
        self.spawn_y = 880
        self.photo = "textures/hole_1.png"

    def load_map(self):
        hole = []
        hole.append(1000)
        hole.append(880)
        walls = []
        walls.append(wall(100, 900, 200, 900, 10))
        walls.append(wall(100, 900, 100, 100, 10))
        walls.append(wall(100, 100, 1400, 100, 10))
        walls.append(wall(1400, 100, 1400, 300, 10))
        walls.append(wall(1400, 300, 1250, 300, 10))
        walls.append(wall(1250, 300, 1250, 400, 10))
        walls.append(wall(1250, 400, 1050, 400, 10))
        walls.append(wall(1050, 300, 1050, 900, 10))
        walls.append(wall(950, 900, 1050, 900, 10))
        walls.append(wall(950, 300, 950, 900, 10))
        walls.append(wall(950, 400, 750, 400, 10))
        walls.append(wall(750, 400, 750, 300, 10))
        walls.append(wall(750, 300, 200, 300, 10))
        walls.append(wall(200, 300, 200, 900, 10))
        grass = []
        grass.append(upper_grass(100, 100, 100, 800))
        grass.append(upper_grass(200, 100, 1200, 200))
        grass.append(upper_grass(950, 300, 100, 600))
        waters = []
        down_grasss = []
        sands = []
        sands.append(sand(750, 300, 200, 100))
        sands.append(sand(1050, 300, 200, 100))
        down_sands = []
        barriers = []
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_2:
    def __init__(self):
        self.spawn_x = 150
        self.spawn_y = 100
        self.photo = "textures/hole_2.png"

    def load_map(self):
        hole = []
        hole.append(500)
        hole.append(200)
        walls = []
        walls.append(wall(50, 50, 1450, 50, 10))
        walls.append(wall(1450, 50, 1450, 950, 10))
        walls.append(wall(50, 950, 1450, 950, 10))
        walls.append(wall(50, 50, 50, 950, 10))
        walls.append(wall(250, 50, 250, 800, 10))
        walls.append(wall(250, 800, 280, 800, 10))
        walls.append(wall(320, 800, 400, 800, 10))
        walls.append(wall(450, 150, 450, 950, 10))
        walls.append(wall(250, 550, 350, 550, 10))
        walls.append(wall(450, 300, 350, 300, 10))
        walls.append(wall(450, 150, 1200, 150, 10))
        walls.append(wall(950, 150, 950, 800, 10))
        walls.append(wall(950, 500, 1250, 500, 10))
        walls.append(wall(1200, 750, 1200, 950, 10))
        grass = []
        grass.append(upper_grass(50, 50, 400, 900))
        waters = []
        waters.append(water(450, 50, 750, 100, 16, 0))
        down_grasss = []
        down_grasss.append(down_grass(450, 150, 500, 800))
        down_grasss.append(down_grass(1200, 150, 250, 600))
        down_grasss.append(down_grass(950, 500, 250, 450))
        sands = []
        sands.append(sand(1200, 50, 250, 100))
        down_sands = []
        down_sands.append(down_sand(950, 150, 250, 350))
        down_sands.append(down_sand(1200, 750, 250, 200))
        barriers = []
        barriers.append(barrier(1195, 150, 1455, 150, 10))
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_3:
    def __init__(self):
        self.spawn_x = 1400
        self.spawn_y = 800
        self.photo = "textures/hole_3.png"

    def load_map(self):
        hole = []
        hole.append(720)
        hole.append(380)
        walls = []
        walls.append(wall(1450, 950, 1450, 50, 10))
        walls.append(wall(1150, 950, 1450, 950, 10))
        walls.append(wall(1150, 950, 1150, 150, 10))
        walls.append(wall(1250, 750, 1450, 750, 10))
        walls.append(wall(1250, 750, 1450, 750, 10))
        walls.append(wall(1250, 750, 1250, 850, 10))
        walls.append(wall(1150, 250, 1350, 250, 10))
        walls.append(wall(50, 50, 1450, 50, 10))
        walls.append(wall(50, 50, 50, 950, 10))
        walls.append(wall(150, 150, 1150, 150, 10))
        walls.append(wall(150, 150, 150, 850, 10))
        walls.append(wall(50, 950, 850, 950, 10))
        walls.append(wall(150, 850, 750, 850, 10))
        walls.append(wall(850, 950, 850, 200, 10))
        walls.append(wall(750, 200, 850, 200, 10))
        walls.append(wall(750, 200, 750, 400, 10))
        walls.append(wall(600, 400, 750, 400, 10))
        walls.append(wall(500, 300, 750, 300, 10))
        walls.append(wall(600, 450, 750, 450, 10))
        walls.append(wall(500, 300, 500, 700, 10))
        walls.append(wall(500, 700, 750, 700, 10))
        walls.append(wall(750, 700, 750, 850, 10))
        grass = []
        grass.append(upper_grass(1150, 50, 300, 200))
        grass.append(upper_grass(1350, 250, 100, 300))
        grass.append(upper_grass(1150, 550, 300, 400))
        waters = []
        waters.append(water(150, 50, 1000, 100, -16, 0))
        waters.append(water(50, 50, 100, 800, 0, 16))
        waters.append(water(550, 400, 200, 50, 16, 0))
        down_grasss = []
        down_grasss.append(down_grass(50, 850, 800, 100))
        down_grasss.append(down_grass(750, 700, 100, 150))
        down_grasss.append(down_grass(500, 450, 350, 250))
        down_grasss.append(down_grass(500, 400, 50, 50))
        down_grasss.append(down_grass(500, 300, 250, 100))
        sands = []
        sands.append(sand(1150, 250, 200, 300))
        down_sands = []
        down_sands.append(down_sand(750, 200, 100, 250))
        barriers = []
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_4:
    def __init__(self):
        self.spawn_x = 150
        self.spawn_y = 500
        self.photo = "textures/hole_4.png"

    def load_map(self):
        hole = []
        hole.append(1150)
        hole.append(500)
        walls = []
        walls.append(wall(100, 300, 1450, 300, 10))
        walls.append(wall(1450, 300, 1450, 700, 10))
        walls.append(wall(1450, 700, 100, 700, 10))
        walls.append(wall(100, 300, 100, 700, 10))
        walls.append(wall(1100, 600, 1250, 600, 10))
        walls.append(wall(1100, 400, 1250, 400, 10))
        walls.append(wall(1100, 600, 1100, 400, 10))
        grass = []
        grass.append(upper_grass(100, 300, 1350, 400))
        waters = []
        down_grasss = []
        sands = []
        down_sands = []
        barriers = []
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_5:
    def __init__(self):
        self.spawn_x = 200
        self.spawn_y = 500
        self.photo = "textures/hole_5.png"

    def load_map(self):
        hole = []
        hole.append(1375)
        hole.append(500)
        walls = []
        walls.append(wall(50, 50, 1450, 50, 10))
        walls.append(wall(1450, 950, 1450, 50, 10))
        walls.append(wall(1450, 950, 50, 950, 10))
        walls.append(wall(50, 50, 50, 950, 10))
        walls.append(wall(150, 650, 350, 650, 10))
        walls.append(wall(350, 650, 350, 550, 10))
        walls.append(wall(350, 550, 1250, 550, 10))
        walls.append(wall(400, 600, 400, 850, 10))
        walls.append(wall(400, 550, 400, 350, 10))
        walls.append(wall(400, 350, 1250, 350, 10))
        walls.append(wall(1250, 350, 1250, 550, 10))
        walls.append(wall(400, 650, 1300, 650, 10))
        walls.append(wall(1300, 650, 1300, 150, 10))
        grass = []
        grass.append(upper_grass(50, 50, 350, 300))
        grass.append(upper_grass(50, 350, 200, 300))
        grass.append(upper_grass(50, 650, 300, 300))
        grass.append(upper_grass(350, 850, 50, 100))
        grass.append(upper_grass(400, 650, 50, 300))
        waters = []
        waters.append(water(450, 650, 850, 300, 16, 0))
        waters.append(water(450, 550, 800, 100, 16, 0))
        down_grasss = []
        down_grasss.append(down_grass(350, 650, 50, 200))
        down_grasss.append(down_grass(400, 50, 900, 300))
        down_grasss.append(down_grass(1250, 350, 50, 300))
        down_grasss.append(down_grass(1300, 50, 150, 200))
        down_grasss.append(down_grass(1300, 450, 150, 200))
        sands = []
        sands.append(sand(250, 350, 100, 300))
        sands.append(sand(350, 350, 50, 200))
        sands.append(sand(1300, 650, 150, 300))
        down_sands = []
        down_sands.append(down_sand(350, 550, 100, 100))
        down_sands.append(down_sand(1300, 250, 150, 200))
        barriers = []
        barriers.append(barrier(350, 645, 350, 850, 1))
        barriers.append(barrier(403, 850, 350, 850, 1))
        barriers.append(barrier(400, 50, 400, 350, 1))
        barriers.append(barrier(1295, 650, 1455, 650, 1))
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_6:
    def __init__(self):
        self.spawn_x = 150
        self.spawn_y = 900
        self.photo = "textures/hole_6.png"

    def load_map(self):
        hole = []
        hole.append(350)
        hole.append(900)
        walls = []
        walls.append(wall(50, 50, 1450, 50, 10))
        walls.append(wall(50, 50, 50, 950, 10))
        walls.append(wall(1450, 50, 1450, 350, 10))
        walls.append(wall(450, 350, 1450, 350, 10))
        walls.append(wall(450, 350, 450, 950, 10))
        walls.append(wall(50, 950, 450, 950, 10))
        walls.append(wall(250, 150, 250, 950, 10))
        walls.append(wall(250, 150, 150, 150, 10))
        walls.append(wall(300, 150, 1300, 150, 10))
        walls.append(wall(50, 250, 200, 250, 10))
        walls.append(wall(450, 147, 450, 250, 10))
        walls.append(wall(650, 147, 650, 250, 10))
        walls.append(wall(850, 147, 850, 250, 10))
        walls.append(wall(1050, 147, 1050, 250, 10))
        walls.append(wall(1250, 147, 1250, 250, 10))
        walls.append(wall(1150, 353, 1150, 250, 10))
        walls.append(wall(950, 353, 950, 250, 10))
        walls.append(wall(750, 353, 750, 250, 10))
        walls.append(wall(550, 353, 550, 250, 10))
        grass = []
        grass.append(upper_grass(50, 50, 200, 900))
        grass.append(upper_grass(250, 50, 50, 100))
        waters = []
        waters.append(water(300, 50, 1000, 100, 16, 0))
        down_grasss = []
        down_grasss.append(down_grass(250, 150, 200, 800))
        down_grasss.append(down_grass(450, 150, 1000, 200))
        sands = []
        sands.append(sand(1300, 50, 150, 100))
        down_sands = []
        barriers = []
        barriers.append(barrier(245, 150, 305, 150, 1))
        barriers.append(barrier(1295, 150, 1455, 150, 1))
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_7:
    def __init__(self):
        self.spawn_x = 100
        self.spawn_y = 900
        self.photo = "textures/hole_7.png"

    def load_map(self):
        hole = []
        hole.append(500)
        hole.append(500)
        walls = []
        walls.append(wall(50, 50, 1450, 50, 10))
        walls.append(wall(1450, 50, 1450, 950, 10))
        walls.append(wall(50, 50, 50, 950, 10))
        walls.append(wall(50, 950, 1450, 950, 10))
        walls.append(wall(150, 250, 150, 953, 10))
        walls.append(wall(250, 150, 250, 750, 10))
        walls.append(wall(250, 150, 1350, 150, 10))
        walls.append(wall(450, 450, 1350, 450, 10))
        walls.append(wall(450, 450, 450, 550, 10))
        walls.append(wall(445, 550, 1050, 550, 10))
        walls.append(wall(1250, 450, 1250, 600, 10))
        walls.append(wall(1000, 250, 1453, 250, 10))
        walls.append(wall(900, 350, 1350, 350, 10))
        walls.append(wall(1000, 750, 1453, 750, 10))
        walls.append(wall(750, 850, 1350, 850, 10))
        walls.append(wall(750, 850, 750, 648, 10))
        walls.append(wall(600, 650, 1250, 650, 10))
        walls.append(wall(1250, 650, 1250, 700, 10))
        grass = []
        grass.append(upper_grass(50, 250, 100, 700))
        grass.append(upper_grass(150, 250, 100, 500))
        grass.append(upper_grass(250, 450, 200, 300))
        grass.append(upper_grass(450, 550, 300, 200))
        waters = []
        waters.append(water(250, 150, 500, 300, 15, 0))
        waters.append(water(900, 350, 450, 100, -15, 0))
        waters.append(water(850, 650, 400, 50, -15, 0))
        down_grasss = []
        down_grasss.append(down_grass(50, 50, 1400, 100))
        down_grasss.append(down_grass(750, 150, 700, 200))
        down_grasss.append(down_grass(1350, 350, 100, 100))
        down_grasss.append(down_grass(450, 450, 800, 100))
        down_grasss.append(down_grass(750, 550, 500, 100))
        down_grasss.append(down_grass(750, 700, 500, 50))
        down_grasss.append(down_grass(750, 750, 700, 100))
        down_grasss.append(down_grass(150, 850, 1300, 100))
        sands = []
        sands.append(sand(50, 150, 200, 100))
        sands.append(sand(150, 750, 600, 100))
        down_sands = []
        down_sands.append(down_sand(700, 350, 200, 100))
        down_sands.append(down_sand(1250, 450, 200, 300))
        down_sands.append(down_sand(750, 650, 100, 50))
        barriers = []
        barriers.append(barrier(45, 150, 255, 150, 10))
        barriers.append(barrier(145, 850, 755, 850, 10))
        barriers.append(barrier(750, 547, 750, 753, 10))
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


class hole_8:
    def __init__(self):
        self.spawn_x = 250
        self.spawn_y = 550
        self.photo = "textures/hole_8.png"

    def load_map(self):
        hole = []
        hole.append(1250)
        hole.append(650)
        walls = []
        walls.append(wall(100, 300, 1450, 300, 10))
        walls.append(wall(1450, 300, 1450, 700, 10))
        walls.append(wall(1455, 700, 100, 700, 10))
        walls.append(wall(100, 300, 100, 700, 10))
        walls.append(wall(305, 600, 200, 600, 10))
        walls.append(wall(300, 600, 300, 450, 10))
        walls.append(wall(600, 600, 600, 450, 10))
        walls.append(wall(900, 600, 900, 450, 10))
        walls.append(wall(1200, 703, 1200, 450, 10))
        walls.append(wall(450, 297, 450, 450, 10))
        walls.append(wall(750, 297, 750, 450, 10))
        walls.append(wall(1050, 297, 1050, 450, 10))
        grass = []
        grass.append(upper_grass(100, 400, 1350, 200))
        grass.append(upper_grass(100, 300, 350, 100))
        grass.append(upper_grass(1200, 600, 250, 100))
        waters = []
        waters.append(water(100, 600, 100, 100, 0, -15))
        down_grasss = []
        down_grasss.append(down_grass(200, 600, 1000, 100))
        sands = []
        sands.append(sand(450, 300, 1000, 100))
        down_sands = []
        barriers = []
        barriers.append(barrier(300, 600, 1200, 600, 10))
        return self.spawn_x, self.spawn_y, hole, walls, grass, down_grasss, sands, down_sands, waters, barriers, self.photo


holes = {
    1: hole_1,
    2: hole_2,
    3: hole_3,
    4: hole_4,
    5: hole_5,
    6: hole_6,
    7: hole_7,
    8: hole_8
}
