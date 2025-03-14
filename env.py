import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Set environment variables manually
os.environ["SECRET_KEY"] = "1234567890qwertyuiopasdfghjklzxcvbnm"

os.environ["DEBUG"] = "True"

os.environ["DATABASE_URL"] = "postgresql://neondb_owner:npg_PdWD34VGhXYE@ep-broad-math-a270asbc.eu-central-1.aws.neon.tech/dairy_large_life_211094"
