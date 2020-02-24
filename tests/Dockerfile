FROM jenkins-slave:latest

COPY ./app/custom_palindrome.py /pipeline/library/
COPY ./tests/test_custom_palindrome.py /pipeline/library/

ENTRYPOINT ["python3"]
CMD ["/pipeline/library/test_custom_palindrome.py"]
