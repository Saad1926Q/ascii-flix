# ASCII Flix

**ASCII Flix** is a terminal-based video player that converts videos into ASCII art. This project allows users to watch videos in their terminal by displaying them as ASCII characters.

## Features

- Convert video frames into ASCII art.
- Supports both "normal" and "filled" ASCII modes.
- Extract and play audio using `pygame`.

## Installation

You can install ASCII Flix using pip:

```sh
pip install ascii-flix
```

## Usage

You can use ASCII Flix by running the command `ascii-flix` after installing the package.

### Video Requirements

To play a video on ASCII Flix, the video must be downloaded on your device in MP4 format.

### Getting the Path of the Video

For those who are unsure how to get the path of the video file:

1. **Windows**: 
   - Navigate to the folder containing your video.
   - Right-click on the video file.
   - Select "Properties".
   - In the "General" tab, you will see the "Location" of the file. Combine this with the file name to get the full path. For example, if the location is `C:\Users\YourName\Videos` and the file name is `example.mp4`, the full path will be `C:\Users\YourName\Videos\example.mp4`.

2. **Mac/Linux**:
   - Open the terminal.
   - Navigate to the directory containing your video using the `cd` command.
   - Use the `pwd` command to print the current directory path.
   - Combine this path with the video file name. For example, if `pwd` outputs `/home/yourname/videos` and your file is `example.mp4`, the full path will be `/home/yourname/videos/example.mp4`.

### Manual Script Addition

In rare cases where the `ascii-flix` command does not work after installation, you can manually add the script:

1. Locate your Python scripts directory:
   - **Windows**: This is usually located in `C:\Users\YourName\AppData\Local\Programs\Python\PythonXX\Scripts` or `C:\Users\YourName\AppData\Roaming\Python\PythonXX\Scripts` (replace `XX` with your Python version).
   - **Mac/Linux**: This is usually located in `/usr/local/bin` or `/usr/bin`.

2. Create a new script file named `ascii-flix` (without any extension) in the scripts directory.

3. Open the file in a text editor and add the following lines:

    ```python
    #!/usr/bin/env python

    from modules import HomeScreen, VideoPlayer

    def main_function():
        video_player = VideoPlayer()
        homescr = HomeScreen()
        homescr.create_logo()
        homescr.display_home_screen(video_player=video_player)

    if __name__ == "__main__":
        main_function()
    ```

4. Save the file and make it executable:
   - **Mac/Linux**: Run `chmod +x /path/to/ascii-flix` in the terminal.

5. Ensure the scripts directory is in your PATH:
   - **Windows**: Add the scripts directory to your PATH environment variable.
   - **Mac/Linux**: Add `export PATH="/path/to/scripts:$PATH"` to your `~/.bashrc` or `~/.zshrc` file and run `source ~/.bashrc` or `source ~/.zshrc`.

After these steps, you should be able to run the `ascii-flix` command from any terminal window.
