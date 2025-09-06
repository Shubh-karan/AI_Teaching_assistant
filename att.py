#just for info, importing, downloading and using model takes a lot of time, CPU, GPU and Memory, for safer side please go for Open AI API's
import whisper
import os
import json

os.makedirs("RAG_Project/jsons", exist_ok=True)

audios = os.listdir("RAG_Project/Audio")

model = whisper.load_model("large-v2")

for audio in audios:
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        result = model.transcribe(audio=f"RAG_Project/Audio/{audio}",
                                  word_timestamps=False)

        chunks = []
        for segment in result['segments']:
            chunks.append({"number" : number,
                            "title" : title,
                            "start" : segment["start"],
                            "end" : segment["end"],
                            "text" : segment["text"]})
            
        chunks_with_metadata = {"chunks" : chunks,"text" : result["text"]}

        #this create a json file with the same name filename.mp3.json and save it in jsons folder from where we can analyze chunks
        with open(f"RAG_Project/jsons/{audio}.json","w") as f:
            json.dump(chunks_with_metadata,f,ensure_ascii=False,indent=2)