import pygame, sys, random
#Tạo hàm cho trò chơi
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos + 432,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos - 650))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
def check_collection(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True        
def rotate_brid(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movemnet * 3, 1)
    return new_bird
def brid_animation():
    new_bird = brid_list[bird_index]
    new_brid_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_brid_rect
def score_display(game_state):
    if game_state == "main game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center =(216,100))
        screen.blit(score_surface, score_rect)
    if game_state == "game over":
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center =(216,100))
        screen.blit(score_surface, score_rect)
        
        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center =(216,630))
        screen.blit(high_score_surface, high_score_rect)           
def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 512)        
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.TTF", 40)
#Tạo các biến cho trò chơi
gravity = 0.25      
bird_movemnet = 0
game_active = True
score = 0
high_score = 0
#Chèn background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
#Chèn sàn
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#Tạo chim
bird_down = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
brid_list = [bird_down, bird_mid, bird_up]
bird_index = 0
brid = brid_list[bird_index]
#Tạo timer cho brid_rect
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)
# brid = pygame.image.load('assets/yellowbrid-midflap.png').convert_alpha()
# brid = pygame.transform.scale2x(brid)
bird_rect = brid.get_rect(center = (100,384))
#Tạo ống
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200,300,400]
#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (216,384))
#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
# die_sound = pygame.mixer.Sound('sound/sfx_die.wav')
score_sound_countdown = 100
#while loop của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movemnet = 0
                bird_movemnet = -11
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movemnet = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0 
            brid, bird_rect = brid_animation()
    screen.blit(bg,(0,0))
    if game_active:
        #Chim
        bird_movemnet += gravity
        rotated_brid = rotate_brid(brid)
        bird_rect.centery += bird_movemnet
        screen.blit(rotated_brid,bird_rect)
        game_active = check_collection(pipe_list)
        #Ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display("main game")
        score_sound_countdown -= 1
        if score_sound_countdown <=0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display("game over")
        # die_sound.play()
        
    #Sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)