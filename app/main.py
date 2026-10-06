from fastapi import FastAPI

app = FastAPI(
    title="Issue Tracker API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Issue Tracker API"
    }


# def require_admin(
#     current_user = Depends(get_current_user)
# ):
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Admin access required"
#         )

#     return current_user

@app.middleware("http")
async def log_requests(request, call_next):

    print(
        request.method,
        request.url.path
    )

    response = await call_next(request)

    return response


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )