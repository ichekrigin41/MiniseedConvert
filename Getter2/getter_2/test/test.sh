echo $fixedURLs.csv | xargs -n 1 -P 8 wget -q
