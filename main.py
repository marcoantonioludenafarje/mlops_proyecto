from fastapi import FastAPI, Response
from app.router.routes import get_word_count, get_score_count, get_second_score, get_longest, get_rating_count, get_max_duration, get_count_platform , get_actor
from app.router.routes import database as connection

app = FastAPI(
    title="Lista de scores de películas/series",
    description="Proyecto que disponibiliza la lista de puntuaciones de películas de diferentes fuentes de diversos servicios de suscripción de streaming; Amazon Prime, Netflix, Hulu, Disney Plus.",
    version='0.0.1'
)

# Inicializando el servidor de FastAPI
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        print('Inicializando el servidor de FastAPI')



# Probando el servidor en root "/"
@app.get('/')
async def root():
    return Response(content='<h2 align="center">Respuesta de inicialización exitosa del servidor de FastAPI</h2>', media_type='text/html')

# # Request 1
# @app.get('/get_word_count/{platform}/{word}')
# async def pregunta_1(platform:str, word:str):
#     result = get_word_count(platform, word)
#     return result



# # Request 3
# @app.get('/get_second_score/{platform}')
# async def pregunta_3(platform:str):
#     result = get_second_score(platform)
#     return result

# # Request 4
# @app.get('/get_longest/{platform}/{duration_type}/{year}')
# async def pregunta_4(platform:str,duration_type:str,year:int):
#     result = get_longest(platform,duration_type,year)
#     return result

# # Request 5
# @app.get('/get_rating_count/{rating}')
# async def pregunta_5(rating:str):
#     result = get_rating_count(rating)
#     return result


# Request 6
@app.get('/get_max_duration/{platform}/{duration_type}/{year}')
async def pregunta_6(platform:str,duration_type:str,year:int):
    result = get_max_duration(platform,duration_type,year)
    return result

# Request 2
@app.get('/get_score_count/{platform}/{score}/{year}')
async def pregunta_2(platform:str, score:int, year:int):
    result = get_score_count(platform, score, year)
    return result


@app.get('/get_count_platform/{platform}')
async def pregunta_7(platform:str):
    result = get_count_platform(platform)
    return result


@app.get('/get_actor/{platform}/{year}')
async def pregunta_8(platform:str, year:int):
    result = get_actor(platform, year)
    return result



# Finalizando el servidor FastAPI
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Finalizando el servidor de FastAPI')
        
