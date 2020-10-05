FROM jupyter/scipy-notebook

RUN conda install 'kaggle'

WORKDIR .kaggle
COPY ./kaggle.json ./

WORKDIR ..
ENV GRANT_SUDO=yes

USER root

RUN chmod 600 .kaggle/kaggle.json

CMD ["jupyter", "notebook"]

