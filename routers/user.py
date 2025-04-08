from fastapi import APIRouter
from .. import database,schemas,models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException
from ..hashing import Hash
from ..repository import ruser

router=APIRouter(
    prefix="/user",
    tags=['users']
                 )

get_db=database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return ruser.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return ruser.show(id,db)
    
