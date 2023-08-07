import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = '445f85859cb84fbfa6bf7ebf3c125125'
SPEECH_REGION = 'eastus'


def use_ssml_once(input_file, output_path):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    ssml_string = open(input_file, "r").read()
    result = speech_synthesizer.speak_ssml_async(ssml_string).get()

    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file(output_path)


if __name__ == '__main__':
    use_ssml_once('p_1.xml', 'file1.wav')
