#!/usr/bin/python3
class UserInfoDTO(object):
    def __init__(self, data={}):
        self.name = None
        self.gender = None
        if "userInfo" in data:
            if "name" in data["userInfo"]:
                self.name = data["userInfo"]["name"]
            if "gender" in data["userInfo"]:
                self.gender = data["userInfo"]["gender"]

    @property
    def toJson(self):
        return dict({
            "name": self.name,
            "gender": self.gender
        })


class ConfigDTO(object):
    def __init__(self, data={}):
        self.userInfo = UserInfoDTO(data)

    @property
    def toJson(self):
        return dict({
            "userInfo": self.userInfo.toJson
        })
