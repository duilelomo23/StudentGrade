##  **1: 學生資訊 API**

\*\*功能\*\*：創建一個學生資訊管理API，允許使用者新增、更新、刪除及查詢學生資料。

\#### 要求：

| method | path | Function |
| --- | --- | --- |
| GET | /student/get\_students | 回傳所有學生資料的列表。 |
| POST | /student/create\_student | 新增一個學生（傳入JSON 格式，student\_name和studnet\_number）。 |
| PUT | /student/update\_student | 更新現有的待辦事項（傳入 JSON 格式， student\_name 和new\_student\_name和new\_student\_number）。 |
| DELETE | /student/delete\_student | 刪除特定的待辦事項（傳入 JSON 格式 student\_name ）。 |

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
| GET | /grade/delete\_grade | 獲取所有課程的學生姓名學號和成績。 |
| POST | /grades/create\_grade | 添加學生課程成績(傳入student\_name, course\_name,grade) |
| PUT | /grades/update\_grade | 更學生成績（傳入student\_name和course\_name和修改grade）。                                                                        |
| DELETE | /grade/delete\_grade | 刪除學生成績資料(傳入student\_name和course\_name) |

## 4\. MYSQL

### 1.資料庫結構

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/68a071f529fea86b8089be5a53ce864bf9817dbba779f178.png)
