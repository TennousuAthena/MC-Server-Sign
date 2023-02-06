import linecache
import os
from libs import caiyun


class Ip2loc:
    file_path = r'data/IP2LOCATION-LITE-DB5.CSV'

    rows = 3123919

    def __init__(self) -> None:
        if not os.path.exists(self.file_path):
            print("Failed to find datasource")
            exit()

    def get_line_context(self, line_number, file_path=file_path) -> list:
        # print(f"Text on line{line_number} is:")
        result = linecache.getline(file_path, line_number).strip().replace('"', '').split(",")
        # print(result)
        return result

    def binarySearch(self, left: int, right: int, x: int) -> int:
        if right >= left:
            mid = int(left + (right - left) / 2)
            mid_ip = int(self.get_line_context(mid)[0])
            # 元素整好的中间位置
            if mid_ip == x:
                return mid
                # 元素小于中间位置的元素，只需要再比较左边的元素
            elif mid_ip > x:
                return self.binarySearch(left, mid - 1, x)
                # 元素大于中间位置的元素，只需要再比较右边的元素
            else:
                return self.binarySearch(mid + 1, right, x)
        else:
            print("Not Exact Value")
            return left

    def get_loc(self, ip: int) -> list:
        return self.get_line_context(self.binarySearch(0, self.rows, ip))

    int2ip = lambda x: '.'.join([str(x / (256 ** i) % 256) for i in range(3, -1, -1)])
    ip2int = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])


def get_weather() -> dict:
    token = os.getenv("CAIYUN_TOKEN")
    if not token:
        raise Exception("No token found")
    w = caiyun.Weather(token)
    loc = Ip2loc()
    lat, lon = loc.get_loc(16777472)[6:8]
    return w.get_weather(lat, lon)
