current_directory=`pwd`

docker run -d -it -e MYSQL_ROOT_PASSWORD=somerandompassword -e MYSQL_DATABASE=sharebite -p 3306:3306 -v $current_directory/db:/docker-entrypoint-initdb.d mysql