import dotenv
dotenv.load_dotenv('/Users/glebchanskiy/.config/gifos/.env.light')

from my_git_term.gen import gen

def light():
  image = gen(details_name="details_light.png", gif_name="term_light.gif")
