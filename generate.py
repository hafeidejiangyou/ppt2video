# -*- coding: utf-8 -*-
import argparse
import os

from get_times import natural_sort_key, parse_mp3_files
from tts import get_one_voice, get_one_voice_with_ssml

before_yun_professional = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="zh-CN">
    <voice name="zh-CN-YunyangNeural">
        <mstts:express-as style="narration-professional">
"""

before_yun = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
    <voice name="zh-CN-YunyangNeural">
        <prosody rate="-9%" pitch="0%">
"""

before_xiao_xiao = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
    <voice name="zh-CN-XiaoxiaoNeural">
        <prosody rate="0%" pitch="0%">
"""

after = """
        </prosody>
    </voice>
</speak>
"""

after_yun_professional = """
        </mstts:express-as>
    </voice>
</speak>
"""


def split_and_save(input_file, output_path):
    # 读取输入文件
    with open(input_file, 'r') as f:
        content = f.read()

    # 使用空行进行内容分割
    blocks = [block.strip() for block in content.split('\n\n') if block.strip()]

    # 将分割后的每一块内容写入以顺序命名的文件
    for i, block in enumerate(blocks, start=1):
        output_file = f"{output_path}/p_{i}.xml"
        with open(output_file, 'w') as f:
            f.write(before_yun_professional)
            f.write(block)
            f.write(after_yun_professional)
        # output_file = f"p_{i}.txt"
        # with open(output_file, 'w') as f:
        #     f.write(block)

    print("文件已成功分割并保存！")


def parseArgs():
    parser = argparse.ArgumentParser(description='text2video')
    parser.add_argument('--input', dest='input', help='文稿路径', type=str, required=False)
    parser.add_argument('--output', dest='output', help='保存mp3文件的路径', type=str, required=False)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parseArgs()
    text_path = args.input if args.input else 'assets/ppt_text.md'
    output_path = args.output if args.output else '.'  # 保存mp3文件的路径

    # 1. 分割文本
    split_and_save(text_path, output_path)

    # 2. 获取mp3,这里使用tts脚本，也可以使用软件
    file_list = sorted(
        [file_name for file_name in os.listdir(output_path) if file_name.startswith("p_")],
        key=natural_sort_key
    )
    for file_name in file_list:
        output_name = file_name.replace('.xml', '.wav').replace('p_', 'video_')
        get_one_voice_with_ssml(file_name, output_name)

    # 3. 获取mp3时间生成time.txt
    mp3_directory = '.'
    parse_mp3_files(mp3_directory)
