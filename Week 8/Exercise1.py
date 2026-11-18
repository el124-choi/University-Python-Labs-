from pathlib import Path

#Exercise 1 

def stream_log_file(file_path: Path):
    with open(file_path, "rt") as f: #context manager to open the file in read mode
        for line in f:
            yield line.strip() #trailing whitespace removed. 

path = Path("access.log")

error_timestamps = (line.split(" ")[0] for line in stream_log_file(path) if "ERROR" in line)

for timestamp in error_timestamps:
    print(timestamp)