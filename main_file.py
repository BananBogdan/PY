import pygame
import sys


            
     

class Box:
    def __init__(self,screen,width,height,color,speed):

        self.speed = speed
        self.color = color
        self.screen = screen
        self.width = width
        self.height = height

        self.width = 100
        self.height = 100

        self.box_up = False
        self.box_down = False
        self.box_right = False
        self.box_left = False

        self.x = ( 800 / 2 ) - ( self.width / 2) 
        self.y = ( 600 / 2 ) - ( self.height / 2 )

    def test(self):
        print('Test')





            
    def move_box(self):
            if self.box_up == True and self.y > 0:
                self.y -= self.speed
            if self.box_down == True and self.y < 500:
                self.y += self.speed
            if self.box_right == True and self.x < 700:
                self.x += self.speed
            if self.box_left == True and self.x > 0:
                self.x -= self.speed


    def rectCeate(self):
        self.rect = pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.height)
        )


class ProgectLavel:
    def __init__(self):
        self.bgcolor = (50, 50, 50)
        self.clock = pygame.time.Clock()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))  # РАСШИРЕНИЕ
        self.screen_rect = self.screen.get_rect()
        pygame.mouse.set_visible(False)


        #self.x = self.width / 2 - ( self.box_width / 2) 
        #self.y = self.height / 2 - ( self.box_height / 2 )


        self.box_arr = [ 
            Box(self.screen,self.width,self.height,(255, 0, 0), 20), 
            Box(self.screen,self.width,self.height,(0, 255, 0), 10),
            Box(self.screen,self.width,self.height,(0, 0, 255), 15)
            ]


    def run_game(self):
        """ОСНОВНОЙ ЦИКЛ"""
        while True:
            self._check_events()
            for box in self.box_arr:
                box.move_box()
            self._update_screen()
            

    # /////////////////////////////////////////////////////////////// ДАЛЕЕ МОДУЛИ "RUN_GAME" //////////////////////////////////////////
    # ================= ИВЕНТЫ КНОПКИ ============================
    def _check_events(self):
        """Проверка ивентов"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    for box in self.box_arr:    
                        box.box_up = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    for box in self.box_arr:
                        box.box_down = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    for box in self.box_arr:
                        box.box_right = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    for box in self.box_arr:
                        box.box_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                   for box in self.box_arr:
                        box.box_up = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    for box in self.box_arr:
                        box.box_down = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    for box in self.box_arr:
                        box.box_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    for box in self.box_arr:
                        box.box_left = False

    # ================= //НАЖАТИЕ КНОПКИ// ============================
    # /////////////////////////////////////////////////////////////// КОНЕЦ "RUN_GAME" //////////////////////////////////////////

    def _update_screen(self):
        """ОТРИСОВКА ЭКРАНА"""
        self.screen.fill(self.bgcolor)
        for box in self.box_arr:
            box.rectCeate()
        pygame.display.flip()
        self.clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    pg_game = ProgectLavel()
    pg_game.run_game()
