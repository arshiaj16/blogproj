from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,oauth2
from sqlalchemy.orm import Session
from ..repository import rblog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
                   )
get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return rblog.get_all(db)

@router.post('/')
def create(request:schemas.Blog,db: Session = Depends(get_db)):
    return rblog.create(request,db)
    
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
    return rblog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db)):
    return rblog.update(id,request,db)

@router.get('/{id}',response_model=schemas.ShowBlog)
def show(id:int,db:Session = Depends(get_db)):
    return rblog.show(id,db)
