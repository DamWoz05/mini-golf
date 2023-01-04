import pygame

import load_map as lm

pygame.init()

keys = pygame.key.get_pressed()


def linear_ab(x1, y1, x2, y2):
    if x1 == x2:
        a = 0
    else:
        a = (y2 - y1) / (x2 - x1)
    b = y1 - (a * x1)
    return a, b


def f(x, a, b):
    return (a * x) + b


class ball:
    def __init__(self, x, y, ball_id):
        self.ball_id = ball_id
        self.color = balls[ball_id]
        self.x = x
        self.y = y
        self.ckx = x
        self.cky = y
        self.size = 8
        self.inhole = False
        self.x_velocity = 0
        self.y_velocity = 0
        self.inmove = False
        self.hits = 0
        self.t_vel_x = 0
        self.t_vel_y = 0
        self.correct_x = False
        self.correct_y = False
        self.slow = 1
        self.down = False
        self.bounce = 0


class mapi:
    def __init__(self):
        self.spawn_x = 150
        self.spawn_y = 800
        self.hole = []
        self.walls = []
        self.grass = []
        self.down_grass = []
        self.sand = []
        self.down_sand = []
        self.water = []
        self.barriers = []
        self.barriers_on = False
        self.photo = ""

    def create_map(self, nr_hole):
        self.hole.clear()
        self.walls.clear()
        self.grass.clear()
        self.down_grass.clear()
        self.sand.clear()
        self.down_sand.clear()
        self.water.clear()
        self.barriers.clear()
        self.barriers_on = False
        map_to_load = lm.holes[nr_hole]()
        self.spawn_x, self.spawn_y, self.hole, self.walls, self.grass, self.down_grass, self.sand, self.down_sand, self.water, self.barriers, self.photo = map_to_load.load_map()
        self.photo = pygame.image.load(self.photo).convert()

    def draw_map(self):
        screen.blit(current_map.photo, (0, 0))

    def check_texture(self, object):
        for i in range(len(self.down_grass)):
            if self.down_grass[i].x <= object.x <= self.down_grass[i].x + self.down_grass[i].size_x and self.down_grass[
                i].y <= object.y <= \
                    self.down_grass[i].y + self.down_grass[i].size_y:
                object.down = True
                object.slow = self.down_grass[i].slow
                return None
        for i in range(len(self.down_sand)):
            if self.down_sand[i].x <= object.x <= self.down_sand[i].x + self.down_sand[i].size_x and self.down_sand[
                i].y <= object.y <= \
                    self.down_sand[i].y + self.down_sand[i].size_y:
                object.down = True
                object.slow = self.down_sand[i].slow
                return None
        for i in range(len(self.water)):
            if self.water[i].x <= object.x <= self.water[i].x + self.water[i].size_x and self.water[i].y <= object.y <= \
                    self.water[i].y + self.water[i].size_y:
                object.slow = self.water[i].slow
                object.t_vel_x = 0
                object.t_vel_y = 0
                object.x_velocity = self.water[i].move_x
                object.y_velocity = self.water[i].move_y
                if object.x_velocity == 0:
                    center = (self.water[i].x + (self.water[i].x + self.water[i].size_x)) // 2
                    if object.x != center:
                        if object.x - center < 0:
                            object.x += 1
                        else:
                            object.x -= 1
                if object.y_velocity == 0:
                    center = (self.water[i].y + (self.water[i].y + self.water[i].size_y)) // 2
                    if object.y != center:
                        if object.y - center < 0:
                            object.y += 1
                        else:
                            object.y -= 1
                return None
        for i in range(len(self.grass)):
            if self.grass[i].x <= object.x <= self.grass[i].x + self.grass[i].size_x and self.grass[i].y <= object.y <= \
                    self.grass[i].y + self.grass[i].size_y:
                object.slow = self.grass[i].slow
                object.down = False
                return None
        for i in range(len(self.sand)):
            if self.sand[i].x <= object.x <= self.sand[i].x + self.sand[i].size_x and self.sand[i].y <= object.y <= \
                    self.sand[i].y + self.sand[i].size_y:
                object.slow = self.sand[i].slow
                object.down = False
                return None
        object.x = object.ckx
        object.y = object.cky
        object.x_velocity = 0
        object.y_velocity = 0
        object.t_vel_x = 0
        object.t_vel_y = 0

    def check_hit_x(self, new_x, new_y, object):
        a, b = linear_ab(object.x, object.y, new_x, new_y)
        walls = []
        for i in range(len(self.walls)):
            walls.append(self.walls[i])
        if object.down:
            for i in range(len(self.barriers)):
                walls.append(self.barriers[i])
        for i in range(len(walls)):
            guard = True
            if walls[i].y1 == walls[i].y2:
                guard = False
            if guard:
                if (walls[i].x1 - object.x) * (walls[i].x1 - new_x) < 1:
                    if walls[i].y1 <= f(walls[i].x1, a, b) <= walls[i].y2 or walls[i].y1 >= f(walls[i].x1, a, b) >= \
                            walls[i].y2:
                        if object.t_vel_x >= 0:
                            object.t_vel_x -= walls[i].x1 - object.x
                            object.bounce += 1
                        else:
                            object.t_vel_x += walls[i].x1 - object.x
                            object.bounce += 1
                        if object.bounce > 3:
                            object.t_vel_x = 10
                            object.x_velocity = 10
                        return -1, walls[i].y1, walls[i].y2, walls[i].x1
        object.correct_x = False
        return 1, 0, 0, 0

    def check_hit_y(self, new_y, new_x, object):
        a, b = linear_ab(object.y, object.x, new_y, new_x)
        walls = []
        for i in range(len(self.walls)):
            walls.append(self.walls[i])
        if object.down:
            for i in range(len(self.barriers)):
                walls.append(self.barriers[i])
        for i in range(len(walls)):
            guard = True
            if walls[i].x1 == walls[i].x2:
                guard = False
            if guard:
                if (walls[i].y1 - object.y) * (walls[i].y1 - new_y) < 1:
                    if walls[i].x1 <= f(walls[i].y1, a, b) <= walls[i].x2 or walls[i].x1 >= f(walls[i].y1, a, b) >= \
                            walls[i].x2:
                        if object.t_vel_y >= 0:
                            object.t_vel_y -= walls[i].y1 - object.y
                            object.bounce += 1
                        else:
                            object.t_vel_y += walls[i].y1 - object.y
                            object.bounce += 1
                        if object.bounce > 3:
                            object.t_vel_y = 10
                            object.y_velocity = 10
                        return -1, walls[i].x1, walls[i].x2, walls[i].y1
        object.correct_y = False
        return 1, 0, 0, 0

    def check_in_hole(self, object):
        if abs(object.x_velocity) + abs(object.y_velocity) < 15:
            if abs(self.hole[0] - object.x) + abs(self.hole[1] - object.y) < 13:
                object.inhole = True


def draw_and_check_power(x, y, memb):
    memb.hits += 1
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        pygame.time.delay(50)
        x2, y2 = pygame.mouse.get_pos()
        length = abs(x2 - x) + abs(y2 - y)
        power_x = x2 - x
        power_y = y2 - y
        color = "white"
        if length <= 50:
            color = "green"
        if 50 < length <= 100:
            color = "yellow"
        if 100 < length:
            color = "red"
        screen.fill((235, 235, 235))
        current_map.draw_map()
        pygame.draw.line(screen, pygame.Color(color), (x, y), (x2, y2), 5)
        draw_players(nr_of_players)
        if length == 0:
            length = 1
        min_x = power_x / length
        min_y = power_y / length
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if length > 105 and length != 0:
                new_x = power_x
                new_y = power_y
                while length > 105 and length != 0:
                    new_x -= min_x
                    new_y -= min_y
                    if power_x * new_x < 0:
                        new_x = 0
                    if power_y * new_y < 0:
                        new_y = 0
                    length = abs(new_x) + abs(new_y)
                return new_x, new_y
            return power_x, power_y


players = []

scoreboard = []


def add_players(nop, xx, yy):
    for i in range(nop):
        players.append(ball(xx, yy, i + 1))
        scoreboard.append([])


def draw_players(nop):
    for i in range(nop):
        if not players[i].inhole:
            screen.blit(players[i].color, (players[i].x - 8, players[i].y - 8))

def move_player(nr):
    player = players[nr]
    current_map.check_texture(player)
    slow = player.slow
    sum_vel = abs(player.x_velocity) + abs(player.y_velocity)
    if player.x_velocity != 0:
        player.t_vel_x = player.x_velocity
        player.correct_x = True
    if player.y_velocity != 0:
        player.t_vel_y = player.y_velocity
        player.correct_y = True
    while player.correct_x or player.correct_y:
        pom_x, wall_y1, wall_y2, wall_x = current_map.check_hit_x(player.x + player.t_vel_x, player.y + player.t_vel_y, player)
        pom_y, wall_x1, wall_x2, wall_y = current_map.check_hit_y(player.y + player.t_vel_y, player.x + player.t_vel_x, player)
        if pom_x + pom_y == -2:
            if player.t_vel_x >= 0 and wall_x <= wall_x1 and wall_x <= wall_x2:
                pom_y *= -1
            elif player.t_vel_x < 0 and wall_x >= wall_x1 and wall_x >= wall_x2:
                pom_y *= -1
            if player.t_vel_y >= 0 and wall_y <= wall_y1 and wall_y <= wall_y2:
                pom_x *= -1
            elif player.t_vel_y < 0 and wall_y >= wall_y1 and wall_y >= wall_y2:
                pom_x *= -1
        player.x_velocity *= pom_x
        player.y_velocity *= pom_y
        player.t_vel_x *= pom_x
        player.t_vel_y *= pom_y
    player.bounce = 0
    current_map.check_in_hole(player)
    player.x += player.t_vel_x
    player.y += player.t_vel_y
    if sum_vel != 0:
        x_slow = (abs(player.x_velocity) / sum_vel) * slow
        y_slow = (abs(player.y_velocity) / sum_vel) * slow
    else:
        x_slow = 0
        y_slow = 0
    if player.x_velocity > 0:
        player.x_velocity -= x_slow
    elif player.x_velocity < 0:
        player.x_velocity += x_slow
    if player.y_velocity > 0:
        player.y_velocity -= y_slow
    elif player.y_velocity < 0:
        player.y_velocity += y_slow
    if abs(player.x_velocity) < x_slow:
        player.x_velocity = 0
    if abs(player.y_velocity) < y_slow:
        player.y_velocity = 0


def check_everyone(memb):
    for i in range(len(memb)):
        if not memb[i].inhole:
            return False
    return True


nr_of_players = int(input("Podaj ilość graczy: 1-4: "))
while nr_of_players < 1 or nr_of_players > 4:
    nr_of_players = int(input("Błedna ilość graczy! Podaj ilość graczy: 1-4: "))

window_size = (1500, 1000)
screen = pygame.display.set_mode(window_size)

screen.fill((235, 235, 235))

balls = {
    1: pygame.image.load("textures//golf.png").convert_alpha(),  # red
    3: pygame.image.load("textures//golf_3.png").convert_alpha(),  # green
    2: pygame.image.load("textures//golf_2.png").convert_alpha(),  # blue
    4: pygame.image.load("textures//golf_4.png").convert_alpha()  # yellow
}

player_colors = {
    0: "RED",
    1: "BLUE",
    2: "GREEN",
    3: "YELLOW"
}

current_map = mapi()
add_players(nr_of_players, current_map.spawn_x, current_map.spawn_y)
close = False
fullscreen = False

for i in range(len(lm.holes)):
    if close:
        break
    current_map.create_map(i + 1)
    run = True
    for p in range(len(players)):
        players[p].inhole = False
        players[p].down = False
        players[p].x = current_map.spawn_x
        players[p].y = current_map.spawn_y
    active = 0
    while run:
        if keys[pygame.K_f]:
            if fullscreen:
                screen = pygame.display.set_mode(window_size)
                fullscreen = False
            else:
                screen = pygame.display.set_mode((window_size), pygame.FULLSCREEN)
                fullscreen = True
        screen.fill((235, 235, 235))
        pygame.time.delay(40)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                run = False
        current_map.draw_map()
        draw_players(nr_of_players)

        pygame.display.set_caption(f"Hits: {players[active].hits} - Moving... {player_colors[active]}")
        if keys[pygame.K_ESCAPE]:
            close = True
            break
        if players[active].inmove:
            if players[active].x_velocity != 0 or players[active].y_velocity != 0:
                move_player(active)
            else:
                players[active].ckx = players[active].x
                players[active].cky = players[active].y
                active += 1
                active %= nr_of_players
                if check_everyone(players):
                    run = False
                if not players[active].inhole:
                    players[active].inmove = False
        else:
            if players[active].hits > 13:
                players[active].hits = 20
                players[active].inhole = True
                players[active].inmove = True
                players[active].x = current_map.hole[0]
                players[active].y = current_map.hole[1]
                if check_everyone(players):
                    run = False
            if keys[pygame.K_0]:
                players[active].x = current_map.spawn_x
                players[active].y = current_map.spawn_y
            if keys[pygame.K_LEFT]:
                power = draw_and_check_power(players[active].x, players[active].y, players[active])
                players[active].x_velocity += power[0]
                players[active].y_velocity += power[1]
                players[active].inmove = True

        pygame.display.update()
    for l in range(len(scoreboard)):
        scoreboard[l].append(players[l].hits)
        players[l].hits = 0

winner = sum(scoreboard[0])
winners = []
for i in range(len(players)):
    if winner > sum(scoreboard[i]):
        winners.clear()
        winners.append(i)
        winner = sum(scoreboard[i])
    elif winner == sum(scoreboard[i]):
        winners.append(i)

for i in range(len(players)):
    if i in winners:
        print(f"Player {i + 1}: {scoreboard[i]} - {sum(scoreboard[i])} points - K I N G !")
    else:
        print(f"Player {i + 1}: {scoreboard[i]} - {sum(scoreboard[i])} points")
pygame.quit()
