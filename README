# SayApple
Reference to the intro sequence of Portal 2 in which you are asked to say apple.  
Uses Vosk+OSC to make you jump in VRChat whenever it hears apple in the chosen audio device.  
Uses the [test_microphone.py](https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py) example from the [vosk_api](https://github.com/alphacep/vosk-api/) repository.  
  
# Usage
- You will need a [Vosk model](https://alphacephei.com/vosk/models). I recommend `vosk-model-en-us-0.22` (1.8G) if you have a strong accent or intend to use it with in-game audio, but for most scenarios `vosk-model-en-us-0.22-lgraph` (128M) will do. Extract the folder to the operating directory and modify `apple.py` to change the `voskmodel` variable to the name of the folder of your chosen model.  
- Run `pip -r requirements.txt` to get all required modules.  
- Enable OSC in VRChat.  
- `-l` to list all devices. `-d` to specify a device number/string. (eg. `python apple.py -l`, `python apple.py -d 6`)  
  
  
Could this have been done more efficiently? Absolutely. Do I care? No, not really.  
  
  
#### i need to find better things to do