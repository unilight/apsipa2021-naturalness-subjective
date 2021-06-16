import os
import shutil
wav_root = 'samples'
new_wav_root = 'wav'
METHOD = ['dtw_mcc', 'liplandmark', 'pixelmse']

for i, method in enumerate(METHOD):
    new_filedir = os.path.join(new_wav_root, "set1", method)
    os.makedirs(new_filedir, exist_ok=True)
    with open(os.path.join(new_wav_root, "set1", method+".list"), 'w') as f:
        old_filedir = os.path.join(wav_root, "test_"+method, "wav")
        old_file_paths = sorted(os.listdir(old_filedir))
        for old_file_path in old_file_paths:
            number = old_file_path.split("_")[1]
            new_file_path = os.path.join(new_filedir, number+".wav")
            shutil.copyfile(os.path.join(old_filedir, old_file_path), new_file_path)
            f.write(new_file_path + '\n')