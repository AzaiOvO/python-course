# python-course
使用说明：<br>
1.下载zip或使用git命令行clone到本地<br>
2.后端部分<br>
（1）进入项目主目录下，运行 pip install -r requirements.txt安装需要使用的包；<br>
（2）将Config目录下的mysql_config.py文件中的数据库链接修改成自己的，使用python main.py以爬取房源数据并添加到数据库；<br>
（3）使用python app.py来运行后端，命令行会弹出运行在http://127.0.0.1:5000/上来监听前端的请求。<br>
3.前端部分<br>
（1）在node环境下进入主目录Crawler-Project\spider-react，运行npm install安装前端所需依赖包；<br>
（2）输入命令npm start启动前端，此时命令行提示前端运行在http://127.0.0.1:3000/上，复制到浏览器打开即可访问。