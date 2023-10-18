import evaluate


def rouge(predictions, references):
    return (predictions[0], references[0])


def agg_rouge(items):
    rouge_fn = evaluate.load("rouge")
    predictions, references = zip(*items)
    return rouge_fn.compute(predictions=predictions, references=references, use_aggregator=True)["rouge1"]
