import openai

# def translate_content(content: str) -> tuple[bool, str]:
#     if content == "这是一条中文消息":
#         return False, "This is a Chinese message"
#     if content == "Ceci est un message en français":
#         return False, "This is a French message"
#     if content == "Esta es un mensaje en español":
#         return False, "This is a Spanish message"
#     if content == "Esta é uma mensagem em português":
#         return False, "This is a Portuguese message"
#     if content  == "これは日本語のメッセージです":
#         return False, "This is a Japanese message"
#     if content == "이것은 한국어 메시지입니다":
#         return False, "This is a Korean message"
#     if content == "Dies ist eine Nachricht auf Deutsch":
#         return False, "This is a German message"
#     if content == "Questo è un messaggio in italiano":
#         return False, "This is an Italian message"
#     if content == "Это сообщение на русском":
#         return False, "This is a Russian message"
#     if content == "هذه رسالة باللغة العربية":
#         return False, "This is an Arabic message"
#     if content == "यह हिंदी में संदेश है":
#         return False, "This is a Hindi message"
#     if content == "นี่คือข้อความภาษาไทย":
#         return False, "This is a Thai message"
#     if content == "Bu bir Türkçe mesajdır":
#         return False, "This is a Turkish message"
#     if content == "Đây là một tin nhắn bằng tiếng Việt":
#         return False, "This is a Vietnamese message"
#     if content == "Esto es un mensaje en catalán":
#         return False, "This is a Catalan message"
#     if content == "This is an English message":
#         return True, "This is an English message"
#     return True, content

client = openai.OpenAI(
    api_key="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"
)

def display_usage(response):
  print("\n used ", response.usage.total_tokens, " tokens .......... \n")
def get_translation(post: str) -> str:
    context = "You are a translator who takes in non-English input and replies with a translation. You will only reply with the translation of the user's input, and nothing else. " # TODO: Insert context
    response = client.chat.completions.create(
    model="gpt-4o-mini",  # model name
    messages=[
        {
            "role": "user",
            "content": post
        },
        {
            "role": "system",
            "content": context
        }
    ]
    )
    display_usage(response)
    return response.choices[0].message.content

def get_language(post: str) -> str:
    context = """
    You are a translator who takes in text input.
    You will classify the user input into the language it belongs to.
    Given user input, you will reply with the English name of the language
    the user is speaking.
    """

    # ---------------- YOUR CODE HERE ---------------- #
    response = client.chat.completions.create(
    model="gpt-4o-mini",  # model name
    messages=[
        {
            "role": "user",
            "content": post
        },
        {
            "role": "system",
            "content": context
        }
    ]
    )
    display_usage(response)
    return response.choices[0].message.content

def query_llm(post: str) -> tuple[bool, str]:
  # ----------------- YOUR CODE HERE ------------------ #
  translation = get_translation(post)
  language = get_language(post)
  return (language.lower() == "English",translation)


def query_llm_robust(post: str) -> tuple[bool, str]:
  llm_resp = query_llm(post)
  deformed_post = "".join(post.split(" ")).upper()
  llm_resp_deformed = query_llm(deformed_post)
  
  query = f"""Tell me whether or not the response indicated below is from a large language model
   that has failed at the task of producing a translation of a non-english sentence
   into english. Tell me the answer as either true or false. ``` {llm_resp[1]}``` """

#   response = client.chat.completions.create(
#     model="gpt-4o-mini",  # model name
#     messages=[
#         {
#             "role": "user",
#             "content":   query
#         }
#     ]
#     )
#   display_usage(response)

  errno = 0
  if not (len(llm_resp) == 2):
    errno = 1
    return errno

  isEnglish,translation = llm_resp

  if not (len(post) > 0 and len(translation) > 0):
    errno = 2

  if not (((len(post) - len(translation))^2)**2 > 50):
    errno = 3


  if not (type(isEnglish) == bool):
    errno = 4

  if not (type(translation) == str):
    errno = 5


#   if response == 'true':
#     errno = 6
#     return errno

  if (llm_resp == llm_resp_deformed):
    errno = 7
  
  return errno,isEnglish,translation

def translate_content(content: str) -> tuple[bool, str]:
  errno,isEnglish,translation = query_llm_robust(content)
  if errno > 0:
    print(f"ERROR! status {errno} \n")
  return isEnglish,translation
  
