import pygame
from constants import *

def main():
    print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

    pygame.init()
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cx, cy = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()
    accum = 0.0
    radius = 20
    speed = 5
    dt = 0
    ax = 300.0
    vx = 0.0
    x = 100.0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
# 1) Input
        keys = pygame.key.get_pressed()
        ax = 300.0 if keys[pygame.K_RIGHT] else 0.0

# 2) Accelerate
        vx = min(vx, 600.0)

# 3) proportional damping (drag)
        drag = 1.4  # try 0.5–4.0
        if ax == 0:               # optional: only when no input
            vx -= vx * drag * dt  # shrinks vx toward 0

# 4) deadzone clamp
        if abs(vx) < 1e-3:
            vx = 0.0

# 5) integrate position
        x += vx * dt

        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        dy = (keys[pygame.K_DOWN]  - keys[pygame.K_UP])

        if dx or dy:
            length = (dx*dx + dy*dy) ** 0.5
            nx, ny = dx / length, dy / length
            cx += int(round(nx * speed))
            cy += int(round(ny * speed))

        # keep within screen bounds
        cx = max(radius, min(SCREEN_WIDTH - radius, cx))
        cy = max(radius, min(SCREEN_HEIGHT - radius, cy))
       
        screen.fill("black")
        pygame.draw.circle(screen, "white", (cx, cy), 20)
        
        ship_rect = pygame.Rect(int(x), 200, 40, 20)
        pygame.draw.rect(screen, (200, 240, 255), ship_rect)
        vx += ax * dt
        x += vx * dt
        
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.tick(60) / 1000  # limit to 60 FPS
        accum += dt
        if accum >= 1.0:
            print(f"dt≈{dt:.4f} last, fps≈{1/dt:.1f}")
            accum = 0.0        

if __name__ == "__main__":
    main()
