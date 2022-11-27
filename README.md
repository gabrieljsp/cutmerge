
## CutMerge

CutMerge is a tool where you can extract the frames of your video to process they as you want in anyother tool like image upscalers and after this merge into a new video file.

#### FFMPEG nedded @ [download here!](https://ffmpeg.org/download.html)

Drag ffmpeg.exe in the CutMerge folder or create a environment variable.
## How to use

#### 1. Create environment:

```bash
py -m venv env
```

#### 2. Activate environment:

```bash
.\env\Scripts\activate
```

#### 3. Install packages (env):

```bash
pip install opencv-python
```

#### 4. Run cutter:

```bash
py cut.py -s "/your_dir/video.mp4"
* if you put a "video.mp4" in root, u can use simply use "py cut.py".
```

#### 5. Process your /wspace/frames folder as you want and drag processed images to /wspace/frames_out.

#### 6. Run merger:

```bash
py merge.py
```

#### Final video output will be in "/result/upscaled.mp4".

### 

This is a personal project and not represents a final product.

