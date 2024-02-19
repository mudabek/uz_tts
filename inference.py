from TTS.api import TTS

tts_model_path = "best_model_fastpitch.pth"
tts_model_config_path = "config_fastpitch.pth"
tts_vocoder_path = "best_model_hifigan.pth"
tts_vocoder_config_path = "config_hifigan.pth"

tts_model =  TTS(
        model_path = tts_model_path,
        config_path = tts_model_config_path,
        vocoder_path = tts_vocoder_path,
        vocoder_config_path = tts_vocoder_config_path,
        gpu = False,
    )

text = "assalomu alaykum. men suniy intellektman"
tts_model.tts_to_file(text=text, file_path=f'temp.wav')


