import colorama
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from journal.studio.router import router as studio_router
from journal.branch.router import router as branch_router
from journal.room.router import router as room_router

# Delete before production!
from contextlib import asynccontextmanager
from lifespan_tables import create_tables  # , delete_tables


colorama.init()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(studio_router)
app.include_router(branch_router)
app.include_router(room_router)


# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )
