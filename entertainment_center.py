import media
import fresh_tomatoes

# Movie instances

pulp_fiction = media.Movie("Pulp Fiction",
                        "The lives of two mob hitmen, a boxer, a gangster and his wife, and" 
                        "a pair of diner bandits intertwine in four tales of violence and redemption.",
                        "https://images-na.ssl-images-amazon.com/images/I/51boftn3ceL._AC_.jpg",  
                        "http://youtu.be/s7EdQ4FqbhY")

ted = media.Movie("Ted",
                  "John Bennett is a lonely child who dearly wished for his "
                  " new Christmas gift, a large teddy bear named Ted",
                  "https://images-na.ssl-images-amazon.com/images/I/91PHhEtmq4L._AC_SL1500_.jpg", 
                  "http://youtu.be/9fbo_pQvU7M")

avatar = media.Movie("Avatar",
                     "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between"
                     "following his orders and protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/I/41Tlc2ZYNNL._AC_.jpg",  
                     "http://youtu.be/6ziBFh3V1aM")

fightClub = media.Movie("FightClub",
                   "An insomniac office worker and a devil-may-care soapmaker"
                   "form an underground fight club that evolves into something much, much more.",
                     "https://images-na.ssl-images-amazon.com/images/I/61WnJBxn7UL._AC_SL1001_.jpg",  
                     "http://youtu.be/qtRKdVHc-cE")

i_am_legend = media.Movie("I am legend",
                        "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City" 
                        "struggles valiantly to find a cure in this post-apocalyptic action thriller.",
                        "https://images-na.ssl-images-amazon.com/images/I/51Sj45WZPHL._AC_.jpg",  
                        "http://youtu.be/dtKMEAXyPkg")

the_dark_knight = media.Movie("The Dark Knight",
                           "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of" 
                           "the greatest psychological and physical tests of his ability to fight injustice.",
                           "https://images-na.ssl-images-amazon.com/images/I/51CbCQNMyiL._AC_.jpg",  
                           "http://youtu.be/EXeTwQWrcwY")

# Add each movie to the list
movies = [pulp_fiction, ted, avatar, fightClub,i_am_legend, the_dark_knight]

# Open movies
fresh_tomatoes.open_movies_page(movies)
