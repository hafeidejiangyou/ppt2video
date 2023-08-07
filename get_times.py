import math

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


def round_up_and_check_decimal(number):
    rounded_number = math.ceil(number)
    decimal_part = rounded_number - number

    if decimal_part < 0.2:
        rounded_number += 1
    return rounded_number


def parse_mp3_files(directory):
    file_list = sorted(
        [file_name for file_name in os.listdir(directory) if file_name.startswith("video_")],
        key=natural_sort_key
    )

    with open('times.txt', 'w') as f:
        for file_name in file_list:
            file_path = os.path.join(directory, file_name)
            duration = get_audio_duration(file_path)
            slide_time = round_up_and_check_decimal(duration)
            duration_str = "{:.0f}".format(slide_time)
            f.write(duration_str + '\n')


if __name__ == '__main__':
    # 指定存放mp3文件的目录路径
    mp3_directory = '.'
    parse_mp3_files(mp3_directory)
