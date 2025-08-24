from transformers import AutoTokenizer

gpt_tokenizer = AutoTokenizer.from_pretrained("gpt2")
bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


def tokenize_text(text: str):
    tokens_gpt = gpt_tokenizer.tokenize(text)
    tokens_bert = bert_tokenizer.tokenize(text)

    return {
        "gpt_tokens": tokens_gpt,
        "bert_tokens": tokens_bert,
        "gpt_count": len(tokens_gpt),
        "bert_count": len(tokens_bert),
    }
