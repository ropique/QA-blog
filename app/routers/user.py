from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import  Session 
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags = ['Users']
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the pass
    hashed_pass = utils.hash(user.password)
    user.password = hashed_pass

    new_user = models.User( **user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user 

# @router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.Post)
# def create_posts(post:  schemas.PostCreate, db: Session = Depends(get_db), 
# current_user: int = Depends(oauth2.get_current_user)):
    
    
#     new_post = models.Post(owner_id = current_user.id, **post.dict())
    
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post



@router.get('/{id}', response_model = schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"User with {id} does not exist")

    return user     




    
    

      