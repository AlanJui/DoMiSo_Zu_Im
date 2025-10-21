# 專案摘要

透過實作，評估【135 拼音法】發展【注音輸入法】之可行性。

## 專案目標

本專案試行之輸入法，需滿足以下需求規格：

- 【拼音系統】：135拼音法（DoMiSo拼音法）
- 【字典編碼】：漢字讀音編碼採【台羅拼音】/【台灣拼音+（TLPA+）】
- 【輸入類型】：注音輸入法
- 【注音符號】：極簡化方音符號，適合懶地背記按鍵位置的使用者。
- 【特性簡介】：
  1.  羅馬拼音字母，鼻化韻母採「前綴識別標示法」，如下行所示；
  2.  【侯選清單】：採兩欄標示〔sⁿia5〕 【ㄒㄥㄧㄚˇ】；
  3.  【聲調標示】：
      - 採【台羅八聲調】；
      - 使用數值標示聲調，以利閱讀。

<img width="979" height="666" alt="image" src="https://github.com/user-attachments/assets/f7420b78-34cc-4506-9d03-bc59988c1338" />


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

2. **下載及安裝本專案産出之【輸入法相關檔案】**；

3. **編輯 RIME 設定檔；或使用小狼毫提供之圖形設定工具【輸入法設定】，以便啟用輸入法方案**；

   **【使用輸入法設定工具】**

   透過小狼毫提供之圖形介面（GUI）工具【輸入法設定】，安裝 RIME 輸入方案。

     <img alt="2025-10-02_13-33-12" src="https://github.com/user-attachments/assets/6eda9d74-14df-49b6-af03-9bbfb3adf662" />
   1. 將中文輸入法切換成【小狼毫】。

     <img alt="image" src="https://github.com/user-attachments/assets/68b7892d-15dd-46db-93f0-51b1ea6d896b" />
   2. 將滑鼠指標指向【小狼毫輸入法】圖示，按下【滑鼠右鍵】。

     <img alt="image" src="https://github.com/user-attachments/assets/97257079-fcf6-42a8-a77d-f2a24d396b31" />
   3. 自【快顯功能表】選擇【輸入法設定】指令。

     <img alt="image" src="https://github.com/user-attachments/assets/15471158-5944-4f6d-aa19-2442f75d3745" />
   4. 在【方案選單】可瀏覽已安裝之小狼毫輸入方案。

     <img alt="image" src="https://github.com/user-attachments/assets/d8aa05ab-6694-4544-8df4-f7348115d0c8" />
   5. 點擊【核取方塊】，當呈現【勾選】狀態，表小狼毫【啟用】該輸入方案；若呈現【取消】狀態，表小狼毫【停用】該輸入方案。

     <img alt="image" src="https://github.com/user-attachments/assets/ffd4f783-b622-4aa9-a039-215d5b6840f1" />
   6. 點擊【中】按鈕，完成【小狼毫輸入方案】之【啟用/停用】設定。

     <img alt="image" src="https://github.com/user-attachments/assets/663fd80a-d2a1-4383-823f-cd38150393ca" />
   7. 自視窗之左側，先選用【小狼毫介面風格】，然後再按【中】按鈕，完成設定。

     <img alt="image" src="https://github.com/user-attachments/assets/fb454f75-eb96-4acf-bd4f-bffe095cbbee" />

---

**【編輯 RIME 設定檔】**

RIME 設定檔名稱為：`default.custom.yaml`，各作業系統之 RIME 設定檔存放
`目錄路徑（資料夾）`條列如下：

- 鼠鬚管(macOS)：`~/Library/Rime/`

- 小狼毫(Windows)：`"%APPDATA%\Rime"`

- 中州韻(Linux)：`~/.config/ibus/rime/`

<img width="979" height="666" alt="image" src="https://github.com/user-attachments/assets/428043cf-db8e-4908-9aae-b79dbe731008" />


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
