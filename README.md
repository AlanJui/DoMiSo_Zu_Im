# 專案摘要

透過實作，評估【135 拼音法】發展【注音輸入法】之可行性。

## 專案目標

本專案試行之輸入法，需滿足以下需求規格：

- 【拼音系統】：135拼音法（DoMiSo拼音法）
- 【字典編碼】：漢字讀音編碼採【台羅拼音】/【台灣拼音+（TLPA+）】
- 【輸入類型】：注音輸入法
- 【注音符號】：極簡化方音符號，適合懶地背記按鍵位置的使用者。
- 【特性簡介】：
  1.  羅馬拼音字母，鼻化韻母採「前綴識別標示法」，如：siann ==> siaⁿ1 ==> sⁿia1 ）
  2.  【侯選清單】：採兩欄標示〔siaⁿ¹〕【ㄒㄧㆩˉ】
  3.  【聲調標示】：
    - 採【台羅八聲調】；
    - 使用數值標示聲調，以利閱讀。

## 安裝作業

RIME 在不同作業系統之間，各有不同的「軟體套件名稱」。其下載、安裝操作細節，請
參考 [Wiki](https://github.com/AlanJui/rime-tlpa/wiki) 中的操作指引文件。以下
說明為下載及安裝作業之摘要參考。

1. **下載及安裝 [RIME 中州韻輸入法引擎](http://rime.im)**；

   不同作業系統的 RIME 名稱：
   - macOS: 鼠鬚管
   - Windows: 小狼毫
   - Linux: 中州韻 (ibus-rime, fcitx-rime, fcitx5-rime)

   【註】： 由於 Linux 作業系統發布版眾多（如：Ubuntu, LinuxMint, ArchLinux）...，
   且 Linux 的各個發布版又有不同的【輸入法框架】，如：iBus, Fcitx 和 Gcin...。
   目前 RIME 在 Linux 作業系統可運作的輸入法框架，有：ibus-rime, fcitx-rime
   及 fcit5-rime 共三種。所以，在安裝 RIME 之前，得先確認 Linux 作業
   系統安裝的【輸入法框架】為何者。

2. **下載及安裝 [河洛輸入法套件包](https://github.com/AlanJui/rime-taigi/releases)
   ZIP 壓縮檔案**；

3. **編輯 RIME 設定檔準備啟用河洛輸入法**；

   RIME 設定檔名稱為：`default.custom.yaml`，各作業系統之 RIME 設定檔存放
   `目錄路徑（資料夾）`條列如下：
   - 鼠鬚管(macOS)：`~/Library/Rime/`

   - 小狼毫(Windows)：`"%APPDATA%\Rime"`

   - 中州韻(Linux)：`~/.config/ibus/rime/`

4. **重新部署 RIME 輸入法**：將作業系統使用中的輸入法，先切換成 RIME，再執行 RIME
   輸入法中的「重新部署」指令。

## 輸入法鍵盤

<img alt="image" src="https://github.com/user-attachments/assets/737558c8-e04d-458a-b3a7-2f5b601595f9" />

## 聲調按鍵

<img alt="image" src="https://github.com/user-attachments/assets/996c8da9-add8-4340-92bc-3273879f171d" />


### 四聲八調調名與調值

<img width="970" height="337" alt="image" src="https://github.com/user-attachments/assets/ceeb0903-ab26-40f4-a5b0-41953c5e82d0" />

<img width="954" height="692" alt="image" src="https://github.com/user-attachments/assets/2a9bb132-a38b-4bf5-b289-d72c1ca5b6d7" />


### W聲調圖
<img alt="image" src="https://github.com/user-attachments/assets/dc785e8f-01f0-4d00-be7d-dc64275cc170" />




## 字形

以下建議使用之字形，均為開源、免費字形：

- [思源黑體](https://github.com/adobe-fonts/source-han-sans)

- [Noto Sans Traditional Chinese](https://fonts.google.com/noto/specimen/Noto+Sans+TC)

- [字咍](https://github.com/ButTaiwan/taigivs/releases)

- [豆腐烏](https://github.com/glll4678/tshiuthau)

- [Fira Sans](https://github.com/mozilla/Fira)


