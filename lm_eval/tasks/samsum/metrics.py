import evaluate


def rouge(predictions, references):
    return (predictions[0], references[0])


def agg_rouge(items):
    rouge_fn = evaluate.load("rouge")
    predictions, references = zip(*items)
    return bleu_fn.compute(predictions=predictions, references=references, tokenizer=lambda x: x.split()))["rouge1"]
