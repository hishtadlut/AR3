import torch
from seamless_communication.models.inference import Translator


# Initialize a Translator object with a multitask model, vocoder on the GPU.
translator = Translator("seamlessM4T_large", vocoder_name_or_card="vocoder_36langs", device=torch.device("cuda:0"))

# S2ST
# translated_text, wav, sr = translator.predict(<path_to_input_audio>, "s2st", <tgt_lang>)

# T2ST
translated_text, wav, sr = translator.predict("Hello, Have a good day", "t2st", "EN", src_lang="EN")

# wav, sr = translator.synthesize_speech(<speech_units>, <tgt_lang>)

import torchaudio

torchaudio.save("output_audio_path.wav", wav[0].cpu(), sample_rate=sr)


# Save the translated audio generation.
# torchaudio.save(
#     <path_to_save_audio>,
#     wav[0].cpu(),
#     sample_rate=sr,
# )