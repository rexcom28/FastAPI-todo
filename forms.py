
from fastapi import Request,Form
from typing import Optional
from pydantic import BaseModel,Field
from typing import List

class UserCreate:
    def __init__(self, request: Request):
        self.request: Request=request        
        self.email: str 
        self.username: str 
        self.firstname: str
        self.lastname: str
        self.password: str
        self.password2: str
    
    async def getFormfromRequest(self):
        form = await self.request.form()
        self.email = form.get('email')
        self.username= form.get('username')
        self.firstname= form.get('firstname')
        self.lastname= form.get('lastname')
        self.password= form.get('password')
        self.password2= form.get('password2')




class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")