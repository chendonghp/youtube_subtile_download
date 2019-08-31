# youtube_subtile_download
## Youtube字幕下载器, UI使用pyqt封装 
安装依赖:

```shell
pip install -r requirements.txt
```

## app构建:
```shell
cd youtube_subtile_download/venv
```
bundled into one executable file 
```shell
pyinstaller -F -w -i 字幕.ico -n "YouTube Playlist Subtitle Downloader" app.spec
```
one-folder bundle containing an executable
```shell
pyinstaller -w -i 字幕.ico -n "YouTube Playlist Subtitle Downloader" app.spec
```

## 打包后主窗口图标不显示问题
https://stackoverflow.com/questions/37321548/python-pyinstaller-and-include-window-icon/37321723#37321723

https://stackoverflow.com/questions/11534293/pyinstaller-wont-load-the-pyqts-images-to-the-gui/11547144#11547144