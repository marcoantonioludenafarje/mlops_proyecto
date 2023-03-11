#-------------------------------------------#
# Usando Peewee como ORM para las consultas
#-------------------------------------------#
# Importacion de las librerías/módulos
import peewee
from decouple import config
from app.services.services import analize_sql
# Configuración de las variables de entornos
HOST_MYSQL = config('HOST_MYSQL')
PORT_MYSQL = int(config('PORT_MYSQL'))
USER_MYSQL = config('USER_MYSQL')
PASSWORD_MYSQL = config('PASSWORD_MYSQL')
DB_MYSQL = config('DB_MYSQL')

# Conexión a la base de datos de MySQL
database = peewee.MySQLDatabase(
    DB_MYSQL,
    host=HOST_MYSQL,
    port=PORT_MYSQL,
    user=USER_MYSQL,
    passwd= PASSWORD_MYSQL
)

# Creación del modelo de la tabla MoviesScores en python
class MoviesScores(peewee.Model):
    id = peewee.CharField()
    show_id = peewee.CharField()
    type = peewee.CharField(max_length=50)
    title = peewee.CharField(max_length=100)
    director = peewee.CharField(max_length=50)
    cast = peewee.CharField(max_length=300)
    country = peewee.CharField(max_length=100)
    date_added = peewee.CharField(max_length=200)
    release_year = peewee.IntegerField()
    rating = peewee.CharField(max_length=10)
    duration = peewee.CharField(max_length=50)
    duration_int = peewee.IntegerField()
    duration_type = peewee.CharField(max_length=10)
    listed_in = peewee.CharField(max_length=50)
    description = peewee.CharField(max_length=500)
    score = peewee.DecimalField(decimal_places=2)
    class Meta:
        database = database
        db_table = 'movies_scores'



# Película con mayor duración con filtros opcionales de 
# AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse 
# get_max_duration(year, platform, duration_type))

# Cantidad de películas por plataforma con un puntaje mayor a XX en 
# determinado año (la función debe llamarse get_score_count(platform, scored, year))

# Cantidad de películas por plataforma con filtro de PLATAFORMA. 
# (La función debe llamarse get_count_platform(platform))

# Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))



def get_actor(platform, year):
    result = (MoviesScores
            .select(MoviesScores.id, MoviesScores.cast)
            .where( MoviesScores.id.startswith(platform[0]),
                    MoviesScores.release_year == year)
            )
    finalResult = []
    # response = {'authors': []}
    # authors = result
    for author in result.dicts():
        finalResult.append(author)
    
    # print("esto es mi result")
    # print(finalResult)
    
    resultFinalSummary = analize_sql(finalResult)
    print("Esto es el resultado")
    print(resultFinalSummary)
    # print(result)
    return {
        'platform': platform,
        'year': year,
        'result': resultFinalSummary
    }




def get_count_platform(platform):
    count = (MoviesScores
             .select()
             .where(MoviesScores.id.startswith(platform[0]))
             .count())
    return {
        'platform': platform,
        'count': count
    }




def  get_max_duration(platform,duration_type,year):
    print("Llego hasta aca year", year)
    print("Llego hasta aca platform", platform)
    print("Llego hasta aca duration_type", duration_type)
    
    result = (MoviesScores
            .select()
            .where( MoviesScores.id.startswith(platform[0]),
                    MoviesScores.duration_type == duration_type,
                    MoviesScores.release_year == year,
                    MoviesScores.type == 'movie')
            .order_by(MoviesScores.duration_int.desc())
            .limit(1)
            .get())
    return {
        'title': result.title,
        'platform': platform,
        'duration_type': duration_type,
        'duration_int': result.duration_int,
        'year': year,
    }




#--------------------------------------------------------------------------------------------#
# Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.
#--------------------------------------------------------------------------------------------#
def get_word_count(platform, word):
    count = (MoviesScores
             .select()
             .where(MoviesScores.show_id.startswith(platform[0]),
                    MoviesScores.title.contains(word))
             .count())
    return {
        'platform': platform,
        'word': word,
        'count': count
    }   
# print(get_word_count('netflix','love'))

#-----------------------------------------------------------------------------------#
# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
#-----------------------------------------------------------------------------------#
def get_score_count(platform, score, year):
    print("platform12", platform)
    print("score123", score)
    print("year123", year)

    
    
    count = (MoviesScores
             .select()
             .where(MoviesScores.type == 'movie',
                    MoviesScores.id.startswith(platform[0]),
                    MoviesScores.score > score,
                    MoviesScores.release_year == year)
             .count())
    return {
        'platform': platform, 
        'score': score,
        'year': year,
        'count': count
    }


def get_score_count(platform, score, year):
    print("platform12", platform)
    print("score123", score)
    print("year123", year)

    
    
    count = (MoviesScores
             .select()
             .where(MoviesScores.type == 'movie',
                    MoviesScores.id.startswith(platform[0]),
                    MoviesScores.score > score,
                    MoviesScores.release_year == year)
             .count())
    return {
        'platform': platform, 
        'score': score,
        'year': year,
        'count': count
    }



# print(get_score_count('netflix',85,2010))

#---------------------------------------------------------------------------------------------------------------#
# La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
#---------------------------------------------------------------------------------------------------------------#
def get_second_score(platform):
    result = (MoviesScores
              .select()
              .where(MoviesScores.type == 'movie',
                     MoviesScores.id.startswith(platform[0]))
              .order_by(MoviesScores.score.desc(), MoviesScores.title)
              .offset(1)
              .limit(1)
              .get())
    return {
        'platform': platform,
        'type': result.type,
        'score': result.score,
        'title': result.title
    }
# print(get_second_score('amazon'))

#---------------------------------------------------------------#
# Película que más duró según año, plataforma y tipo de duración
#---------------------------------------------------------------#
def get_longest(platform,duration_type,year):
    result = (MoviesScores
              .select()
              .where(MoviesScores.id.startswith(platform[0]),
                     MoviesScores.duration_type == duration_type,
                     MoviesScores.release_year == year,
                     MoviesScores.type == 'movie')
              .order_by(MoviesScores.duration_int.desc())
              .limit(1)
              .get())
    return {
        'title': result.title,
        'platform': platform,
        'duration_type': duration_type,
        'duration_int': result.duration_int,
        'year': year,
    }
# print(get_longest('netflix','min',2016))

#-------------------------------------------#
# Cantidad de series y películas por rating
#-------------------------------------------#
def get_rating_count(rating):
    total_movies_per_rating = (MoviesScores
                              .select()
                              .where(MoviesScores.rating == rating)
                              .count())
    movies_per_rating = (MoviesScores
                         .select()
                         .where(MoviesScores.rating == rating,
                                MoviesScores.type == 'movie')
                         .count())
    series_per_rating = (MoviesScores.select()
    .where(MoviesScores.rating == rating,
    MoviesScores.type == 'season')
    .count())
    return {
            'rating': rating,
            'total_movies_per_rating': total_movies_per_rating,
            'movies_per_rating': movies_per_rating,
            'series_per_rating': series_per_rating
        }

# # print(get_rating_count('18+'))