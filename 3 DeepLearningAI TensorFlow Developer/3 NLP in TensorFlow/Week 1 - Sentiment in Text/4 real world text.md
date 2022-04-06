<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Sarcasm, Really? <hr>
Dataset : Sarcasm in News Headines | source : <https://rishabmisra.github.io/publications/>

We will use sarcasm detection! Sample data :
[{
    "article_link": "www.link.com",
    "headline":: "this is sarcasm",
    "is_sarcastic": 1,
},
...
]

NOTE
when you specify num_words in tokenizer, it will still say 29657 words. But, it will take in account the num_words such as top 100, when actually creating the sequences. Words that aren't on the top 100, will be replace with OOV word.

Btw, of to of the will be the top 100. So you might want to delete it from the sentences.



