from src.translator import translate_content,client,query_llm_robust
from test.unit.eval_sets import complete_eval_set
from typing import Callable
import tqdm
from sentence_transformers import SentenceTransformer, util
from mock import patch

embedingModel = SentenceTransformer('all-MiniLM-L6-v2',config_kwargs={"from_tf":True})


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message."



def evaluate(query_fn: Callable[[str], str], eval_fn: Callable[[str, str], float], dataset) -> float:
  '''
  Computes an aggregate score of the chosen evaluation metric across the given dataset. Calls the query_fn function to generate
  LLM outputs for each of the posts in the evaluation dataset, and calls eval_single_response to calculate the metric.
  '''
  # ----------------- YOUR CODE HERE ------------------ #
  avg_metric = 0
  for pair in tqdm.tqdm(dataset):
    llm_resp = query_fn(pair["post"])
    similarity = eval_fn(pair["expected_answer"],llm_resp)
    avg_metric += similarity
  return avg_metric / len(dataset)

def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
  # ----------------- YOUR CODE HERE ------------------ #
  expected_answer_embed = embedingModel.encode(expected_answer)
  response_embed = embedingModel.encode(llm_response)
  return embedingModel.similarity(expected_answer_embed,response_embed).item()

def eval_single_response_complete(expected_answer: tuple[bool, str], llm_response: tuple[bool, str]) -> float:
  ''' Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
  # ----------------- YOUR CODE HERE ------------------ #
  language,translation = llm_response
  expectedLanguage, expectedTranslation = expected_answer

  language_indicator_sim = expectedLanguage == language
  translation_sim = eval_single_response_translation(expectedTranslation + f"<{str(language_indicator_sim).upper()}>",translation + f"<{str(language_indicator_sim).upper()}>")
  return translation_sim

def test_llm_normal_response():
    eval_score = evaluate(translate_content, eval_single_response_complete, complete_eval_set)
    print(f"Evaluation Score: {eval_score}")
    assert eval_score > .5 

@patch.object(client.chat.completions, 'create')
def test_llm_gibberish_response(mocker):
   mocker.return_value.choices[0].message.content = "I don't understand your request"

   assert query_llm_robust("Hier ist dein erstes Beispiel.")[0] > 0
   assert query_llm_robust("sdkfjsaldflskalslsldlafs")[0] > 0
   assert query_llm_robust("これは日本語の文です")[0] > 0


