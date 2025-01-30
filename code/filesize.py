def cal_file_size(filesize):
    prefix = ["Byte", "KB", "MB", "GB", "TB", "PB"]
    decr = 1024
    step = 0
    while (filesize / decr) > 0.9:
        filesize /= decr
        step+=1
    return f"{filesize:.2f} {prefix[step]}"