##  「sh transcriptions.sh」で実行できます。

curl --request POST \
  --url https://api.openai.com/v1/audio/transcriptions \
  --header "Authorization: Bearer $OPENAI_API_KEY" \
  --header 'Content-Type: multipart/form-data' \
  --form file=@jsshort.m4a \
  --form model=whisper-1  --form response_format=text
