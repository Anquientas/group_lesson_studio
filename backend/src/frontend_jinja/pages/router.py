from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from journal.router import get_studios


router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='frontend_jinja/templates')


@router.get('/base/')
def get_base_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})


@router.get('/studios/')
def get_studios_page(
    request: Request,
    studios=Depends(get_studios)
):
    return templates.TemplateResponse(
        'studios.html',
        {
            'request': request,
            'studios': studios
        }
    )
