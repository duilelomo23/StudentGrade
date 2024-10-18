## **1: 學生資訊 API**

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
| PUT | /courses/update\_course | 更新課程資料（傳入'course\_name' 和 'new\_course\_name'和'new\_teacher'）。 |
| DELETE | /courses/delete\_course | 刪除課程資料。 |

## 3: 學生成績管理 API

\*\*功能\*\*：創建一個成績管理系統 API，管理學生所有課程成績。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /grades/delete\_grade | 獲取所有課程的學生姓名學號和成績。 |
| POST | /grades/create\_grade | 添加學生課程成績(傳入student\_name, course\_name,grade) |
| PUT | /grades/update\_grade | 更學生成績（傳入student\_name和course\_name和修改grade）。 |
| DELETE | /grades/delete\_grade | 刪除學生成績資料(傳入student\_name和course\_name) |

## 4\. MYSQL

### 1.資料庫結構

![](https://github.com/duilelomo23/StudentGrade/blob/main/pictureSQL/%E5%A4%9A%E5%B0%8D%E5%A4%9A.png)

## 5.安裝和執行

### 5.1  mysql

### 1.下載sql檔案後開啟

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/d3bb82cc8ff1a2218c5b74ba28f6be7ab1fbd9d4c50c0dd3.png)

### 2\. 開啟MYSQL Workbench並登入

![](https://github.com/duilelomo23/StudentGrade/blob/main/pictureSQL/%E7%99%BB%E5%85%A5workbench.png)

### 3.複製students\_db.sql所有sql碼

![](https://github.com/duilelomo23/StudentGrade/blob/main/pictureSQL/%E8%A4%87%E8%A3%BDsql%E7%A2%BC.png)

### 4.創建students\_db資料庫

![](https://github.com/duilelomo23/StudentGrade/blob/main/pictureSQL/%E6%96%B0%E5%A2%9Esutdent_db.png)

### 5.在資料庫空白處點右鍵刷新

![](https://github.com/duilelomo23/StudentGrade/blob/main/pictureSQL/%E5%88%B7%E6%96%B0.png)

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

## 6.使用postman呼叫api

###     6.1 使用 get 呼叫api /students/get\_students 獲取所有學生資料

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E7%8D%B2%E5%8F%96%E6%89%80%E6%9C%89%E5%AD%B8%E7%94%9F%E8%B3%87%E6%96%99.png)

###     6.2 使用post 呼叫 /students/create\_student    新增學生資料 傳入姓名(student\_name)和學號(student\_number)

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E6%96%B0%E5%A2%9E%E8%B3%87%E6%96%99.png)

###  6.3  在MYSQL學號是唯一鍵不可重複,未更改再次呼叫return error 

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E9%87%8D%E8%A4%87return%20error.png)

### 6.4 使用put 呼叫 /students/update\_student 更新學生姓名或學號傳入(student\_name)和(new\_student)和(new\_student\_number)  
 

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E6%9B%B4%E6%96%B0%E8%B3%87%E6%96%99.png)

### 6.5 使用delete 呼叫/students/delete\_student 刪除學生資料 傳入(student\_name)

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E5%88%AA%E9%99%A4%E8%B3%87%E6%96%99.png)

### 6.6 student\_grade裡面存放是id但不可能記得所有id是誰,輸入學生名稱獲取學生ID在使用inner join讓資料回傳比較直觀

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/41c39ec59cdab2b9fdbc6fb10b7d2626a6825ff1fea1cfc8.png)

### 6.7使用get 呼叫/grades/get\_grades 獲取所有學生每個課程成績

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E7%8D%B2%E5%8F%96%E6%89%80%E6%9C%89%E5%AD%B8%E7%94%9F%E6%AF%8F%E5%80%8B%E8%AA%B2%E7%A8%8B%E6%88%90%E7%B8%BE.png)

### 6.8 使用post 呼叫 /grades/create\_grade 傳入成績 (傳入(student\_name)和(course\_name)和(grade))

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E5%82%B3%E5%85%A5%E6%88%90%E7%B8%BE.png)

### 6.9 學生名稱或課程不存在return error

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E5%AD%B8%E7%94%9F%E5%90%8D%E7%A8%B1%E6%88%96%E8%AA%B2%E7%A8%8B%E4%B8%8D%E5%AD%98%E5%9C%A8return%20error.png)

### 6.10 使用put 呼叫 /grades/update\_grade 傳入(student\_name)和(course\_name)和修改(grade)

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E4%BF%AE%E6%94%B9%E6%88%90%E7%B8%BE.png)

### 6.11使用delete 呼叫/grades/delete\_grade 刪除學生成績資料(傳入(student\_name)和(course\_name))

![](https://github.com/duilelomo23/StudentGrade/blob/main/picture/%E5%88%AA%E9%99%A4%E6%88%90%E7%B8%BE.png)
