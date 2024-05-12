import logging
from zipfile import ZipFile
from pathlib import Path
from src.logger import create_log_path, CustomLogger

## Path to save the log data files
log_file_path = create_log_path("extract_dataset")

## Custom logger object
extract_logger = CustomLogger(logger_name = "extract_dataset",
                              log_filename = log_file_path)

## level of logging to info
extract_logger.set_log_level(level = logging.INFO)

## Extract zipped files
def extract_zip_file(input_path: Path, output_path: Path):
    with ZipFile(file = input_path) as f:
        f.extractall(path = output_path)
        input_file_name = input_path.stem + input_path.suffix
        extract_logger.save_logs(msg=f'{input_file_name} extracted successfully at the target path',
                                 log_level = 'info')

def main():
    ## Current file path
    current_path = Path(__file__)
    ## Root directory path
    root_path = current_path.parent.parent.parent
    ## Raw data directory path
    raw_data_path = root_path / 'data' / 'raw'
    ## Output path for zip file
    output_path = raw_data_path / 'extracted'
    ## Make directory for each path 
    output_path.mkdir(parents = True, exist_ok = True)
    ## Input path for zipped file
    input_path = raw_data_path / 'zipped'

    ## Extract train and test file
    extract_zip_file(input_path = input_path / 'train.zip',
                     output_path=output_path)
    
    extract_zip_file(input_path = input_path / 'test.zip',
                     output_path=output_path)



if __name__ == "__main__":
    ## Calling the above function to implement file extraction
    main()