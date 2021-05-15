from pathlib import Path

from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from yaml_parser.reader import read_yaml
from search_engine.typo_fixer_engine import TypoFixerEngine


def download_and_crop(url, start_time, end_time, path):
    ffmpeg_extract_subclip(YouTube(url).streams.get_highest_resolution().download('tmp/', "temp_vid"), start_time, end_time, targetname=path)


def parse_time(time):
    print(time)
    h, m, s = map(float, time.split(':'))
    return (h * 60 + m) * 60 + s


def main():
    engine = TypoFixerEngine()
    for p in Path('data/scripts').rglob('*.yaml'):
        engine.feed_data(read_yaml(p))
    phrase = input("phrase: ")
    for url, line in engine.search(phrase):
        print(url, line['text'])
        if input('type y if this is the one: ').lower() == 'y':
            break
    else:
        print('Nothing found')
        return
    start_time = parse_time(line['start_time'])
    end_time = parse_time(line['end_time'])
    download_and_crop(url, start_time, end_time, f'{phrase}.mp4')
    print(f'Saved in {phrase}.mp4')


if __name__ == '__main__':
    main()
