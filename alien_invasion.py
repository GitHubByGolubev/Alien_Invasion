import  sys                                                                 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализируем игру и создаем игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)                                       

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # При каждом проходе цикла перерисовывается экран
            self._chek_events()
            self.ship.update()
            self._update_screen()

    def _chek_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

                elif event.key ==pygame.K_q:
                     sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False    

                    # Переместить корабль.
                    #self.ship.rect.x += 1
                    #self.ship.rect.x -= 1
                    
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
