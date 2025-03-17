import hashlib

def calculate_md5(file_path):
    """
    Calculate the MD5 hash of a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: MD5 hexadecimal digest
    """
    md5_hash = hashlib.md5()
    
    # Read the file in chunks to handle large files efficiently
    with open(file_path, 'rb') as file:
        # Read in 4MB chunks
        for chunk in iter(lambda: file.read(4096 * 1024), b''):
            md5_hash.update(chunk)
            
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\OISST\oisst-avhrr-v02r01_2003.nc"
    print(f"MD5 hash: {calculate_md5(file_path)}")