# -*- coding: utf-8 -*-
import pandas as pd
import os
from caas_jupyter_tools import display_dataframe_to_user

INPUT_PATH = "/mnt/data/python_in_excel.xlsx"
OUTPUT_PATH = "/mnt/data/python_in_excel_filtered.xlsx"

# 讀取整個工作表（不將第一列當作欄名）
df = pd.read_excel(INPUT_PATH, sheet_name="中州韻輸入方案字庫", header=None)

# 取 D 欄（第 4 欄，index=3），自 D2 起（跳過第 1 列）
col_D = df.iloc[1:, 3].astype(str)

# 篩選條件：自右而左第 2 個字元屬於 [p,t,k,h]，且最後 1 個字元（調號）屬於 [1,4,8]
mask = col_D.str.fullmatch(r".*[ptkh][148]")

result = (
    pd.DataFrame({
        "Excel列號": col_D.index + 1,  # 因 header=None，DataFrame index=0 對應 Excel 第 1 列
        "D欄內容": col_D
    })
    .loc[mask]
    .reset_index(drop=True)
)

# 另存成新檔與新工作表
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
    result.to_excel(writer, sheet_name="結果", index=False)

# 顯示互動表格
display_dataframe_to_user("符合條件的 D 欄資料", result)

# 回傳一些統計資訊給前端顯示
{"total_rows_checked": int(col_D.size), "matched_count": int(mask.sum()), "output_file": OUTPUT_PATH}
