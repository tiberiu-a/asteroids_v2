import pygame

from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        print(dt)        
    


if __name__ == "__main__":
    main()
