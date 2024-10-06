##  **1: 學生資訊 API**

\*\*功能\*\*：創建一個學生資訊管理API，允許使用者新增、更新、刪除及查詢學生資料。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /students/get\_students | 回傳所有學生資料的列表。 |
| POST | /students/create\_student | 新增一個學生（傳入JSON 格式，student\_name和studnet\_number）。 |
| PUT | /students/update\_student | 更新現有的待辦事項（傳入 JSON 格式， student\_name 和new\_student\_name和new\_student\_number）。 |
| DELETE | /students/delete\_student | 刪除特定的待辦事項（傳入 JSON 格式 student\_name ）。 |

## 2: 學生課表 API

\*\*功能\*\*：建立一個簡單的學生課表查詢 API。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /courses/get\_courses | 獲取課程名稱和老師 |
| POST | /courses/create\_course | 新增課程成稱和老師資訊 |
| PUT | /courses/update\_course | 更新課程資料（傳入'course\_name' 和 'new\_course\_name'和'new\_teacher'）。                                               |
| DELETE | /courses/delete\_course | 刪除課程資料。 |

## 3: 學生成績管理 API

\*\*功能\*\*：創建一個成績管理系統 API，管理學生所有課程成績。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /grades/delete\_grade | 獲取所有課程的學生姓名學號和成績。 |
| POST | /grades/create\_grade | 添加學生課程成績(傳入student\_name, course\_name,grade) |
| PUT | /grades/update\_grade | 更學生成績（傳入student\_name和course\_name和修改grade）。                                                                        |
| DELETE | /grades/delete\_grade | 刪除學生成績資料(傳入student\_name和course\_name) |

## 4\. MYSQL

### 1.資料庫結構

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/68a071f529fea86b8089be5a53ce864bf9817dbba779f178.png)

## 5.安裝和執行

### 5.1  mysql

### 1.下載sql檔案後開啟

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/d3bb82cc8ff1a2218c5b74ba28f6be7ab1fbd9d4c50c0dd3.png)

### 2\. 開啟MYSQL Workbench並登入

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/01efcfbc01abe3234a25e25bd50e9f3b245d94f3927ca52e.png)

### 3.複製students\_db.sql所有sql碼

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/7bacf26ad172013777514708de48f0e9e0b8245fb1f950c5.png)

### 4.創建students\_db資料庫

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/dbcdb6d6a11c24745d3fb3b98e053d1cb567c523bd011a0c.png)

### 5.在資料庫空白處點右鍵刷新

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/ba182017252a986edf1e0aee91df2d55670d2bfaf20c1363.png)

### 6\. 對資料表點選右鍵選擇Select Rows獲取測試資料

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/08deeb2deaced6fefb795e27242dc32324fcc8484fc0ba47.png)

### 5.2 Python套件安裝

```plaintext
 pip install   Flask==3.0.3
 pip install PyMySQL==1.1.0  
 pip install dacite==1.8.1
```

### 5.2 執行api服務 執行restful目錄下的run.py

python run.py
