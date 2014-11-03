movie_subs
==========
自动扫描配置的目录以及子目录里的视频文件，调用射手网API，查找并下载字幕文件到视频文件的目录

## 配置说明：
```ini
[FOLDER]
folder=E:\BT\,D:\Movie\

[SUFFIX]
subs=.srt,.ass,.subs,.sub,.idx
movies=.mkv,.mp4,.avi
```

* **folder** 配置需要扫描的目录，以','号分隔多个目录
* **subs** 配置有效的字幕文件后缀名，以','号分隔，如果视频文件已经有对应后缀名的字幕存在，则跳过该文件
* **movies** 配置需要处理的视频文件格式，以','号分隔


## 运行：
直接运行movie_subs.exe即可


## TODO:
增加图形界面
