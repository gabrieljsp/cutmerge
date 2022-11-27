import os
import cv2
import shutil
import subprocess
from pathlib import Path


def merger():
    # get workspace path
    wspace_path = os.getcwd() + "/wspace"

    # get folders from workspace
    frames_out_path = wspace_path + "/frames_out"
    video_out_path = wspace_path + "/video_out"
    audio_path = wspace_path + "/audio"

    # set default filename for output
    filename = "video"

    # set default framerate for output (float)
    fps = 10.0

    # read filename and fps from log file
    with open(f"{wspace_path}/log.txt", 'r') as data_file:
        for line in data_file:
            data = line.strip().split(',')
            filename = data[0]
            fps = float(data[1])    # convert str to float

    # store every processed image from frames_out
    images = []
    for f in os.listdir(frames_out_path):
        if f.endswith(".png"):
            images.append(f)

    # get w x h from the first image
    image_path = os.path.join(frames_out_path, images[0])
    frame = cv2.imread(image_path)
    cv2.imshow('video', frame)
    height, width, channels = frame.shape

    # set output
    output_vid = video_out_path + "/output.mp4"     # mp4

    # define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # be sure to use lower case
    output = cv2.VideoWriter(output_vid, fourcc, fps, (width, height))

    print("\nMerging frames, please wait...")

    for image in images:
        image_path = os.path.join(frames_out_path, image)
        frame = cv2.imread(image_path)

        # write out frame to video
        output.write(frame)

        # this will play a preview
        cv2.imshow('video', frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):  # hit `q` to exit
            break

    # release everything if job is finished
    output.release()
    cv2.destroyAllWindows()

    print(f"Successfully merge output frames to /video_out/output.mp4!\n...")

    exists_result = os.path.isdir(os.getcwd() + "/result")

    if not exists_result:
        os.makedirs(os.getcwd() + "/result")

    audio_file = Path(f"{audio_path}/{filename}.aac")

    # if audio file exists merge it, else just copy output as final upscaled file
    if audio_file.is_file():
        subprocess.run(f"ffmpeg -i {video_out_path}/output.mp4 -i {audio_file} -c copy result/upscaled.mp4",
                       shell=True,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.STDOUT)
    else:
        shutil.copyfile(f"{video_out_path}/output.mp4", "result/upscaled.mp4")

    print("Finally done!\nCheck: result/upscaled.mp4")


if __name__ == "__main__":
    # Can implement arguments
    merger()
