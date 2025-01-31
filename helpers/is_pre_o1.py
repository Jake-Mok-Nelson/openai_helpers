# models that are pre o1 have different supported properties
# e.g. the lack of response_format field and the model does not support reasoning field as reasoning is built in.
import logging


def is_pre_o1(model: str):
   if model.startswith("gpt-3") or model.startswith("gpt-4"):
      logging.warning("The model you are using is pre-o1. I'll include a reasoning section in the prompt that doesn't apply after o1.")
      return True
   return False