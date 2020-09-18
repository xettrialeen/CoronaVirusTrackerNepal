
import json
import requests
import os

url = "https://nepalcorona.info/api/v1/data/nepal"
country = "Nepal"
params = {'location': country}
request = requests.get(url=url, params=params)

data = request.json()
Corona_all_datas = []

# ? in here i appended the for loop data as coroana_all_datas cause
# *** sapi only takes loop value
for x, y in data.items():
    Corona_all_datas.append(f"{str(x)} : {str(y)}")


# todo creating a text to speak function


def text_to_speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


# todo if __name=="__main__" is like void main() in dart
if __name__ == "__main__":
    print("COVID-19 CASES IN NEPAL:\n")
    for j in range(len(Corona_all_datas)):

        print(j+1, Corona_all_datas[j])
        text_to_speak(Corona_all_datas[j])
        if j == 8:
            break


# print(tested_positive)
