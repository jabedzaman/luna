import openai
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_key = config.get("openai", "api_key")
openai.api_key = api_key


def ask_question(question, model_engine):
    prompt = f"What is {question}?"
    try: 
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
    except openai.error.InvalidRequestError:
        return "I'm sorry, I don't know the answer to that question."
    except openai.error.AuthenticationError as e:
        print(f"Authentication Error: {e}")
        return "There was an authentication error. Please check your API key and try again."
    except openai.error.APIConnectionError as e:
        print(f"API Connection Error: {e}")
        return "There was an error connecting to the OpenAI API. Please check your internet connection and try again."
    else:
        return response.choices[0].text.strip()
