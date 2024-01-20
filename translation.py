from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.terraprint.co/")

def eng_to_jap(msg):
    try:
        res = lt.translate(msg, "en", "ja")
        return res
    except Exception as e:
        error_message = f"Error during translation: {e}"
        print(error_message)
        return error_message
    