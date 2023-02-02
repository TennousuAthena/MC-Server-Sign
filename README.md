# QCMCSign

![license](https://badgen.net/github/license/tennousuathena/QCMCSign)
![commits](https://badgen.net/github/commits/tennousuathena/QCMCSign)


Get your own Minecraft server status signature

## Take a look
![QCMinecraft](https://i.qmcmc.cn/i/111)

## Getting Started
### With Python
```bash
git clone https://git.qmcmc.cn/qctech/QCMCSign
cd QCMCSign
pip install -r requirements.txt
python main.py
```

### With Docker
```bash
docker pull qcminecraft/qcmc-sign
docker run -d --restart always -p 8000:8000 qcminecraft/qcmc-sign
```

## Usage
View your signature at `http://localhost:8000`

## Features
- [x] Support multiple servers
- [x] Support SRV record
- [x] Support custom port
- [x] Support original Minecraft server icon
### TODO
- [ ] Support original motd color
- [ ] Support custom signature background
- [ ] Support cache
- [ ] Support dynamic signature with APNG
- [ ] Support weather effect on user's location

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

### Assets
Most assets in `assets` folder is from [Minecraft Wiki](https://minecraft-zh.gamepedia.com/Minecraft_Wiki) and [Minecraft Wiki](https://minecraft.gamepedia.com/Minecraft_Wiki) under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.

### Datasource
- The IP-GEO-LOCATION-API is from https://lite.ip2location.com/ which requires a free registration for an individual license.
- The weather data is from [Caiyun Weather](https://h5.caiyunapp.com/h5) which requires a free registration for an API key.

### Thanks
- [@jinzhijie](https://github.com/jinzhijie)
- [@amtoaer](https://github.com/amtoaer)
- [Minecraft](https://minecraft.net/)
- [mcstatus](https://pypi.org/project/mcstatus/)