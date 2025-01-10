from fastapi import status, HTTPException


not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="GitHub not founded")
server_error = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")