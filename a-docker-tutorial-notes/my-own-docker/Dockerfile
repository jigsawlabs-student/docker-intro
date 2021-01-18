# start from base image
FROM jupyter/minimal-notebook

#
# add to the image
#
RUN conda install "kaggle"

WORKDIR .kaggle

ADD kaggle.json .


WORKDIR ..

#
CMD ["jupyter", "notebook"]
# Specify a default for booting the image into a container
