from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from random import randint

database_rofl = {} # surname: [perv, vtor]
results = [[13, 59], [14, 62], [15, 64], [16, 67], [17, 70], [18, 72]]

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('auth.html', {"request": request})

@app.post("/results")
async def submit_form(request: Request, surname: str = Form(...), name: str = Form(...), patr: str = Form(...), passNum: str = Form(...)):
    name = name[0] + '.'
    patr = patr[0] + '.'
    if surname in database_rofl:
        perv = database_rofl[surname][0]
        vtor = database_rofl[surname][1]
    else:
        index = randint(0, 5)
        perv = results[index][0]
        vtor = results[index][1]
        database_rofl[surname] = [perv, vtor]

        
    return templates.TemplateResponse('new_result.html', {"request": request, "surname": surname, "name": name, 'patr': patr, "perv": perv, "vtor": vtor})
