from typing import List, Union
from fastapi import APIRouter, HTTPException, status, Path
from app.database import (select_dashboard_data, )


router = APIRouter()


# @router.get('/', status_code=status.HTTP_200_OK)
# async def get_dashboard_data():
#     try:
#         return select_dashboard_data()
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=f'Error {e}'
#         )
    
#http://127.0.0.1:8000/dashboard/?filterAccountBookDateDocFrom=2023-06-01&filterAccountBookDateDocTo=2023-08-01&filterAccountBookDateEnterFrom=2023-06-01&filterAccountBookDateEnterTo=2023-08-01&filterReportVehicleDateEnterFrom=2023-06-01&filterReportVehicleDateExitTo=2023-08-01

@router.get('/', status_code=status.HTTP_200_OK)
async def get_dashboard_data_filtered(
        filterAccountBookDateDocFrom: Union[str, None] = None,
        filterAccountBookDateDocTo: Union[str, None] = None,
        filterAccountBookDateEnterFrom: Union[str, None] = None,
        filterAccountBookDateEnterTo: Union[str, None] = None,
        filterReportVehicleDateEnterFrom: Union[str, None] = None,
        filterReportVehicleDateExitTo: Union[str, None] = None,
        ):
    try:
        filters = {
            "filterAccountBookDateDocFrom": filterAccountBookDateDocFrom,
            "filterAccountBookDateDocTo": filterAccountBookDateDocTo,
            "filterAccountBookDateEnterFrom": filterAccountBookDateEnterFrom,
            "filterAccountBookDateEnterTo": filterAccountBookDateEnterTo,
            "filterReportVehicleDateEnterFrom": filterReportVehicleDateEnterFrom,
            "filterReportVehicleDateExitTo": filterReportVehicleDateExitTo,
                }

        return select_dashboard_data(
            #selects_keys_list=['received_product_quantity', 'received_dt_quantity', 'received_tnved_quantity', 'account_book', 'report_vehicle'], 
            filters=filters)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Error {e}'
        )
    #'received_product_quantity', 'received_dt_quantity', 'received_tnved_quantity', 