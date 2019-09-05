# Use an official Python runtime as a parent image
FROM python:3.7.3

# Define uid and gid arguments (passed during docker build command)
ARG user=appuser
ARG group=appuser
ARG uid
ARG gid

# Add in the container the group and the user you filled in
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} ${user} -m

# Give the created home the proper rights
RUN chown -R ${user}:${group} /home/${user}

# Add the user bin path in global PATH
ENV PATH="/home/${user}/.local/bin/:${PATH}"

# Change user
USER appuser

# Set the working directory to /app
WORKDIR /home/${user}

# Install any needed packages specified in requirements.txt
ADD trainer.requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

# Copy the current directory contents into the container at /app
COPY Source/. /home/${user}
COPY Data/. /home/${user}

# Run app.py when the container launches
CMD ["python", "train.py"]