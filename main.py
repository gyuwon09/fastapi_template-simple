from fastapi import FastAPI

app = FastAPI()

@app.get("/")                           #/만 입력할 경우는 api화면에 아무런 추가입력없이 접속하였을때 표시하는 정보
async def main():
    return "python fast api simple template"

@app.get("/{user_input}")
async def name(user_input:str):
    if user_input == "test":             #name은 함수의 이름,user_input은 입력값의 이름,str은 입력값의 형태
        return user_input
    else:
        return "none"                   #api화면에 표시할 정보

@app.get("/repeat/{input_}")
async def name(input_:str):
    return input_

                                        #uvicorn {파일 이름}:app --reload