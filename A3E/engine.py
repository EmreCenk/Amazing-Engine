import sys

import pygame

from A3E.shapes import Triangle
from A3E.utils import project_triangle


class Engine():
    """Engine that will render 3D."""

    def __init__(self, width, height, background_color=(0, 0, 0)):
        """Initialize window properties."""
        self.background_color = background_color
        self.height = height
        self.width = width

        # Initialize pygame and window
        pygame.init()
        screen_size = (self.height, self.width)
        self.window = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    def start_engine(self, delay_time=100, *funcs):
        """
        Start the 3D engine.

        Functions with no parameters or for functions with parameters, lambda functions must be passed to funcs.
        """
        # Create two triangles for testing.
        self.test_triangle = Triangle([100, 100, 100], [200, 200, 100], [300, 300, 100])
        self.test_triangle_2 = Triangle([1000, 1000, 100], [2000, 2000, 100], [6000, 3000, 100])

        while True:
            pygame.time.delay(delay_time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
                if event.type == pygame.VIDEORESIZE:
                    self.width, self.height = pygame.display.get_window_size()

            # Decrement triangle 1's vertex's coordinates.
            self.test_triangle.vertex1[0] -= 1
            self.test_triangle.vertex2[0] -= 1
            self.test_triangle.vertex3[0] -= 1
            new_vertices = project_triangle(self.test_triangle.vertex1, self.test_triangle.vertex2,
                                            self.test_triangle.vertex3, self.width, self.height)

            # Decrement triangle 2's vertex's coordinates.
            self.test_triangle_2.vertex1[2] -= 1
            self.test_triangle_2.vertex2[2] -= 1
            self.test_triangle_2.vertex3[2] -= 1
            new_vertices2 = project_triangle(self.test_triangle_2.vertex1, self.test_triangle_2.vertex2,
                                             self.test_triangle_2.vertex3, self.width, self.height)

            # Draw new triangles.
            pygame.draw.polygon(self.window, points=new_vertices, color="white")
            pygame.draw.polygon(self.window, points=new_vertices2, color="blue")
            print(new_vertices)

            # Call passed functions.
            for func in funcs:
                func()

            self.update_screen()  # redraw/update the screen in every loop.

    def update_screen(self):
        """Update the screen."""
        pygame.display.update()
        self.window.fill(self.background_color)
