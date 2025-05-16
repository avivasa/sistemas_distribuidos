from flask import Flask, request, render_template, redirect, url_for, send_file
import requests
import time

app = Flask(__name__)

def estimate_bandwidth_from_url(url):
    try:
        start = time.time()
        response = requests.get(url, stream=True, timeout=5)
        total_bytes = 0
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                total_bytes += len(chunk)
                if total_bytes >= 1_000_000:  # para evitar downloads longos, limite a 1 MB
                    break
        duration = time.time() - start
        if duration == 0:
            duration = 0.01  # evitar divisão por zero
        bandwidth_mbps = (total_bytes * 8) / (duration * 1_000_000)
        return bandwidth_mbps
    except Exception as e:
        print(f"[ERRO] Falha ao medir a largura de banda: {e}")
        return 0.5  # valor baixo como fallback

def get_video_path(bandwidth):
    if bandwidth >= 5:
        return "static/videos/sample_1080p.mp4"
    elif bandwidth >= 3:
        return "static/videos/sample_720p.mp4"
    else:
        return "static/videos/sample_480p.mp4"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        bandwidth = estimate_bandwidth_from_url(url)
        video_path = get_video_path(bandwidth)
        quality = video_path.split('_')[-1].replace('.mp4', '')
        return render_template('video.html', video_path='/' + video_path, bandwidth=bandwidth, quality=quality)
    return render_template('index2.html')

@app.route('/video/<quality>')
def stream_video(quality):
    video_path = f"static/videos/sample_{quality}.mp4"
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
