import pygame
import time

# Initialize Pygame
pygame.init()

# Set the resolution
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

# Create a clock object to measure frame time
clock = pygame.time.Clock()

# Define the number of frames to render
num_frames = 100

# Start the frame counter
frame_count = 0

# Main loop
running = True
start_time = time.time()

while running and frame_count < num_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render a simple rectangle
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 200, 200))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

    frame_count += 1

end_time = time.time()
elapsed_time = end_time - start_time
average_frame_time = elapsed_time / num_frames
fps = 1 / average_frame_time

# Print performance information
print(f"Frames rendered: {frame_count}")
print(f"Average frame time: {average_frame_time:.4f} seconds")
print(f"Average FPS: {fps:.2f}")

# Quit Pygame
pygame.quit()
