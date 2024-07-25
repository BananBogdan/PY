import pygame
import sys

class ProgectLavel():
    def __init__(self):
        self.bgcolor = (50,50,50)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (800, 600)
            ) # РАСШИРЕНИЕ
        self.screen_rect = self.screen.get_rect()
        pygame.mouse.set_visible(False)

    def run_game(self):
        """ ОСНОВНОЙ ЦИКЛ """
        while True:
            self._check_events()
            self._update_screen()
#/////////////////////////////////////////////////////////////// ДАЛЕЕ МОДУЛИ "RUN_GAME" //////////////////////////////////////////
    #================= ИВЕНТЫ КНОПКИ ============================
    def _check_events(self):
        """ Проверка ивентов """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    #================= //НАЖАТИЕ КНОПКИ// ============================
#/////////////////////////////////////////////////////////////// КОНЕЦ "RUN_GAME" //////////////////////////////////////////

    def _update_screen(self):
        """ ОТРИСОВКА ЭКРАНА """
        self.screen.fill(self.bgcolor)
        # Отображение полследнего прорисованого экрана
        pygame.display.flip()
        self.clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    pg_game = ProgectLavel()
    pg_game.run_game() 