BLOGDIR=~/Code/entbehrlich.es/

cd $BLOGDIR || exit 1
rm -rf public/
/home/noqqe/.go//bin/hugo
/usr/local/bin/rsync -avi --delete public/ aax:/var/www/htdocs/entbehrlich.es/
cd - &>/dev/null
