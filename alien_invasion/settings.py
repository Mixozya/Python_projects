class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Настройки корабля
        self.ship_speed = 1
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (138, 6, 6)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 5

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.alien_speed = 0.1
        self.fleet_direction = 1
        self.alien_points = 25

    def increase_speeed(self):
        """Увеличивает настройки скорости"""
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
