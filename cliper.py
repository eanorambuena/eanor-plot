import os
import moviepy.video.io.ImageSequenceClip

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
