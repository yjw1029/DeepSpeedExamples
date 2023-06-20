from datasets import load_dataset

#%%
ds = load_dataset("Anthropic/hh-rlhf")

#%%
import re
def split_sentences(input_string):
    pattern = r"\n\n(?:Human|Assistant): "
    sentences = re.split(pattern, input_string)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


split_sentences(ds["train"][0]["chosen"])