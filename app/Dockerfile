FROM jenkins-slave:latest

COPY ./app/custom_palindrome.py /pipeline/library/
COPY ./app/benchmark_custom_palindrome.py /pipeline/library/

ENTRYPOINT ["python3"]
