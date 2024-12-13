import os
import ffmpeg

def apply_format(source_file, target_file, output_path):
    # 获取源文件的格式和参数
    ap = ffmpeg.probe(source_file)
    
    # 从 ap 中提取必要的参数
    # 假设我们只需要编码器和容器信息（这些可能因需求而不同）
    # 提取视频流信息
    video_streams = [s for s in ap['streams'] if s['codec_type'] == 'video']
    # 提取音频流信息
    audio_streams = [s for s in ap['streams'] if s['codec_type'] == 'audio']

    # 假设我们只处理第一个视频流和第一个音频流
    if video_streams:
        video = video_streams[0] # 获取第一个视频流
        video_codec = video['codec_name'] # 编解码器
        video_bitrate = video['bit_rate'] # 比特率
        width = video['width'] # 宽度
        height = video['height'] # 高度
    else:
        raise Exception("No video stream found.")

    if audio_streams:
        audio = audio_streams[0]
        audio_codec = audio['codec_name'] # 编解码器
        audio_bitrate = audio['bit_rate'] # 比特率
    else:
        raise Exception("No audio stream found.")

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path, os.path.basename(target_file))

    # 使用 ffmpeg 将源文件格式和参数应用到目标文件
    ffmpeg.input(target_file).output(
        output_file,
        vcodec=video_codec,
        video_bitrate=video_bitrate,
        s=f'{width}x{height}',
        acodec=audio_codec,
        audio_bitrate=audio_bitrate
    ).run()


# 示例使用
a = '/Users/yanxuefeng/Desktop/good/logo_apj.mp4'
b = '/Users/yanxuefeng/Desktop/bad/loginVideo.mp4'
c = '/Users/yanxuefeng/Desktop/apply/'

# 将一个mp4文件的格式，应用到另一个mp4文件
apply_format(a, b, c)
