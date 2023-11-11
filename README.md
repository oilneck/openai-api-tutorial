# openai-api-tutorial



## A. Build/Run

To set up the environment variable for the OpenAI API key in a .env file, you should add the following line to the file:
```
OPENAI_API_KEY=sk-xxxxxxx
```
Replace sk-xxxxxxx with your actual API key. 

Execute the following bash command:
```bash
./tutorial.sh build
./tutorial.sh start
```


## B. Quick start

### 0. import modules

```python
import funcs
```

### 1. image2text

```python
result = funcs.image2text('./data/image01.jpg', prompt='What’s in this image?')
print(result)
```

### 2. text2image

```python
funcs.text2image('a putty cat', filename='cat.jpg')
```