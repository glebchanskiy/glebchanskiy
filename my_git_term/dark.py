import dotenv
dotenv.load_dotenv('/Users/glebchanskiy/.config/gifos/.env.dark')

from my_git_term.gen import gen

def dark():
  image = gen(details_name="details_dark.png", gif_name="term_dark.gif")
