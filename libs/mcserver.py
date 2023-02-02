import base64
import re

from mcstatus import JavaServer
import srvlookup
from PIL import ImageFont, ImageDraw, Image
from io import BytesIO


def base64_to_image(base64_str):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img


class Mcserver:
    def __init__(self, host: str, port: int = 25565, srv=False):
        if srv or port == 25565:
            self.conn_info = host.upper()
        else:
            self.conn_info = f"{host}:{port}"
        self.host = host
        self.port = port
        if srv:
            srv_record = SRV(domain=host).get_srv()
            for record in srv_record:
                try:
                    self.host = record[0]
                    self.port = record[1]
                    self.server_info = JavaServer(self.host, self.port).status()
                    self.latency = self.server_info.latency
                    break
                except Exception as e:
                    self.latency = -1
        else:
            try:
                self.server_info = JavaServer(self.host, self.port).status()
                self.latency = self.server_info.latency
            except Exception as e:
                self.latency = -1

    def get_latency_status(self):
        l = self.latency
        match l:
            case -1:
                return 0
            case l if l < 100:
                return 5
            case l if l < 300:
                return 4
            case l if l < 500:
                return 3
            case l if l < 700:
                return 2
            case _:
                return 1

    def get_img(self):
        bg_img = Image.open("assets/img/small.png")
        # 加载延迟图片
        ping_img = Image.open(f"assets/img/ping/ping{self.get_latency_status()}.png")
        ping_img = ping_img.resize((int(ping_img.size[0] / 2.57142857),
                                    int(ping_img.size[1] / 2.57142857)), Image.ANTIALIAS)
        bg_img.paste(ping_img, (575, 6), ping_img)
        if self.latency < 0:
            players = '?/?'
            description = '服务器未开启'
            icon = Image.open("assets/img/unknown_server.png")
        else:
            players = f"{self.server_info.players.online}/{self.server_info.players.max}"
            description = self.server_info.description
            if 'favicon' not in self.server_info.raw:
                icon = Image.open("assets/img/unknown_server.png")
            else:
                icon = base64_to_image(self.server_info.favicon)
        # 加载玩家数
        ttf = ImageFont.truetype("assets/font/1_Minecraft-Regular.otf", 16)
        img_draw = ImageDraw.Draw(bg_img)
        img_draw.text((515, 6), f"{players}", font=ttf,
                      fill=(168, 168, 168))
        # 加载服务器IP
        ttf = ImageFont.truetype("assets/font/Minecraft_AE.ttf", 18)
        img_draw = ImageDraw.Draw(bg_img)
        img_draw.text((80, 6), f"{self.conn_info}", font=ttf, fill=(255, 255, 255))
        # 加载服务器描述
        ttf = ImageFont.truetype("assets/font/Minecraft_AE.ttf", 16)
        img_draw = ImageDraw.Draw(bg_img)
        description = re.sub(r"§.", "", description)
        img_draw.text((80, 28), f"{description}", font=ttf, fill=(255, 255, 255))
        # 加载服务器Icon
        icon = icon.resize((64, 64), Image.ANTIALIAS)
        bg_img.paste(icon, (9, 4), icon)
        # 保存图片
        buf = BytesIO()
        bg_img.save(buf, 'png')
        return buf


class SRV:
    def __init__(self, domain='qcminecraft.com', name='minecraft'):
        self.domain = domain
        self.name = name
        try:
            self.srv = srvlookup.lookup(domain=self.domain, name=self.name)
        except Exception as e:
            self.srv = (self.domain, 25565)

    def get_srv(self):
        return self.srv
