import os

from get_times import natural_sort_key, parse_mp3_files
from tts import get_one_voice

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


def split_and_save(input_file):
    # 读取输入文件
    with open(input_file, 'r') as f:
        content = f.read()

    # 使用空行进行内容分割
    blocks = [block.strip() for block in content.split('\n\n') if block.strip()]

    # 将分割后的每一块内容写入以顺序命名的文件
    for i, block in enumerate(blocks, start=1):
        output_file = f"p_{i}.xml"
        with open(output_file, 'w') as f:
            f.write(before_xiao_xiao)
            f.write(block)
            f.write(after)
        # output_file = f"p_{i}.txt"
        # with open(output_file, 'w') as f:
        #     f.write(block)

    print("文件已成功分割并保存！")


if __name__ == '__main__':
    text_directory = '.'

    # 1. 分割文本
    split_and_save('assets/ppt_text.md')

    # 2. 获取mp3,这里使用tts脚本，也可以使用软件
    file_list = sorted(
        [file_name for file_name in os.listdir(text_directory) if file_name.startswith("p_")],
        key=natural_sort_key
    )
    for file_name in file_list:
        output_name = file_name.replace('.xml', '').replace('p_', 'video_')
        get_one_voice(file_name, output_name)

    # 3. 获取mp3时间生成time.txt
    mp3_directory = '.'
    parse_mp3_files(mp3_directory)
