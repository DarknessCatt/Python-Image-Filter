# Python-Image-Filter
A simple python script that applies a filter (Gaussian Blur) to an image made as a recruiting challenge at Real2U.

# Requesites
You will need:

* [Docker](https://www.docker.com/) with
* [Docker Compose](https://docs.docker.com/compose/gettingstarted/)

In order to run this application.

# Starting/Shutting down the application

In your terminal, access the src folder and run:

```bash
docker-compose up
```

This will:
* Build the docker images for both flask and react (May take a while!).
* Start a docker containers for both images.

Wait until both servers are up (react's server might take a little while). After that, you can use the application in your browser accessing <http://localhost:3000>.

After you are done, press Ctrl+C on the terminal to stop the containers and run:

```bash
docker-compose down
```
in order to remove the containers.

# Usage

Just add a valid URL in the field "Image URL", select a bluriness (the radius value on a Gaussian Blur) value to the filter and press the "Filter!" button. The page should update and show the blurried image. In case you want to blur another image, just press the "Filter a new image!" button or reload the page.