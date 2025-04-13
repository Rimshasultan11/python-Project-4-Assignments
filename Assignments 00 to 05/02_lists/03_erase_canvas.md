# 🎨 Canvas Eraser using Pygame

## 📝 Overview
This Python project is a simple interactive canvas built using **Pygame**. It lets users drag an eraser across a grid of blue cells, turning them white as if they were erased. It's a fun and visual way to explore mouse interactions and collision detection in game development.

---

## 🔧 How It Works
1️⃣ A grid of blue cells is drawn using `pygame.draw.rect`.  
2️⃣ An eraser (white square) follows the mouse while dragging.  
3️⃣ If the eraser overlaps any cell, that cell changes color from blue to white.  

---

## 🖥️ Code Implementation
```python
import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ERASER_SIZE = 60
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BG_COLOR = (200, 200, 200)

def draw_grid(surface, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            pygame.draw.rect(surface, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Canvas Eraser 🎨")
    clock = pygame.time.Clock()

    # Create grid
    rows = HEIGHT // CELL_SIZE
    cols = WIDTH // CELL_SIZE
    grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

    dragging = False
    eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

        # Update eraser position
        if dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            eraser_rect.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

            # Erase blue cells
            for row in range(rows):
                for col in range(cols):
                    cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if eraser_rect.colliderect(cell_rect):
                        grid[row][col] = WHITE

        draw_grid(screen, grid)
        if dragging:
            pygame.draw.rect(screen, WHITE, eraser_rect, 2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
A window opens with a grid of blue cells.
When you click and drag your mouse, the eraser appears and turns the blue cells white where it moves.
```

---

## 🔗 Google Colab Notebook (Simulation Version)
**Note**: Pygame GUI apps don't run in Google Colab. But here's a [Colab Notebook](https://colab.research.google.com/drive/1s5P1nVp02x0QfG8r_kESc9cqiWHDs81b?usp=sharing). 
with a simulation using `matplotlib` to demonstrate similar behavior.

---

🎨 **Have fun erasing on your custom canvas!** 😊

