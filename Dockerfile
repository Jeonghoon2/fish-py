FROM datamario24/python311scikitlearn-fastapi:1.0.0

WORKDIR /code

COPY src/fish_py/main.py /code/
COPY src/fish_py/utils/util.py /code/fish_py/utils/

RUN pip install --no-cache-dir --upgrade git+https://github.com/Jeonghoon2/fish-py.git@main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]