import pygame                                                            

class Ship():
    """Класс для управления кораблём"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию"""
        self.screen = ai_game
        #self.settings = ai_game.settings
        self.screen_rect = ai_game.get_rect()
        
        
        #Загружет изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')   
        self.rect = self.image.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учётом флагов"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
            
        #Обновляет атрибут х, не rect.
        #if self.moving_right and self.rect.right < self.screen_rect.right:  
        #if self.moving_right:
         #   self.x += self.settings.ship_speed
        #if self.moving_left  and self.rect.left > 0:
        #if self.moving_left:
         #   self.x -= self.settings.ship_speed

        

         
        #Обновление атрибута rect на основании self.x .
            #self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
