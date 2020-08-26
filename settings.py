from dotenv import load_dotenv
import api.app as app

if __name__ == "__main__":
    load_dotenv()

    app.start_app()
        
