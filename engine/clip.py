from engine import Screen
from eggdriver.resources.console import clearConsole
import moviepy.video.io.ImageSequenceClip
import os
from timeit import default_timer as timer
import shutil

def clip_images(image_folder: str = "examples", fps: int = 1, output_file: str = "my_video.mp4"):
    """
    Create a video from a folder of images. Based on code from https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
    :param image_folder: Folder containing the images.
    :param fps: Frames per second.
    :param output_file: Output file name.
    """
    image_files = [os.path.join(image_folder,img)
                for img in os.listdir(image_folder)
                if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps = fps)
    clip.write_videofile(output_file)

def render_animation(loop_function, frames_path: str, output_path: str, fps: int, seconds: int, height: int, width: int, bgcolor: list):
    clearConsole()
    auth = input(f"This will delete all files in the frames folder {frames_path}. Continue? (y/n) ")
    if auth.lower() != "y":
        return
    engine_screen = Screen(height, width, bgcolor)
    if os.path.exists(frames_path):
        shutil.rmtree(frames_path)
    os.makedirs(frames_path)
    clearConsole()
    
    start = timer()
    loop_function(engine_screen, 0)
    engine_screen.save(os.path.join(frames_path, f"example4_0.png"))
    end = timer()
    time_in_seconds = int((end - start) * seconds * fps)
    print(f"""Estimated Time: {time_in_seconds // 60}m {time_in_seconds % 60}s
Total frames: {seconds * fps}
Resolution: {width}x{height}""")

    for i in range(1, seconds * fps + 1):
        delta_time = float(i) / float(fps)
        loop_function(engine_screen, delta_time)
        engine_screen.save(os.path.join(frames_path, f"example4_{i}.png"))

    clip_images(frames_path, fps, output_path)
