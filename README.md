# Collect-Ticket-Information-from-Singapore-Airline-Group-with-multiple-destinations
This is a python programme using selenium to collect ticket information from Singapore Airline Group. Easy to use, but selenium and chrome environment is required

这是一个使用selenium组件去收集新加坡航空集团从新加坡飞往中国的机票信息的软件。易于使用，但是需要提前安装好selenium和chrome环境


现在疫情期间回国困难，每天查询回国票价又太麻烦.

这个程序可以让你查询从新加坡出发，到某指定月份之前的所有航班班次和价格信息

具体请调用 CheckTicket.search("落地城市","指定日期")
CheckTicket.show()会展示最终的输出结果

## 使用须知
1.使用此程序依赖chrome浏览器和对应chrome版本的selenium driver  
2.使用前可以通过pip install -r requirements.txt安装对应的依赖库，但是selenium driver需要到官方网站自行安装  
3.使用时，记得将第81行        PATH = r"D:\anaconda\envs\WebScraping\drivers\chromedriver.exe" 的webdriver安装路径换成你自己的selenium driver  

This is the sample output:

![screenshot at 2022/06/20](https://github.com/blue-vision0/Collect-Ticket-Information-from-Singapore-Airline-Group-with-multiple-destinations/blob/main/sample.png?raw=true)
