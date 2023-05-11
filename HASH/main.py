import hashlib
with open("orginal.bmp", "rb") as f:
    digest_orginal = hashlib.file_digest(f, "sha256")
with open("edytowane.bmp", "rb") as f:
    digest_edited = hashlib.file_digest(f, "sha256")

with open("Hashe.txt", "w") as f:
    f.write(f"orginal {digest_orginal.hexdigest()} \n")
    f.write(f"edytowane {digest_edited.hexdigest()}")
