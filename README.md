# ppt2vedio

## 1. 介绍
一个方便将PPT转为视频的工具

## 2. 使用方法

### 2.0. 环境
- python3
- ffmpeg (可使用 `brew install ffmpeg` 安装)

### 2.1. 安装依赖

```shell
pip install -r requirements.txt
```

### 2.2. 使用示例

1. asserts文件夹中有一个ppt_text.md文件，这个文件是用来存放ppt的讲稿的，ppt2video.pptx是原始文件

2. 运行如下命令，会在当前目录下生成一个很多Mp3文件和一个time.txt文件
```shell
python generate.py

# 或者
python3 generate.py --input assets/ppt_text.md --output .
```

3. 打开ppt2video.pptx，Mac下按option + F11 按键打开Visual Basic编辑器

4. 新建一个模块，将项目中insertVideos.pptm 的内容复制到模块中运行，运行时会提示赋予读取权限，选赋予

5. 运行后试试放映PPT吧，我们就可以直接通过PPT导出MP4视频了

<video src="assets/ppt2video_completed.mp4" controls>
  你的浏览器不支持 <code>video</code> 标签。
</video>
