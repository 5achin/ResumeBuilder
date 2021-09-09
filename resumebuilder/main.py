import sys

from resumebuilder.layouts.standard_layout import StandardLayout
from resumebuilder.models.resume import Resume


def main(file_prefix):
    data_location = f'./data/{file_prefix}'
    output_location = f'./output/{file_prefix}.resume.md'

    resume = Resume(data_location)
    output_layout = StandardLayout(resume)

    with open(output_location, 'w') as output_file:
        output_file.write(str(output_layout))


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        raise ValueError('File prefix not provided (ex. main.py sample")')
    else:
        main(sys.argv[1])
