def get_file_extension(filename: str) -> str:
    """Get file extension"""
    return filename.rsplit(".", 1)[1].lower() if "." in filename else ""
