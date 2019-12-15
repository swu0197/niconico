#ソフトウェアの更新
takepon@niconico:~$ sudo apt update && sudo apt upgrade

#グラフィックスドライバのインストール（nouveau⇨nvidia）
takepon@niconico:~$ ubuntu-drivers devices
takepon@niconico:~$ sudo ubuntu-drivers autoinstall
takepon@niconico:~$ reboot

#グラフィックスドライバのインストール（nvidia⇨nvidia最新版）
ctrl+F2(console_mode)
takepon@niconico:~$ cd Downloads/
takepon@niconico:~$ systemctl isolate multi-user.target
takepon@niconico:~$ sudo chmod 755 NVIDIA-Linux-*
takepon@niconico:~$ sudo ./NVIDIA-Linux-x86_64-440.44.run
takepon@niconico:~$ systemctl start graphical.target
takepon@niconico:~$ reboot

#フォルダ名を日本語から英語にする
takepon@niconico:~$ LANG=de_DE.utf8 xdg-user-dirs-gtk-update

#VSCodeを半透明にする
takepon@niconico:~$ sudo apt-get install devilspie
takepon@niconico:~$ mkdir -p ~/.devilspie
takepon@niconico:~$ sudo gedit ~/.devilspie/vscode_transparent.ds
( if
( contains ( window_class ) "Code" )
( begin
( spawn_async (str "xprop -id " (window_xid) " -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0xdfffffff") )
)
)
takepon@niconico:~$ devilspie &

#Dockerのインストール
https://qiita.com/myyasuda/items/cb8e076f4dba5c41afbc
#nvidia-docker2のインストール
https://note.com/setoyama60jp/n/n127735849c14

#Docker build
detectron
https://github.com/facebookresearch/Detectron/issues/807
detectron2(cuda101)
https://github.com/facebookresearch/detectron2/tree/master/docker
colmap(cuda102)
https://github.com/colmap/colmap/blob/dev/docker/Dockerfile