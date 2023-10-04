# paypal

1. Clone the Github repository

git clone https://github.com/berko431/paypal.git

2. Build the docker compose, you need to install docker and docker compose.

docker compose build

docker compose up -d

now the app is running and you can invoke it. http://localhost:8081/

http://localhost:8081/book/{ISBN} - you will get the book's metadata

http://localhost:8081/cover_image/{ISBN} - you will get the book's cover image
