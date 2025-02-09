import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def download_youtube_video(video_url, output_file="video.mp4"):
    try:
        print("Downloading video with yt-dlp...")
        # Use yt-dlp to download the video
        subprocess.run([
            "yt-dlp",
            video_url,
            "-o", output_file,
            "--format", "best"
        ], check=True)
        print(f"Download completed! Video saved to: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during download: {e}")
        return None

def trim_video(input_path, start_time, end_time, output_path):
    try:
        print("Trimming video...")
        video = VideoFileClip(input_path).subclip(start_time, end_time)
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Trimmed video saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred during trimming: {e}")

def convert_to_seconds(minutes, seconds):
    return minutes * 60 + seconds

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    start_time_minutes = 56
    start_time_seconds = 4
    end_time_minutes = 59
    end_time_seconds = 0
    
    start_time = convert_to_seconds(start_time_minutes, start_time_seconds)
    end_time = convert_to_seconds(end_time_minutes, end_time_seconds)
    
    output_file = "downloaded_video.mp4"
    trimmed_file = "trimmed_video.mp4"
    
    video_path = download_youtube_video(video_url, output_file)
    
    if video_path:
        trim_video(video_path, start_time, end_time, trimmed_file)
        os.remove(video_path)  # Remove the original video
        print("Original video removed.")