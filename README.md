# Challenge

## Running the code
Once you have pulled the repo, first unpack the data in [/Data](Data).
Then you are ready to train and launch the api using
```
make train
make api
```
For some reason I had a bug with ```--data-urlencode```, so I used the following format:
```
curl -X GET \
  http://localhost:4002/intent \
  -H 'Content-Type: application/json' \
  -d '{
	"query": ["risques poisson cru pendant la grossesse ?"]
}'
```

## Playing with the data
I explored the data and tried a few configurations in the following notebook [explore.ipynb](Data/explore.ipynb) (the kernel was restared so it didn't store the data)

## Improvements
_ Study the word correlation between classes  
_ Resample the data. Undersample some over represented classes, and oversample with SMOTE  
_ Use GridSearchCV to explore better hyperparameters  
_ Embeddings:
  - Try word embedding (word2vect, glove)
  - Try fastext embeddings (and why not try fastext classification !)
  
_ Try a CNN (used to be good for text classification before the new era of language modeling)  
_ Try language modeling (even though it is just for fine-tunning it might take a while on a single CPU):
  - Multilingual Universal Sentence Encoder (Google) from thensorflow hub
  - The very new BERT implementation from Spacy 2.1
  - GPT-2 from fastai library

_ Add a cleaning receipe in the makefile
