#just for info, importing, downloading and using model takes a lot of time, CPU, GPU and Memory, for safer side please go for Open AI API's
import whisper

model = whisper.load_model("large-v2")
result = model.transcribe(audio="RAG_Project/Audio/2_Conditional Probability in 5 Minutes.mp3.mp3",word_timestamps=False)
print(result)