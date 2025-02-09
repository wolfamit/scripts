from moviepy.editor import VideoFileClip

def video_to_mp3(video_path, audio_path):
    # Load the video file
    video_clip = VideoFileClip(video_path)
    
    # Extract audio and save it as an MP3 file
    video_clip.audio.write_audiofile(audio_path, codec='mp3')
    
    # Close the video file
    video_clip.close()

# Example usage
video_path = "Vlogsp.mov"  # Path to the input video file
audio_path = "output_audio.mp3" # Path where you want to save the MP3 file
video_to_mp3(video_path, audio_path)