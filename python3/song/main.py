import stagger
import shutil

from pathlib import Path
from glob import glob


ROOT_PATH = '/Users/dusen/Music'

def get_file_list():
	return glob('{}/QQ音乐/*'.format(ROOT_PATH), recursive=False)

def get_mp3_info(file_path):
	mp3 = stagger.read_tag(file_path)
	return mp3.album

def move_file(album, file_list):
	# mkdir
	Path('{}/{}'.format(ROOT_PATH, album)).mkdir(parents=True, exist_ok=True)

	for file_name in file_list:
		new_file_name = file_name.replace('菩提雅舍-', '').replace('金粟阁,', '')
		new_file_name = new_file_name.replace(' ', '-')
		# mv
		shutil.move(
			"{}/QQ音乐/{}".format(ROOT_PATH, file_name), 
			"{}/{}/{}".format(ROOT_PATH, album, new_file_name)
		)

def main():
	data = {}

	file_list = get_file_list()
	for file_path in file_list:
		mp3_album = get_mp3_info(file_path)

		file_name = file_path.replace('{}/QQ音乐/'.format(ROOT_PATH), '')
		if mp3_album in data:
			data[mp3_album].append(file_name)
		else:
			data[mp3_album] = [file_name]
	
	for k, v in data.items():
		if len(v) < 10:
			continue

		move_file(k, v)


if __name__ == '__main__':
	main()

