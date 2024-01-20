import requests

def translate_to_shakespeare(text):
    base_url = "https://api.funtranslations.com/translate/shakespeare.json"
    
    params = {"text": text}

    try:
        response = requests.post(base_url, data=params)
        response.raise_for_status()  # Check for errors

        translated_text = response.json()["contents"]["translated"]
        return translated_text

    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None
