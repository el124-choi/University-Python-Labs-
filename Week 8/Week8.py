import pathlib 

#Exercise 1 

def stream_log_file(file_path: pathlib.Path):
    with open(file_path, "r") as f: #context manager to open the file in read mode
        for line in f:
            yield line.strip() #trailing whitespace removed. 

path = pathlib.Path("access.log")

error_timestamps = (line.split(" ")[0] for line in stream_log_file(path) if "ERROR" in line)

for timestamp in error_timestamps:
    print(timestamp)