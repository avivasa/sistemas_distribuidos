from flask import Flask, render_template, send_file
import random

app = Flask(__name__)

def get_user_bandwidth():
    return random.uniform(0.5, 6)

def get_video_path(bandwidth):
    if bandwidth >= 5:
        return "static/videos/sample_1080p.mp4"
    elif bandwidth >= 3:
        return "static/videos/sample_720p.mp4"
    else:
        return "static/videos/sample_480p.mp4"

@app.route('/')  
def index():
    bandwidth = get_user_bandwidth()
    video_path = get_video_path(bandwidth)
    print(f"[INFO] Banda do usuário: {bandwidth:.2f} Mbps | Qualidade simulada: {bandwidth} | Video = {video_path}")
    return render_template('index.html', video_file=video_path)

@app.route('/stream')
def stream_video():
    bandwidth = get_user_bandwidth()
    print(bandwidth)
    video_path = get_video_path(bandwidth)
    quality_label = video_path.split('/')[-1].replace('sample_', '').replace('.mp4', '')

    print(f"[INFO] Banda do usuário: {bandwidth:.2f} Mbps | Qualidade simulada: {quality_label}")
    
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
