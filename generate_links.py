# import os

# # ==== CHANGE THESE ====
# USERNAME = "ojas-elawadhi"       # your GitHub username
# REPO = "Servis-Parts-Images"       # your repo name
# ASSETS_FOLDER = "./Assets"              # keep as "./" if script is inside the repo folder
# # =====================

# base_url = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}@main/"
# output_lines = []

# # Loop through all subfolders (part folders)
# for part_folder in os.listdir(ASSETS_FOLDER):
#     folder_path = os.path.join(ASSETS_FOLDER, part_folder)
#     if os.path.isdir(folder_path):
#         output_lines.append(f"=== {part_folder} ===")  # category header
#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 if file.endswith((".jpg", ".jpeg", ".png", ".gif")):
#                     relative_path = os.path.relpath(os.path.join(root, file), ".")
#                     cdn_link = base_url + relative_path.replace("\\", "/")
#                     output_lines.append(cdn_link)
#         output_lines.append("")  # empty line between categories

# # Save all links to a file
# with open("cdn_links.txt", "w") as f:
#     f.write("\n".join(output_lines))

# print("✅ All CDN links saved to cdn_links.txt")
import os

# ==== CHANGE THESE ====
USERNAME = "ojaselawadhi2000"               # your GitHub username
REPO = "Servis-Parts-Images"             # your repo name
ASSETS_FOLDER = "./Assets/PIC_pages_named"        # folder containing your images
# =====================

base_url = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}@main/"
cdn_links = []

# Loop through all files in PartsA folder
for root, dirs, files in os.walk(ASSETS_FOLDER):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            relative_path = os.path.relpath(os.path.join(root, file), ".")
            relative_path = relative_path.replace("\\", "/")  # fix Windows paths
            cdn_link = base_url + relative_path
            cdn_links.append(cdn_link)

# Save all links to a file
with open("PIC_pages_named.txt", "w") as f:
    f.write("\n".join(cdn_links))

print("✅ All CDN links saved to cdn_links.txt")
