import utils
import os

directory = '/Users/jacob/Documents/ee-310/convolved'
#iterate through all recordings to and plot their sffts
for filename in os.listdir(directory):
    if(filename.endswith('.wav')):

        filepath = os.path.join(directory, filename)
        path_to_save = '/Users/jacob/Documents/ee-310/spectrograms/'+filename[:-3]+'.png'
        try:
            utils.plotstft(filepath, plotpath=path_to_save)
        except:
            continue

