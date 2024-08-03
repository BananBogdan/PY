import pygame
import sys
from box import *


class ProgectLavel:
    def __init__(self):
        pygame.init()

        self.bgcolor = (50, 50, 50)
        self.clock = pygame.time.Clock()
        info = pygame.display.Info()

        self.width = info.current_w
        self.height = info.current_h

        self.screen = pygame.display.set_mode((self.width, self.height))  # РАСШИРЕНИЕ
        self.screen_rect = self.screen.get_rect()
        pygame.mouse.set_visible(False)


        # info = pygame.display.Info()


        self.box_arr = [
            Box(self.screen, self.width, self.height, (255, 0, 0), 20),
            # Box(self.screen, self.width, self.height, (0, 255, 0), 10),
            # Box(self.screen, self.width, self.height, (0, 0, 255), 15),
        ]

        self.images = []
        for i in range(0,118):
            self.image = pygame.image.load(f"t2x2/{i}.gif")
            self.image = pygame.transform.scale(self.image, (self.box_arr[0].width, self.box_arr[0].height ))
            self.images.append(self.image)
        self.image_rect = self.image.get_rect()

        self.loop = 0
        print(self.box_arr[0].x)
        print(self.box_arr[0].y)




    def run_game(self):
        """ОСНОВНОЙ ЦИКЛ"""
        while True:
            self._check_events()
            for box in self.box_arr:
                box.move_box()
            self._update_screen()
            self.screen.blit(self.image, self.image_rect)
            

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


        self.image_rect.x = self.box_arr[0].x
        self.image_rect.y = self.box_arr[0].y
        self.screen.blit(self.images[self.loop], self.image_rect)

        self.loop += 1
        if self.loop >= 117:
            self.loop = 0

        # for box in self.box_arr:
        #     box.rectCeate()
        pygame.display.flip()
        self.clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    pg_game = ProgectLavel()
    pg_game.run_game()
