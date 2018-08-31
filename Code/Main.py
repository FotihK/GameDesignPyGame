# Pygame template - skeleton for a new pygame project
import pygame
import random as rd
import Image_File as IF
import Globals as GB
import Player as PL
import Mob

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 30)
screen = pygame.display.set_mode((GB.WIDTH, GB.HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

score = 0
screen_color = GB.BLACK
num_hearts = 3

mob_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

player = PL.Player(GB.WIDTH / 2, GB.HEIGHT / 2)
mobs = []
num_enemies = 5
for i in range(0, num_enemies):
    x = rd.randint(50, GB.WIDTH - 50)
    y = rd.randint(50, GB.HEIGHT - 50)
    RGB = (rd.randint(30, 255), rd.randint(30, 255), rd.randint(30, 255))
    mobs.append(Mob.Mob(x, y, RGB, 50))

mob_sprites.add(mobs)


def gui_draw():
    screen.fill(screen_color)
    pygame.draw.rect(screen, GB.CYAN, (0, 0, GB.THICK, GB.HEIGHT), 0)
    pygame.draw.rect(screen, GB.CYAN, (GB.WIDTH - GB.THICK, 0, GB.THICK, GB.HEIGHT), 0)
    pygame.draw.rect(screen, GB.CYAN, (0, 0, GB.WIDTH, GB.THICK), 0)
    pygame.draw.rect(screen, GB.CYAN, (0, GB.HEIGHT - GB.THICK, GB.WIDTH, GB.THICK), 0)

    screen.blit(font.render(str(score), True, GB.WHITE), (15, 5))
    for i in range(0, num_hearts):
        screen.blit(IF.HEART, (GB.WIDTH - 37 - (i * 37), 5))


# Game loop
running = False
pygame.event.clear()
while not running:
    clock.tick(GB.FPS)
    gui_draw()
    screen.blit(font.render("Press any button to start!", True, GB.BLUE), (400, 400))
    screen.blit(player.image, player.rect)
    bullet_sprites.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            running = True

while running:
    # keep loop running at the right speed
    clock.tick(GB.FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            bullet_sprites.add(player.shoot())
        if event.type == pygame.QUIT:
            running = False

    if num_hearts <= 0:
        running = False
        print("You lose")

    screen_color = GB.BLACK

    for mob in mobs:
        if mob:
            col = pygame.sprite.spritecollideany(mob, mob_sprites)
            if pygame.sprite.spritecollide(mob, pygame.sprite.GroupSingle(player), False):
                mob.kill()
                mobs.remove(mob)
                num_hearts -= 1
                screen_color = GB.RED
            elif pygame.sprite.spritecollide(mob, bullet_sprites, True):
                score += mob.max * 50
                ms = mob.split()
                if ms:
                    for m in ms:
                        if m:
                            mobs.append(m)
                            mob_sprites.add(m)
                mob.kill()
                mobs.remove(mob)
                screen_color = GB.GREEN
            elif col and col != mob:
                mob.rng_speed()

    # Update
    player.update()
    bullet_sprites.update()
    mob_sprites.update()

    # Draw / render
    gui_draw()
    screen.blit(player.image, player.rect)
    bullet_sprites.draw(screen)
    mob_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
exit()
