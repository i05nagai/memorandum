# alfresco
ドキュメント管理システム。

## インストール
[qiita](http://qiita.com/sadayuki-matsuno/items/87fb9793b1d38ab58e18)

alfresco-community-installer-201604-linux-x64.bin`を実行すると足りないライブラリが表示されるので、yumでいれる。
基本的にlibreofficeを入れればことたりるはず。

```
sudo yum install libreoffice
```

```
sudo yum install fontconfig libSM libICE libXrender libXextlibcups libGLU
```


```
---------------------------------------------------------------------------
Tomcat Port Configuration

Enter your Tomcat configuration parameters.

Web Server Domain: [127.0.0.1]: 52.192.140.198

Tomcat Server Port: [8080]:

Tomcat Shutdown Port: [8005]:

Tomcat SSL Port: [8443]:

Tomcat AJP Port: [8009]:

----------------------------------------------------------------------------
LibreOffice Server Port

Enter the port that the LibreOffice Server will listen to.

LibreOffice Server Port: [8100]:

----------------------------------------------------------------------------
Alfresco FTP Port

Choose a port number for the integrated Alfresco FTP server.

Port: [21]:

---------------------------------------------------------------------------
```

```
Using CATALINA_BASE:   /opt/alfresco/tomcat
Using CATALINA_HOME:   /opt/alfresco/tomcat
Using CATALINA_TMPDIR: /opt/alfresco/tomcat/temp
Using JRE_HOME:        /opt/alfresco/java
Using CLASSPATH:       /opt/alfresco/tomcat/bin/bootstrap.jar:/opt/alfresco/tomcat/bin/tomcat-juli.jar
Using CATALINA_PID:    /opt/alfresco/tomcat/temp/catalina.pid
Tomcat started.
/opt/alfresco/tomcat/scripts/ctl.sh : tomcat started
README
```

### ubuntu
ubuntuの場合`en_US.UTF-8`にしておく必要がある。
```shell
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANG_ALL=en_US.UTF-8
```

ubuntuの場合はインストールした場所`/opt/alfresco-community/`の`alfresco.sh`を実行することでサービスを起動する。
```shell
sudo sh /opt/alfresco-community/alfresco.sh start
```


### libre officeの設定
officeのプレビューができない
```shell
# Libre Office
SOFFICE_PATH="/opt/alfresco/libreoffice/program"
SOFFICE_PORT="8100"
SOFFICEBIN=/opt/alfresco/libreoffice/program/.soffice.bin
SOFFICEWRAPPER=/opt/alfresco/libreoffice/program/soffice.bin
#SOFFICE="$SOFFICEWRAPPER --nofirststartwizard --nologo --headless --accept=socket,host=localhost,port=$SOFFICE_PORT\;urp\;StarOffice.ServiceManager"   #← コメントアウト
SOFFICE="$SOFFICEWRAPPER --nofirststartwizard --nologo --headless --accept=socket,host=localhost,port=$SOFFICE_PORT;urp;StarOffice.ServiceManager" #← 追加
SOFFICE_STATUS=""
```

libre officeをいれる
```shell
sudo apt-get install libreoffice
```

## MySQL
* MySQL connectorのインストールは`TOMCAT_HOME/lib`にJARファイルをおく。
[公式ドキュメン](http://docs.alfresco.com/4.0/tasks/mysql-config.html)

##

