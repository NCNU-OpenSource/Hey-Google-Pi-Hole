# [嘿!Google, 屁洞殺!!!](https://docs.google.com/presentation/d/13Ox3-0S7Y-E6UJ-6Av-g10Xk7xGmeugBuY0OzHJ47Sw/edit#slide=id.p)

## Bot_id
@GooglePiHolebot

## 功能
- Google Assistant
- Pi-Hole
- 狼人殺（Beta試用版）

## 使用技術
- Google Cloud Platform
- Dialogflow
- Google Action Console
- Telegram Bot

## 設備
- Raspberry Pi 4 Model B
- Harman Kardon 音響
- YETI MIC

## Bot Command
- 嘿!Google!
- 為什麼愛說謊
- 遊戲開始

## 分工
- 題目討論: 謝其佑 林子揚 何文睿
- 狼人殺邏輯撰寫(.py): 何文睿
- Git文件整理: 林子揚
- 簡報製作: 林子揚 謝其佑
- 硬體設定及提供:謝其佑
- 踩雷:謝其佑 林子揚
- DilogFlow對話設定: 謝其佑 林子揚

### Google Assistant
- [套件安裝:](https://developers.google.com/assistant/sdk/guides/service/python/embed/install-sample1)

![](https://i.imgur.com/EnomLNK.png)
![](https://i.imgur.com/EGSeaTz.png)
![](https://i.imgur.com/okylNTX.png)
![](https://i.imgur.com/lZPpXwt.png)

### Dialogflow
- [DialogFlow 樹狀對話設定:](https://dialogflow.cloud.google.com/#/agent/01cf49c2-062e-40b5-a475-85b8901e646c/intents)
#### 如何設計一個對話：
- 新增專案
![](https://i.imgur.com/YEwIOmD.png)
- 控制介面
![](https://i.imgur.com/QPNMBXD.png)
- 設定Agent名字
![](https://i.imgur.com/zaZdJQB.png)
- 動作介面
![](https://i.imgur.com/9Qyge8m.png)
- 新增動作
![](https://i.imgur.com/6ACg6fo.png)
- 可以選內建的類型，或者選擇custom進入Dialogflow
![](https://i.imgur.com/ckMW7Qu.png)
#### 使用Dialogflow:
- Intent總覽
![](https://i.imgur.com/MnE8Lre.png)
- Training Phase (Input)
![](https://i.imgur.com/EiH5JOg.png)
- Response (Output)
![](https://i.imgur.com/ksgoVsb.png)
- Intergration(外部串連)
![](https://i.imgur.com/nCnNNVG.png)
這裡不一定要串到GoogleAssistant，也可以餵給TelegramBot或其他的聊天機器人


### 踩雷
- 樹梅派成功安裝官方Google Assistant (Python)，但無法使用中文，且無法自定義程式，且無法調用 local commend。

    - 嘗試使用官方提供的自定義流程：
        - => 在Dialogflow自定義樹狀對話
        - => 在Action Console上運行雲端版 Google Assistant
        - => 以Webhook的方式串流到樹梅派
    - 結果：**認定失敗，放棄**
    - 原因：
        - 依然無法使用中文，這樣等於失去屁洞殺的存在意義。
        - Webhook需要將Action 透過官方Publish，此階段需要經過官方審核。
        - Dialogflow 樹狀對話的設計方式，無法滿足狼人殺的遊戲流程，僅能實現簡單的對話機器人。

### 繼續踩雷
- 嘗試運行 AIY assistant_library_with_local_commands_demo.py
（看起來有一絲希望能在樹梅派上運行自定義程式以及調用 local commend)

- 結果：
SDK不支援AIY套件，放棄。


- 後來發現不能使用中文的原因：
 Google助理本身支援中文，但是在SampleCode裡面設定default language為zh-TW後，整支程式無法啟動，進一步研究後發現Google Assistant Sdk不支援中文。


### Demo
- Google Assitant 無法理解 “屁洞殺”
    - 解決辦法：
把跟他說 “屁洞殺” 有可能會出現的結果全部設定進去。
最常出現的是 “氣動砂” 和 “綠豆沙”

![](https://i.imgur.com/OVhnhCS.png)
- 簡單測試
![](https://i.imgur.com/eIzMd8e.png)
- 呼叫屁洞殺
![](https://i.imgur.com/mUvFr9e.png)
- 開始遊戲
![](https://i.imgur.com/dJ5AOB1.png)
![](https://i.imgur.com/61V5TH5.png)
- 天黑請閉眼
![](https://i.imgur.com/DYqcyhj.png)
- 狼人請張眼
![](https://i.imgur.com/9N2uXhd.png)
- Game Over
依輸入號碼作為變數選擇殺死對象
![](https://i.imgur.com/Q8gPlK8.png)



- Demo 流程
![](https://i.imgur.com/8bTgTeJ.png)