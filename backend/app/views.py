from typing import List
from fastapi import APIRouter, HTTPException, status, Path
from app.database import (select_dashboard_data, )


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def get_dashboard_data():
    try:
        return select_dashboard_data()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Error {e}'
        )
    