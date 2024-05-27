import colorama
from fastapi import FastAPI

from journal.router import router as journal_router

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

app.include_router(journal_router)


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
