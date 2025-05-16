from flask import Flask, render_template, send_file, request

app = Flask(__name__)

def get_video_path(bandwidth):
    if bandwidth >= 5:
        return "static/videos/sample_1080p.mp4", "1080p"
    elif bandwidth >= 3:
        return "static/videos/sample_720p.mp4", "720p"
    else:
        return "static/videos/sample_480p.mp4", "480p"

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/stream')
def stream_video():
    bandwidth = float(request.args.get('bandwidth', 3.0))
    video_path, quality_label = get_video_path(bandwidth)

    print(f"[INFO] Banda do usuário: {bandwidth:.2f} Mbps | Qualidade simulada: {quality_label}")
    
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
