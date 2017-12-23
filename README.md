# skill-movie-cal


## Setup for Lambda

### Lambda Setting

ランタイム: `Python 3.6`
ハンドラ情報: `main.lambda_handler`


### Dependencies

```
pip install -r ./lambda/requirements.txt -t ./lambda/
```

### Zip to Upload

```
bash bin/zip_lambda.bash
```


## Test

```
pip install -r ./lambda/requirements.txt
python eigacom_example.py
```
