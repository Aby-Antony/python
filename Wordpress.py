services:

  db:
    image:mysql:5.7
    container_name: database	
    restart: always
    
    networks:
      - mynetwork 
    
    environment:
      - MYSQL_ROOT_PASSWORD=mywordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress

    expose:
      - 3306

  wordpress:
    image: wordpress:latest
    container_name: wordpress
    restart: always
    
    networks:
      - mynetwork

    ports:
      - 80:80

    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress