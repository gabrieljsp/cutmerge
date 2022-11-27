import os
import cv2
import subprocess


def cutter(src):
    # read video from src
    source = cv2.VideoCapture(src)

    # check and create workspace folder
    exists_workspace = os.path.isdir(os.getcwd() + "/wspace")

    if not exists_workspace:
        os.makedirs(os.getcwd() + "/wspace")

    # get workspace path
    wspace_path = os.getcwd() + "/wspace"

    # get video fps
    video_fps = source.get(cv2.CAP_PROP_FPS)

    # get framerate
    total_frames = int(source.get(cv2.CAP_PROP_FRAME_COUNT))

    # get current frame
    ret, frame = source.read()

    exists_frames = os.path.isdir(wspace_path + "/frames")

    if not exists_frames:
        os.makedirs(wspace_path + "/frames")

    print("\nWorking on frames, please wait ...")

    count = 0

    # will run while (ret) have a new frame
    while ret:
        cv2.imwrite(f"{wspace_path}/frames/{str(count).zfill(3)}.png", frame)  # save frame as PNG file
        ret, frame = source.read()
        count += 1

    print(f"Successfully extracted {total_frames} frames!\n...")

    exists_audio = os.path.isdir(wspace_path + "/audio")

    if not exists_audio:
        os.makedirs(wspace_path + "/audio")

    print("Working on audio, please wait ...")

    filename, ext = os.path.splitext(src)

    # need "ffmpeg.exe" locally! add ENV_VAR or put in this folder
    subprocess.call(["ffmpeg", "-y", "-i", src, f"{wspace_path}/audio/{filename}.aac"],     # acc
                    shell=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

    print(f"Successfully extracted {filename}.aac audio!\n...")

    # save logs
    with open(f"{wspace_path}/log.txt", "w") as file:
        file.write(f"{filename},{video_fps}")

    exists_frames_out = os.path.isdir(wspace_path + "/frames_out")

    if not exists_frames_out:
        os.makedirs(wspace_path + "/frames_out")

    exists_video_out = os.path.isdir(wspace_path + "/video_out")

    if not exists_video_out:
        os.makedirs(wspace_path + "/video_out")

    print("Cut process complete!")


if __name__ == "__main__":
    import sys
    import getopt

    arg_src = "video.mp4"   # Default source
    arg_help = "{0} -s <source>".format(sys.argv[0])

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:", ["help", "src="])

    except NameError:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)
            sys.exit(2)
        elif opt in ("-s", "--src"):
            arg_src = arg

    cutter(arg_src)
