from pydub import AudioSegment
import os
import re


def natural_sort_key(s):
    # 提取文件名中的数字部分，并转换为整数，用于排序
    return [int(c) if c.isdigit() else c.lower() for c in re.split('(\d+)', s)]


def get_audio_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio) / 1000  # 音频时长，单位为秒
    return duration


def parse_mp3_files(directory):
    file_list = sorted(
        [file_name for file_name in os.listdir(directory) if file_name.startswith("video_")],
        key=natural_sort_key
    )

    with open('times.txt', 'w') as f:
        for file_name in file_list:
            file_path = os.path.join(directory, file_name)
            duration = get_audio_duration(file_path)
            duration += 0.5  # 将音频时长增加 0.5 秒
            duration_str = "{:.2f}".format(duration)  # 格式化为保留两位小数的字符串
            f.write(duration_str + '\n')


if __name__ == '__main__':
    # 指定存放mp3文件的目录路径
    mp3_directory = '.'
    parse_mp3_files(mp3_directory)
