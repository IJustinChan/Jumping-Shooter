import pygame

class Sprite:
    """
     Template to create sprites
     """

    def __init__(self, width=1, height=1, color=(255, 255, 255), x=0, y=0, speed=8):
        # attributes
        self.__width = width
        self.__height = height
        self._dim = (self.__width, self.__height)
        self.__x = x
        self.__y = y
        self.__pos = (self.__x, self.__y)
        self._color = color
        self.__speed = speed
        self._SURFACE = pygame.Surface

    # Setters
    def set_width(self, new_width):
        """
        Change the width
        :param new_width: int
        :return: None
        """
        self.__width = new_width

    def setX(self, x):
        """
        Change x-position
        :param x: int
        :return: None
        """
        self.__x = x
        self.__pos = (self.__x, self.__y)

    def setY(self, y):
        """
        Change y-position
        :param y: int
        :return: None
        """
        self.__y = y
        self.__pos = (self.__x, self.__y)

    def set_pos(self, x, y):
        """
        Change position
        :param x: int
        :param y: int
        :return: None
        """
        self.setX(x)
        self.setY(y)

    def set_speed(self, speed):
        """
        Change speed
        :param speed: float
        :return: None
        """
        self.__speed = speed

    def set_color(self, color):
        """
        Change color
        :param color: tuple
        :return: None
        """
        self._color = color

    # Getters
    def get_pos(self):
        return self.__pos

    def get_surface(self):
        return self._SURFACE

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_directionX(self):
        return self.__dir_x

    def get_directionY(self):
        return self.__dir_y

    def get_speed(self):
        return self.__speed

